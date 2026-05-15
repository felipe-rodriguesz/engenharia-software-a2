from typing import Iterable, List

from .generator import CarouselGenerator
from .models import CarouselScript, ContentItem
from .repository import ContentRepository
from .review import ReviewHighlighter
from .sources import ContentSource


class ContentService:
    def __init__(
        self,
        sources: Iterable[ContentSource],
        repository: ContentRepository,
        generator: CarouselGenerator,
        highlighter: ReviewHighlighter,
    ) -> None:
        self._sources = list(sources)
        self._repository = repository
        self._generator = generator
        self._highlighter = highlighter

    def detect_new_items(self) -> List[ContentItem]:
        items: List[ContentItem] = []
        for source in self._sources:
            items.extend(source.fetch_items())
        return self._repository.register_new_items(items)

    def generate_script_for(self, item: ContentItem) -> CarouselScript:
        script = self._generator.generate(item)
        marked_slides = self._highlighter.mark(script.slides)
        return CarouselScript(
            content_id=script.content_id,
            slides=marked_slides,
            strategy_name=script.strategy_name,
        )

    def detect_and_generate(self) -> List[CarouselScript]:
        scripts: List[CarouselScript] = []
        for item in self.detect_new_items():
            scripts.append(self.generate_script_for(item))
        return scripts
