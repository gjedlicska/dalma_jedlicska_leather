from datetime import datetime
from typing import Sequence
from attrs import define

from dalma_jedlicska_leather.domain.images import ImageData


@define
class StoryImage(ImageData):
    full_width: bool = False
    width_percentage: float = 100
    padding: int = 0


@define
class Story:
    name: str
    slug: str
    date: datetime
    cover_image: ImageData
    hover_image: ImageData
    images: list[StoryImage]


stories = [
    Story(
        "porcelain",
        "porcelain",
        datetime(2023, 3, 16),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "porcelain",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_brown-64.webp",
            "/static/images/jedlicska_dalma_film_look_brown-64.webp",
            "brown",
        ),
        [
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
                "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
                "porcelain",
                full_width=True,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-21.webp",
                "/static/images/jedlicska_dalma_film_look_porcelain-21.webp",
                "porcelain",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-34.webp",
                "/static/images/jedlicska_dalma_film_look_porcelain-34.webp",
                "porcelain",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-54.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-54.jpg",
                "brown",
                full_width=True,
                width_percentage=50,
                padding=14,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-32.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-32.jpg",
                "porcelain",
                full_width=True,
                width_percentage=70,
                padding=14,
            ),
            # some fake gap creator images
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "porcelain",
                full_width=True,
                width_percentage=0,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "porcelain",
                full_width=True,
                width_percentage=0,
            ),
            # hack above
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-16.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-16.jpg",
                "porcelain",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "porcelain",
                width_percentage=75,
            ),
            # some fake gap creator images
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "porcelain",
                full_width=True,
                width_percentage=0,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-35.jpg",
                "porcelain",
                full_width=True,
                width_percentage=0,
            ),
            # hack above
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-3.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-3.jpg",
                "porcelain",
                width_percentage=75,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-61.jpg",
                "/static/images/jedlicska_dalma_film_look_porcelain-61.jpg",
                "porcelain",
            ),
        ],
    ),
    Story(
        "brown",
        "brown",
        datetime(2023, 3, 16),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_brown-64.webp",
            "/static/images/jedlicska_dalma_film_look_brown-64.webp",
            "brown",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "porcelain",
        ),
        [
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_brown-64.webp",
                "/static/images/jedlicska_dalma_film_look_brown-64.webp",
                "brown",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
                "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
                "porcelain",
            ),
        ],
    ),
    Story(
        "mud",
        "mud",
        datetime(2021, 10, 10),
        ImageData(
            "/static/images/jedlicska_dalma_collection -140.webp",
            "/static/images/jedlicska_dalma_collection -140.webp",
            "mud",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "porcelain",
        ),
        [
            StoryImage(
                "/static/images/jedlicska_dalma_collection -140.webp",
                "/static/images/jedlicska_dalma_collection -140.webp",
                "mud",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
                "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
                "porcelain",
            ),
        ],
    ),
]


async def get_stories() -> Sequence[Story]:
    return stories


async def get_story(story_id: str) -> Story | None:
    filtered_stories = [st for st in stories if st.slug == story_id]
    if not filtered_stories:
        return None
    return filtered_stories[0]
