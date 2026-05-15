import unittest
from datetime import datetime

from app.models import ContentItem
from app.repository import ContentRepository


class ContentRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = ContentRepository()

    def test_register_new_items_success(self) -> None:
        items = [
            ContentItem(
                content_id="blog-1",
                title="Titulo A",
                url="https://blog/a",
                published_at=datetime(2026, 5, 10),
                body="Texto A.",
                source="blog",
            ),
            ContentItem(
                content_id="blog-2",
                title="Titulo B",
                url="https://blog/b",
                published_at=datetime(2026, 5, 11),
                body="Texto B.",
                source="blog",
            ),
        ]

        new_items = self.repo.register_new_items(items)

        self.assertEqual(2, len(new_items))
        self.assertEqual("blog-1", new_items[0].content_id)
        self.assertIsNotNone(self.repo.get_item("blog-2"))

    def test_register_new_items_duplicate_edge(self) -> None:
        item = ContentItem(
            content_id="blog-1",
            title="Titulo A",
            url="https://blog/a",
            published_at=datetime(2026, 5, 10),
            body="Texto A.",
            source="blog",
        )

        new_items = self.repo.register_new_items([item, item])

        self.assertEqual(1, len(new_items))

    def test_register_new_items_missing_id_failure(self) -> None:
        item = ContentItem(
            content_id="",
            title="Titulo A",
            url="https://blog/a",
            published_at=datetime(2026, 5, 10),
            body="Texto A.",
            source="blog",
        )

        with self.assertRaises(ValueError):
            self.repo.register_new_items([item])


if __name__ == "__main__":
    unittest.main()
