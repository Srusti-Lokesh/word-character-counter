# Word & Character Counter

A small Python + Flask text-analysis web application for the internship task **Create a Word and Character Counter**.

## Project objective

Accept a paragraph and calculate:
- Number of characters
- Number of words
- Number of sentences
- Number of spaces

The project also handles empty input and demonstrates basic Python string manipulation.

## Features

- Clean responsive web interface.
- Paragraph input using a textarea.
- Character count using `len(text)`.
- Word count using `text.split()`.
- Sentence count using `.`, `!`, and `?`.
- Space count using `text.count(" ")`.
- Empty-input handling.
- Automated unit tests.
- Render deployment configuration.
- Git rollback procedure/documentation.

## Technology stack

- Python 3.13.5
- Flask 3.1.2
- Gunicorn 23.0.0
- HTML5
- CSS3
- Git/GitHub
- Render

## Project structure

```text
word_character_counter_project/
├── app.py
├── requirements.txt
├── render.yaml
├── .python-version
├── .gitignore
├── README.md
├── sample_paragraph.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
│   └── test_app.py
└── docs/
    └── rollback-evidence.md
```

## Run locally on Windows PowerShell

### 1. Check Python and Git

```powershell
python --version
git --version
```

Python 3.13.x is recommended for matching the included `.python-version`.

### 2. Open the project folder

```powershell
cd "C:\PATH\TO\word_character_counter_project"
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use this only for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run tests

```powershell
python -m unittest discover -s tests -v
```

### 7. Start the application

```powershell
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Stop the local server with `Ctrl+C`.

### 8. Optional production-style local test

```powershell
gunicorn app:app
```

On Windows, Gunicorn itself is normally used on Linux-based production servers such as Render. For Windows local testing, `python app.py` is sufficient.

## GitHub submission

Create a **public** repository named:

```text
word-character-counter
```

Suggested GitHub repository description:

> Python Flask web app that analyzes a paragraph and counts characters, words, sentences, and spaces. Includes tests, Render deployment configuration, and rollback documentation.

Do not upload `.venv/`, secrets, or `.env` files.

### First GitHub push from PowerShell

Run these commands from the project folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial release - Word and Character Counter"
git remote add origin https://github.com/YOUR-USERNAME/word-character-counter.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

### Verify

```powershell
git status
git log --oneline --decorate -5
git remote -v
```

The GitHub repository should contain the source code, README, tests, Render configuration, and rollback documentation.

## Render deployment

The included `render.yaml` already defines:

- Runtime: Python
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Plan: Free
- Auto deploy: enabled

### Dashboard method

1. Sign in to Render.
2. Connect your GitHub account.
3. Select **New → Web Service**.
4. Select the `word-character-counter` repository.
5. Use branch `main`.
6. Confirm the Python runtime.
7. Confirm:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
8. Select the Free plan if appropriate for the assignment.
9. Create the Web Service.
10. Wait for the build/deploy to finish.
11. Open the generated `onrender.com` URL.
12. Enter a sample paragraph and verify all four statistics.

Render can automatically redeploy when new commits are pushed to the selected branch.

## Deployment verification checklist

Use this before submission:

- [ ] GitHub repository is public.
- [ ] README is present and accurate.
- [ ] `requirements.txt` is present.
- [ ] `render.yaml` is present.
- [ ] `.python-version` is present.
- [ ] Local tests pass.
- [ ] Local web page opens.
- [ ] Render build succeeds.
- [ ] Render service is live.
- [ ] Live URL loads without errors.
- [ ] Text analysis works on the live URL.
- [ ] Empty input works.
- [ ] Screenshots of GitHub and Render are saved for evidence.
- [ ] Rollback evidence/procedure is documented.
- [ ] Repository URL is submitted through the internship portal.
- [ ] LinkedIn post is published.

## Interview questions

### What does `split()` do?

`split()` breaks a string into a list of pieces using whitespace by default. Therefore `len(text.split())` provides a simple word count.

### What is the difference between `len()` and `count()`?

`len()` returns the number of items in a string (characters for a string). `count()` returns how many times a specified substring occurs. For example, `text.count(" ")` counts ordinary spaces.

### How are strings represented in Python?

Python strings are immutable sequences of Unicode characters. They can be written using single quotes, double quotes, or triple quotes.

## Submission evidence

Recommended screenshots:
1. GitHub repository main page.
2. GitHub file list showing `README.md`, `requirements.txt`, `render.yaml`, `app.py`, `tests/`, etc.
3. Successful Render deployment/deploy log.
4. Live Render application.
5. Live result after entering the sample paragraph.
6. Git tag/commit or rollback evidence, if required.

## Official deployment references

- Render Flask deployment guide: https://render.com/docs/deploy-flask
- Render first deployment guide: https://render.com/docs/your-first-deploy
- GitHub guide for adding local code: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
