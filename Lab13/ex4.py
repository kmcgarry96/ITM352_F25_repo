# Flask Quiz Game Skeleton - Based on Project 1 quiz.py
# Approach iii: Converting existing terminal quiz to web application

from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import time
import json
from string import ascii_lowercase

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this for production

# Quiz questions from your original quiz.py
QUESTIONS = {
    "What is the capital of France?": ["London", "Berlin", "Paris", "Madrid"],
    "Who painted the Mona Lisa?": ["Van Gogh", "Picasso", "Da Vinci", "Monet"],
    "What year did World War II end?": ["1944", "1945", "1946", "1947"],
    "What is the largest planet?": ["Earth", "Mars", "Jupiter", "Saturn"],
    "Who wrote Romeo and Juliet?": ["Dickens", "Shakespeare", "Austen", "Tolkien"]
}

# Correct answers (index 2 for Paris, Da Vinci, 1945, Jupiter, Shakespeare)
CORRECT_ANSWERS = {
    "What is the capital of France?": "Paris",
    "Who painted the Mona Lisa?": "Da Vinci", 
    "What year did World War II end?": "1945",
    "What is the largest planet?": "Jupiter",
    "Who wrote Romeo and Juliet?": "Shakespeare"
}

@app.route('/')
def index():
    """Home page - Quiz introduction and start"""
    return '''
    <html>
    <head><title>McGarry's Quiz Game</title></head>
    <body>
        <h1>Welcome to McGarry's History Quiz!</h1>
        <p>Test your knowledge with our interactive quiz</p>
        <a href="/login">Login/Register</a><br>
        <a href="/quiz">Start Quiz (Guest)</a><br>
        <a href="/leaderboard">View High Scores</a>
    </body>
    </html>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/registration page"""
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        session['start_time'] = time.time()
        return redirect(url_for('quiz'))
    
    return '''
    <html>
    <head><title>Login - Quiz Game</title></head>
    <body>
        <h2>Enter Your Name</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Your name" required>
            <button type="submit">Start Quiz</button>
        </form>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/quiz')
def quiz():
    """Main quiz page - displays questions"""
    # Initialize quiz session if not exists
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
        session['questions'] = list(QUESTIONS.keys())
        random.shuffle(session['questions'])
        session['start_time'] = time.time()
    
    current_q = session['current_question']
    
    # Check if quiz is complete
    if current_q >= len(session['questions']):
        return redirect(url_for('results'))
    
    question = session['questions'][current_q]
    options = QUESTIONS[question]
    
    html = f'''
    <html>
    <head><title>Quiz Question {current_q + 1}</title></head>
    <body>
        <h2>Question {current_q + 1} of {len(session['questions'])}</h2>
        <h3>{question}</h3>
        <form method="POST" action="/answer">
    '''
    
    # Add options with radio buttons
    for i, option in enumerate(options):
        html += f'<input type="radio" name="answer" value="{option}" id="opt{i}">'
        html += f'<label for="opt{i}">{ascii_lowercase[i]}) {option}</label><br>'
    
    html += '''
            <br><button type="submit">Submit Answer</button>
        </form>
        <p>Score: ''' + str(session['score']) + '''</p>
    </body>
    </html>
    '''
    
    return html

@app.route('/answer', methods=['POST'])
def answer():
    """Process quiz answer"""
    current_q = session['current_question']
    question = session['questions'][current_q]
    user_answer = request.form['answer']
    correct_answer = CORRECT_ANSWERS[question]
    
    # Check if answer is correct
    if user_answer == correct_answer:
        session['score'] += 1
        flash(f"Correct! The answer is {correct_answer}")
    else:
        flash(f"Wrong! The correct answer is {correct_answer}")
    
    # Move to next question
    session['current_question'] += 1
    
    return redirect(url_for('quiz'))

@app.route('/results')
def results():
    """Display quiz results"""
    total_time = time.time() - session.get('start_time', time.time())
    score = session.get('score', 0)
    total_questions = len(session.get('questions', []))
    username = session.get('username', 'Guest')
    
    # Reset session for new quiz
    session.pop('current_question', None)
    session.pop('questions', None)
    
    return f'''
    <html>
    <head><title>Quiz Results</title></head>
    <body>
        <h1>Quiz Complete!</h1>
        <h2>Results for {username}</h2>
        <p>Score: {score}/{total_questions} ({score/total_questions*100:.1f}%)</p>
        <p>Time taken: {total_time:.1f} seconds</p>
        <a href="/quiz">Take Quiz Again</a><br>
        <a href="/">Home</a><br>
        <a href="/leaderboard">View Leaderboard</a>
    </body>
    </html>
    '''

@app.route('/leaderboard')
def leaderboard():
    """Display high scores (skeleton - would load from JSON file)"""
    return '''
    <html>
    <head><title>High Scores</title></head>
    <body>
        <h1>Leaderboard</h1>
        <p>High scores would be displayed here</p>
        <p>(Feature to be implemented with JSON file storage)</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5002)
