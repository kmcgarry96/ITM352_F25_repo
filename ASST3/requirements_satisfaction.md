Requirements Satisfaction - Quiz Webapp (ASST3)

This document maps the assignment requirements to the implementation in this repository and provides evidence (files, behavior, and tests) that each core requirement has been satisfied. The project was implemented using Flask and local JSON data files.

Summary status (core areas):
- Functional requirements: PASS (core functionality implemented)
- Individual requirements requested by the student: PASS for #2 (Leaderboard) and #5 (Hint System)
- Documentation & tests: PASS (README, requirements.txt, smoke_test.py)

Files to inspect (key files):
- `quiz_webapp.py` - Flask backend, routing, session handling, scoring, hint logic, persistence
- `templates/*.html` - Jinja templates for UI (index.html, quiz.html, question_result.html, result.html, leaderboard.html, setname.html)
- `questions.json`, `hints.json` - question and hint data
- `users.json` - persisted leaderboard data (updated when a user saves their score)
- `smoke_test.py` - automated smoke test for core endpoints
- `requirements.txt` and `README.md` - setup instructions and dependencies

Functional Requirement Checklist

1) Convert console quiz to Flask web app
- Evidence: `quiz_webapp.py` defines Flask app, routes (`/`, `/setname`, `/quiz`, `/hint`, `/result`, `/leaderboard`).
- Status: PASS

2) UI/UX with HTML/CSS/Jinja (basic)
- Evidence: `templates/` directory contains Jinja templates rendering dynamic content. Minimal CSS present; the UI is functional and clean but intentionally simple.
- Status: PASS (meets basic requirement)

3) Load questions dynamically from JSON and randomize
- Evidence: `load_questions()` reads `questions.json`; `start_new_quiz()` selects randomized questions and shuffles alternatives.
- Status: PASS

4) Real-time feedback and score tracking
- Evidence: After submitting an answer, `/quiz` POST renders `question_result.html` showing Correct/Incorrect. Score is tracked in `session['score']` and adjusted per question.
- Status: PASS

5) Data management & backend storage
- Evidence: Questions and hints are JSON files. Scores are saved to `users.json` via `save_user_entry()`. `load_users()` reads and normalizes persisted entries.
- Status: PASS

6) Use Flask and RESTful-like endpoints
- Evidence: App uses Flask. Endpoints serve HTML and could be adapted to return JSON for an API; current routes handle retrieving questions and saving user scores server-side.
- Status: PASS

7) Final score & feedback
- Evidence: `/result` shows final score and allows saving a username; saved entries appear in `/leaderboard`.
- Status: PASS

8) Error handling & validation
- Evidence: Basic validation exists (username trimmed; JSON load guarded). More advanced validations (e.g., rate-limiting, strict schema validation) are not necessary for assignment scope.
- Status: PARTIAL (basic handling implemented)

Non-Functional Requirements

- Documentation
  - Evidence: `README.md` contains setup and run instructions. This mapping file documents how requirements are satisfied.
  - Status: PASS

- Performance
  - Evidence: Small app using local JSON files; operations are fast for small data sets. Smoke test verifies endpoints respond quickly.
  - Status: PASS (suitable for assignment)

- Tests & QA
  - Evidence: `smoke_test.py` verifies core endpoints. Manual test performed: started server, ran smoke test, completed a full quiz flow and saved a score to `users.json`.
  - Status: PASS (basic QA)

Individual Requirements (student-specified: #2 and #5)

- Requirement #2 — Leaderboard System
  - Requirement: After completing the quiz, ask user for name and implement a global leaderboard (top 10) with ranking.
  - Evidence:
    - `result()` route (in `quiz_webapp.py`) accepts POST with username and saves score/timestamp using `save_user_entry()`.
    - `leaderboard()` route reads `users.json`, sorts entries and renders `templates/leaderboard.html`.
    - `templates/leaderboard.html` shows top entries with score and timestamp.
    - Manual test: Completed quiz and saved score; new entry appended to `users.json` and displayed on leaderboard.
  - Status: PASS

- Requirement #5 — Hint System
  - Requirement: Allow users to request a hint per question; deduct points or limit hints.
  - Evidence:
    - `/hint` POST route provides a hint for the current question and sets `session['hints_used'][current] = True`.
    - `quiz()` POST scoring checks `hints_used` and applies a 0.5-point penalty when the user answers correctly after using a hint.
    - `templates/quiz.html` shows a "Use Hint" button and displays the hint when used.
    - Manual test: Used hint during a question and observed reduced increment on correct answer.
  - Status: PASS

Use of AI
- Several small non-functional improvements and helper files were created with the assistance of an AI coding assistant (documented in file headers):
  - `quiz_webapp.py` top contains an "AI assistance note" comment describing which changes were AI-assisted.
  - `smoke_test.py` contains a short AI-assistance note describing the prompt used.
- All AI-generated code or suggestions were reviewed and adjusted by the developer before committing. This complies with the assignment requirement to disclose AI use.

How this was verified (tests run)
- Manual verification: Started the Flask server and walked the full quiz flow (set name, start quiz, answer questions, save score), then viewed the leaderboard.
- Automated smoke test: `smoke_test.py` was run against the locally running server and confirmed the three endpoints returned HTTP 200 during testing.

Notes and suggested improvements (optional / extra credit)
- Add a timed quiz mode (timer) and difficulty levels — not implemented here but straightforward to add using session state and additional question metadata.
- Add responsive design CSS or Bootstrap for a polished UI.
- Add unit tests with pytest for route-level checks and behavior around `save_user_entry()` and `load_users()`.

Conclusion
- The core functional requirements for converting the quiz to a web application are implemented.
- The student's individual requirements #2 (Leaderboard) and #5 (Hint System) are implemented and verified.

If you want, I can now:
- Add a small unit test for `save_user_entry()` (quick, ~15–20 minutes), or
- Implement one small optional improvement (e.g., make templates responsive with Bootstrap, ~20–40 minutes).

