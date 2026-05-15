import unittest
from datetime import datetime

from app.generator import CarouselGenerator, DefaultSlideStrategy
from app.models import ContentItem


class CarouselGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = CarouselGenerator(DefaultSlideStrategy())

    def test_generate_slides_success(self) -> None:
        item = ContentItem(
            content_id="blog-10",
            title="Titulo A",
            url="https://blog/a",
            published_at=datetime(2026, 5, 10),
            body="Ponto um. Ponto dois. Ponto tres.",
            source="blog",
        )

        script = self.generator.generate(item)

        self.assertGreaterEqual(len(script.slides), 3)
        self.assertEqual("Abertura", script.slides[0].title)

    def test_generate_slides_missing_body_failure(self) -> None:
        item = ContentItem(
            content_id="blog-10",
            title="Titulo A",
            url="https://blog/a",
            published_at=datetime(2026, 5, 10),
            body=" ",
            source="blog",
        )

        with self.assertRaises(ValueError):
            self.generator.generate(item)

    def test_generate_slides_single_sentence_edge(self) -> None:
        item = ContentItem(
            content_id="blog-10",
            title="Titulo A",
            url="https://blog/a",
            published_at=datetime(2026, 5, 10),
            body="Unico ponto.",
            source="blog",
        )

        script = self.generator.generate(item)

        self.assertEqual(3, len(script.slides))
        self.assertEqual("Encerramento", script.slides[-1].title)


if __name__ == "__main__":
    unittest.main()
