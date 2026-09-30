from flask import Flask, render_template, request
import re

app = Flask(__name__)


def analyze_text(text: str) -> dict:
    """Return basic statistics for the supplied text."""
    if not text:
        return {
            "characters": 0,
            "words": 0,
            "sentences": 0,
            "spaces": 0,
        }

    # split() handles repeated spaces and new lines naturally for word counting.
    words = len(text.split())

    # A run of sentence-ending punctuation is treated as one sentence.
    sentences = len(re.findall(r"[.!?]+", text))

    return {
        "characters": len(text),
        "words": words,
        "sentences": sentences,
        "spaces": text.count(" "),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    stats = analyze_text("")

    if request.method == "POST":
        text = request.form.get("text", "")
        stats = analyze_text(text)

    return render_template("index.html", text=text, stats=stats)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
