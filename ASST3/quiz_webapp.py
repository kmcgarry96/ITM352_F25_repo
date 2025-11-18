"""Web front end for the quiz application.


"""
from flask import Flask, render_template, request, redirect, url_for
import json
import random
import os

"""Web front end for the quiz application."""
from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
import os
import datetime
import time


app = Flask(__name__)
# For session support (development only). In production set from env/secret manager.
app.secret_key = os.environ.get('FLASK_SECRET', 'dev-secret')


def load_questions():
    """Load questions from ASST3/questions.json or fallback to project1/questions.json.
    Normalize to a list of objects with keys: question, alternatives, answer (index).
    """
    base_dir = os.path.dirname(__file__)
    project3_q = os.path.join(base_dir, '..', 'Project3', 'Questions.json')
    local_q = os.path.join(base_dir, 'questions.json')
    fallback_q = os.path.join(base_dir, '..', 'project1', 'questions.json')
    data = None
    # Prefer Project3/Questions.json if the user provided it, then ASST3/questions.json, then fallback
    if os.path.exists(project3_q):
        with open(project3_q, 'r') as f:
            data = json.load(f)
    elif os.path.exists(local_q):
        with open(local_q, 'r') as f:
            data = json.load(f)
    elif os.path.exists(fallback_q):
        with open(fallback_q, 'r') as f:
            content = f.read()
            if content.strip().startswith('```'):
                content = '\n'.join(line for line in content.splitlines() if not line.strip().startswith('```'))
            data = json.loads(content)
    else:
        data = {}

    # If data is a dict (old format: question -> alternatives), convert it.
    if isinstance(data, dict):
        out = []
        for q, alts in data.items():
            # If no explicit answer index provided, assume first option is correct (legacy behavior).
            out.append({'question': q, 'alternatives': alts, 'answer': 0})
        return out
    # If already a list of objects, return as-is
    return data

def load_hints():
    """Load hints from ASST3/hints.json and return a mapping from question text (lowered) to hint string."""
    base_dir = os.path.dirname(__file__)
    hints_path = os.path.join(base_dir, 'hints.json')
    if not os.path.exists(hints_path):
        return {}
    try:
        with open(hints_path, 'r') as f:
            data = json.load(f)
    except Exception:
        return {}

    out = {}
    if isinstance(data, list):
        for item in data:
            q = (item.get('question') or '').strip().lower()
            h = item.get('hint')
            if q and h:
                out[q] = h
    elif isinstance(data, dict):
        # support { question: hint } style too
        for k, v in data.items():
            out[k.strip().lower()] = v
    return out


NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = load_questions()
HINTS = load_hints()
print(f'Loaded {len(QUESTIONS)} questions')


@app.route('/')
def home():
    # Show username input on the home page if not already set in session
    username = session.get('username')
    welcome_msg = None
    # If user is present in session but we haven't shown a welcome message yet,
    # and they exist in the saved users list, prepare a welcome-back message.
    if username and not session.get('welcome_shown'):
        users = load_users()
        for u in users:
            if (u.get('username') or '').strip().lower() == username.strip().lower():
                welcome_msg = f"Welcome back, {username}! Your best score: {u.get('score', 0)}/{u.get('total', '?')}"
                # mark as shown so it doesn't appear on every page load
                session['welcome_shown'] = True
                break

    return render_template('index.html', username=username, welcome_msg=welcome_msg)


@app.route('/setname', methods=['GET', 'POST'])
def setname():
    # GET: show a small page with the name form (prefilled if present)
    if request.method == 'GET':
        return render_template('setname.html', username=session.get('username'))

    # POST: save/remove username then return home
    name = request.form.get('username', '').strip()
    if name:
        # Save the new username and clear the welcome_shown flag so we show
        # a welcome message once on the next home load (if they are a returning user).
        session['username'] = name
        session.pop('welcome_shown', None)
    else:
        session.pop('username', None)
    return redirect(url_for('home'))


