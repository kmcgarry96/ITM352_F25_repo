"""Simple smoke test for the quiz webapp.

AI assistance note:
- This script was created with the help of an AI assistant using the prompt:
    "Create a small Python script that requests /, /quiz?start=1 and /leaderboard and prints HTTP status codes." 
    The developer reviewed and adapted the script before committing.

Run while the server is running (default http://127.0.0.1:5003).
"""
import requests


def main():
    base = "http://127.0.0.1:5003"
    endpoints = ["/", "/quiz?start=1", "/leaderboard"]
    all_ok = True
    for p in endpoints:
        try:
            r = requests.get(base + p, timeout=5)
            print(p, r.status_code, "len:", len(r.text))
            if r.status_code != 200:
                all_ok = False
        except Exception as e:
            print(p, "ERROR:", e)
            all_ok = False

    if all_ok:
        print("SMOKE TEST PASSED")
    else:
        print("SMOKE TEST FAILED")


if __name__ == '__main__':
    main()
