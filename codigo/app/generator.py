from abc import ABC, abstractmethod
from typing import List, Optional

from .models import CarouselScript, CarouselSlide, ContentItem
from .llm_facade import LlmFacade


class SlideStrategy(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_slides(self, item: ContentItem) -> List[CarouselSlide]:
        raise NotImplementedError


class DefaultSlideStrategy(SlideStrategy):
    def __init__(self, facade: Optional[LlmFacade] = None) -> None:
        self._facade = facade or LlmFacade()

    @property
    def name(self) -> str:
        return "tech_educative"

    def generate_slides(self, item: ContentItem) -> List[CarouselSlide]:
        if not item.title:
            raise ValueError("content title is required")
        body = item.body.strip()
        if not body:
            raise ValueError("content body is required")

        points = self._facade.generate_points(body)
        if not points:
            raise ValueError("content body has no sentences")

        slides: List[CarouselSlide] = []
        slides.append(CarouselSlide(index=1, title="Abertura", body=f"O que mudou: {item.title}"))
        for offset, point in enumerate(points[:3], start=2):
            slides.append(CarouselSlide(index=offset, title=f"Slide {offset - 1}", body=point))
        slides.append(
            CarouselSlide(
                index=len(slides) + 1,
                title="Encerramento",
                body="Resumo e proximo passo: leia o conteudo completo.",
            )
        )
        return slides


class CarouselGenerator:
    def __init__(self, strategy: SlideStrategy) -> None:
        self._strategy = strategy

    def generate(self, item: ContentItem) -> CarouselScript:
        slides = self._strategy.generate_slides(item)
        return CarouselScript(content_id=item.content_id, slides=slides, strategy_name=self._strategy.name)