def start_new_quiz():
    """Create a per-session randomized quiz payload stored in session.
    Each item stored contains: question, alternatives (shuffled), answer_index.
    """
    chosen = random.sample(QUESTIONS, min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS)))
    quiz_list = []
    for q in chosen:
        alts = list(q['alternatives'])
        random.shuffle(alts)
        correct_text = q['alternatives'][q['answer']] if 'answer' in q else q['alternatives'][0]
        answer_index = alts.index(correct_text)
        # attach any hint we have for this question (by matching question text)
        hint_text = HINTS.get((q.get('question') or '').strip().lower())
        quiz_list.append({'question': q['question'], 'alternatives': alts, 'answer_index': answer_index, 'hint': hint_text})

    session['quiz_questions'] = quiz_list
    session['current'] = 0
    # use float score to allow half-point penalties
    session['score'] = 0.0
    # per-question hint usage tracking: list of booleans parallel to quiz_list
    session['hints_used'] = [False] * len(quiz_list)
    # current_hint holds the hint text for the current question if requested
    session.pop('current_hint', None)
    # timing and basic statistics for the quiz
    session['start_time'] = time.time()
    session['correct_count'] = 0
    session['incorrect_count'] = 0
    session['missed_questions'] = []


@app.route('/hint', methods=['POST'])
def hint():
    """Provide a one-per-quiz hint for the current question and apply penalty.
    If a question object contains a 'hint' field, use that; otherwise auto-generate a small hint.
    """
    # If no quiz in progress, just redirect to quiz
    if 'quiz_questions' not in session:
        return redirect(url_for('quiz'))

    current = session.get('current', 0)
    hints_used = session.get('hints_used', [])
    if current < len(hints_used) and hints_used[current]:
        # hint already used for this question
        return redirect(url_for('quiz'))
    quiz_questions = session.get('quiz_questions', [])
    if current >= len(quiz_questions):
        return redirect(url_for('result'))

    q = quiz_questions[current]
    # use question-provided hint if available
    hint_text = q.get('hint') if isinstance(q, dict) else None
    if not hint_text:
        # auto-generate: reveal first letter and length of correct answer
        try:
            correct = q['alternatives'][q['answer_index']]
            hint_text = f"Starts with '{correct[0]}' and is {len(correct)} characters long."
        except Exception:
            hint_text = "(no hint available)"

    # record that a hint was used for this question; penalty will be applied
    # only if the user answers this question correctly.
    hints_used = session.get('hints_used', [])
    if current < len(hints_used):
        hints_used[current] = True
        session['hints_used'] = hints_used
    session['current_hint'] = hint_text
    return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Initialize quiz for this session on first GET or when 'start' param is present
    if request.method == 'GET' and ('quiz_questions' not in session or request.args.get('start')):
        start_new_quiz()

    quiz_questions = session.get('quiz_questions', [])
    current = session.get('current', 0)

    # If POST, process previous question's answer
    if request.method == 'POST':
        selected = request.form.get('answer')
        if selected is None:
            the_result = 'No answer submitted!'
        else:
            try:
                sel_idx = int(selected)
            except ValueError:
                sel_idx = None

            prev_q = quiz_questions[current]
            if sel_idx is not None and sel_idx == prev_q['answer_index']:
                # Check if a hint was used for this question; penalty applies only when correct
                hints_used = session.get('hints_used', [])
                used_hint = False
                if current < len(hints_used) and hints_used[current]:
                    used_hint = True
                increment = 1.0 - (0.5 if used_hint else 0.0)
                if increment < 0:
                    increment = 0.0
                session['score'] = float(session.get('score', 0.0)) + increment
                the_result = 'Correct!'
                # update correct count
                session['correct_count'] = int(session.get('correct_count', 0)) + 1
            else:
                the_result = 'Incorrect!'
                # update incorrect count and record missed question for review
                session['incorrect_count'] = int(session.get('incorrect_count', 0)) + 1
                try:
                    correct_ans = prev_q['alternatives'][prev_q['answer_index']]
                except Exception:
                    correct_ans = None
                missed = {'question': prev_q.get('question'), 'correct': correct_ans}
                # try to attach explanation if present in original QUESTIONS
                for orig in QUESTIONS:
                    if (orig.get('question') or '') == prev_q.get('question'):
                        if orig.get('explanation'):
                            missed['explanation'] = orig.get('explanation')
                        break
                mq = session.get('missed_questions', [])
                mq.append(missed)
                session['missed_questions'] = mq

        # Advance to next question after showing result; clear current_hint for next question
        session['current'] = current + 1
        session.pop('current_hint', None)
        return render_template('question_result.html', question_result=the_result,
                               question=quiz_questions[current]['question'],
                               answer=(quiz_questions[current]['alternatives'][quiz_questions[current]['answer_index']]))

    # GET handling: show next question or finish
    if current >= len(quiz_questions):
        return redirect(url_for('result'))

    q = quiz_questions[current]
    # whether a hint was used for this question
    hints_used = session.get('hints_used', [])
    hint_used = False
    if current < len(hints_used) and hints_used[current]:
        hint_used = True
    current_hint = session.get('current_hint') if hint_used else None
    return render_template('quiz.html', num=current+1, total=len(quiz_questions), question=q['question'], options=q['alternatives'], hint_used=hint_used, current_hint=current_hint)


