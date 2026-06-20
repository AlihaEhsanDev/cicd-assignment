# CI/CD Fundamentals with a Python Web API — Completed Solution

## Files included
- `main.py` — FastAPI Task Manager API
- `requirements.txt` — dependencies
- `test_main.py` — 4 passing pytest tests
- `.github/workflows/ci.yml` — GitHub Actions workflow with `test` and `deploy` jobs
- `REFLECTION.md` — wrap-up reflection

## Run locally
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

## Run tests
```bash
pytest -v
```

## Important
For the assignment's screenshot requirement, you still need to:
1. Push this project to GitHub.
2. Open the **Actions** tab.
3. Let one workflow pass (green).
4. Intentionally break a test or formatting rule and push again to capture a failed run (red).
5. Fix it and push again.

Then add those screenshots to your submission.
