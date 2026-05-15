from datetime import datetime

from .factory import SourceFactory
from .generator import CarouselGenerator, DefaultSlideStrategy
from .models import ContentItem
from .repository import ContentRepository
from .review import ReviewHighlighter
from .service import ContentService


def build_sample_items() -> list[ContentItem]:
    return [
        ContentItem(
            content_id="blog-101",
            title="Como reduzimos o tempo de build em 30%",
            url="https://empresa.blog/build-30",
            published_at=datetime(2026, 5, 10),
            body="Explicamos a nova pipeline de CI. Mostramos cache em etapas criticas."
            " Indicamos ganhos por equipe.",
            source="blog",
        ),
        ContentItem(
            content_id="rel-210",
            title="Release 2.1 com novo modulo de alertas",
            url="https://empresa.repo/releases/2.1",
            published_at=datetime(2026, 5, 12),
            body="O sistema agora destaca termos sensiveis automaticamente."
            " O recurso reduz risco de publicacao tecnica.",
            source="release",
        ),
    ]


def main() -> None:
    factory = SourceFactory()
    items = build_sample_items()
    sources = [
        factory.create("blog", {"items": [items[0]]}),
        factory.create("release", {"items": [items[1]]}),
    ]

    repository = ContentRepository()
    generator = CarouselGenerator(DefaultSlideStrategy())
    highlighter = ReviewHighlighter(["termos sensiveis", "risco", "alertas"])
    service = ContentService(sources, repository, generator, highlighter)

    scripts = service.detect_and_generate()
    for script in scripts:
        print(f"Roteiro para {script.content_id} usando {script.strategy_name}")
        for slide in script.slides:
            flag = f" [revisar: {', '.join(slide.highlights)}]" if slide.highlights else ""
            print(f"{slide.index}. {slide.title}: {slide.body}{flag}")


if __name__ == "__main__":
    main()