def users_file_path():
    return os.path.join(os.path.dirname(__file__), 'users.json')


def load_users():
    path = users_file_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r') as f:
            users = json.load(f)
    except Exception:
        return []

    # Normalize / deduplicate entries by username (case-insensitive).
    # Keep the entry with the highest score; on ties keep the most recent timestamp.
    normalized = {}
    for u in users:
        uname = (u.get('username') or '').strip()
        if not uname:
            # skip nameless entries
            continue
        key = uname.lower()
        existing = normalized.get(key)
        if existing is None:
            normalized[key] = u
        else:
            # prefer higher score
            if u.get('score', 0) > existing.get('score', 0):
                normalized[key] = u
            elif u.get('score', 0) == existing.get('score', 0):
                # prefer later timestamp
                if (u.get('timestamp') or '') > (existing.get('timestamp') or ''):
                    normalized[key] = u

    deduped = list(normalized.values())
    # If deduplication removed entries, persist the cleaned list back to disk
    if len(deduped) != len(users):
        deduped = sorted(deduped, key=lambda x: (-x.get('score', 0), x.get('timestamp', '')))
        try:
            with open(path, 'w') as f:
                json.dump(deduped, f, indent=2)
        except Exception:
            pass
        return deduped

    # No duplicates found; return the list sorted for consistent display
    return sorted(users, key=lambda x: (-x.get('score', 0), x.get('timestamp', '')))


def save_user_entry(entry):
    users = load_users()
    # If the username already exists, update their record with the better score
    uname = (entry.get('username') or '').strip()
    found = None
    for u in users:
        if (u.get('username') or '').strip().lower() == uname.lower():
            found = u
            break

    if found:
        # keep the higher score and most recent timestamp for ties
        if entry.get('score', 0) > found.get('score', 0):
            found['score'] = entry.get('score', 0)
            found['total'] = entry.get('total', found.get('total'))
            found['timestamp'] = entry.get('timestamp', found.get('timestamp'))
        else:
            # optionally update timestamp to most recent attempt
            found['timestamp'] = entry.get('timestamp', found.get('timestamp'))
    else:
        users.append(entry)

    # sort desc by score, then by timestamp
    users = sorted(users, key=lambda x: (-x.get('score', 0), x.get('timestamp', '')))
    path = users_file_path()
    with open(path, 'w') as f:
        json.dump(users, f, indent=2)


@app.route('/result', methods=['GET', 'POST'])
def result():
    score = session.get('score', 0)
    total = len(session.get('quiz_questions', []))

    if request.method == 'POST':
        # Prefer username from session; fall back to form input
        username = session.get('username') or request.form.get('username', '').strip()
        if not username:
            username = 'Anonymous'
        entry = {
            'username': username,
            'score': score,
            'total': total,
            # Use timezone-aware UTC timestamp
            'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        save_user_entry(entry)
        # clear session state
        session.pop('quiz_questions', None)
        session.pop('current', None)
        session.pop('score', None)
        session.pop('start_time', None)
        session.pop('correct_count', None)
        session.pop('incorrect_count', None)
        session.pop('missed_questions', None)
        # redirect to leaderboard and show recent entry position
        return redirect(url_for('leaderboard'))

    # GET: show result and username form
    # compute duration and summary stats
    start = session.get('start_time')
    duration = None
    if start:
        try:
            duration = round(time.time() - float(start), 1)
        except Exception:
            duration = None

    correct_count = session.get('correct_count', 0)
    incorrect_count = session.get('incorrect_count', 0)
    missed = session.get('missed_questions', [])

    return render_template('result.html', score=score, total=total, username=session.get('username'),
                           duration=duration, correct=correct_count, incorrect=incorrect_count,
                           missed=missed)


@app.route('/leaderboard')
def leaderboard():
    users = load_users()
    # already sorted in save, but sort again to be safe
    users_sorted = sorted(users, key=lambda x: (-x.get('score', 0), x.get('timestamp', '')))
    top = users_sorted[:10]
    return render_template('leaderboard.html', top=top)


if __name__ == '__main__':
    app.run(debug=True, port=5003)
    