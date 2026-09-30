import unittest
from app import app, analyze_text


class TextAnalysisTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(
            analyze_text(""),
            {"characters": 0, "words": 0, "sentences": 0, "spaces": 0},
        )

    def test_basic_sentence(self):
        self.assertEqual(
            analyze_text("Hello world!"),
            {"characters": 12, "words": 2, "sentences": 1, "spaces": 1},
        )

    def test_multiple_sentences(self):
        stats = analyze_text("Python is useful. It is simple! Is it fun?")
        self.assertEqual(stats["words"], 8)
        self.assertEqual(stats["sentences"], 3)
        self.assertEqual(stats["spaces"], 7)

    def test_flask_page(self):
        client = app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_analysis(self):
        client = app.test_client()
        response = client.post("/", data={"text": "One two. Three!"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Characters", response.data)


if __name__ == "__main__":
    unittest.main()
