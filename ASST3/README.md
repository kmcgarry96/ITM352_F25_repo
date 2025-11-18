Quiz webapp (ASST3)

Quick start (macOS / zsh):

1. Create and activate a virtualenv (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python quiz_webapp.py
```

4. Open in your browser:

http://localhost:5003/

Notes:
- The app stores scores in `users.json` in this folder.
- The server runs in Flask debug mode in development; don't use debug mode in production.
