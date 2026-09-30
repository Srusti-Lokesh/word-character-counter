# Project Report — Word & Character Counter

## 1. Introduction

The Word & Character Counter is a Python Flask web application created for a text-processing internship task. The application accepts a paragraph and calculates four basic statistics: characters, words, sentences, and spaces.

## 2. Objective

The objective is to practice Python string manipulation and basic text processing while producing a simple deployable web application.

## 3. Requirements addressed

| Requirement | Implementation |
|---|---|
| Accept a paragraph | HTML textarea + Flask POST form |
| Character count | `len(text)` |
| Word count | `len(text.split())` |
| Sentence count | Regular expression for `.`, `!`, `?` |
| Space count | `text.count(" ")` |
| Empty input | Returns zero for all statistics |
| Deployment | Render configuration via `render.yaml` |
| Documentation | README and rollback procedure |
| Testing | Python `unittest` test suite |

## 4. Technologies

- Python 3.13.5
- Flask 3.1.2
- Gunicorn 23.0.0
- HTML5
- CSS3
- Git and GitHub
- Render

## 5. Application workflow

1. User opens the web page.
2. User enters or pastes a paragraph.
3. User submits the form.
4. Flask receives the text through a POST request.
5. `analyze_text()` calculates the four statistics.
6. The results are rendered back into the page.
7. The user can clear the input and analyze another paragraph.

## 6. String-processing logic

### Characters

```python
len(text)
```

Counts every character in the submitted string, including spaces and punctuation.

### Words

```python
len(text.split())
```

Splits on whitespace and counts the resulting non-empty tokens.

### Sentences

```python
len(re.findall(r"[.!?]+", text))
```

Counts runs of sentence-ending punctuation. This is intentionally a basic educational approach rather than a full natural-language sentence parser.

### Spaces

```python
text.count(" ")
```

Counts ordinary space characters.

## 7. Empty-input handling

When the input is empty, the application returns:

- Characters: 0
- Words: 0
- Sentences: 0
- Spaces: 0

This prevents errors and satisfies the project hint.

## 8. Testing

The project includes automated tests for:

- Empty input.
- Basic sentence counting.
- Multiple sentences.
- GET page availability.
- POST form processing.

Run:

```powershell
python -m unittest discover -s tests -v
```

## 9. Deployment

Render is configured as a Python Web Service. The production build command is:

```text
pip install -r requirements.txt
```

The production start command is:

```text
gunicorn app:app
```

The repository also includes `render.yaml` so the deployment settings are stored with the project.

## 10. Rollback

A known-good release can be tagged:

```powershell
git tag -a v1.0.0 -m "Known-good release"
git push origin v1.0.0
```

If a later change must be undone, a Git revert can be created:

```powershell
git revert <BAD_COMMIT_SHA>
git push origin main
```

The repository contains `docs/rollback-evidence.md` with the full procedure and evidence checklist.

## 11. Conclusion

The project demonstrates fundamental Python string operations, a simple Flask request/response workflow, automated testing, Git version control, and cloud deployment preparation. It is suitable as a small internship project demonstrating basic text processing and deployment practices.

## 12. References

Render Flask guide:
https://render.com/docs/deploy-flask

Render first deployment:
https://render.com/docs/your-first-deploy

GitHub command-line repository guide:
https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
