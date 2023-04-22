from datetime import datetime
from typing import Sequence
from attrs import define

from dalma_jedlicska_leather.services.models import ImageData


@define
class StoryImage(ImageData):
    full_width: bool = False


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
            "porcelain",
        ),
        ImageData("/static/images/jedlicska_dalma_film_look_brown-64.webp", "brown"),
        [
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
                "porcelain",
                True,
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-21.webp",
                "porcelain",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-34.webp",
                "porcelain",
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_brown-64.webp", "brown", True
            ),
        ],
    ),
    Story(
        "brown",
        "brown",
        datetime(2023, 3, 16),
        ImageData("/static/images/jedlicska_dalma_film_look_brown-64.webp", "brown"),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "porcelain",
        ),
        [
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_brown-64.webp", "brown"
            ),
            StoryImage(
                "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
                "porcelain",
            ),
        ],
    ),
    Story(
        "mud",
        "mud",
        datetime(2021, 10, 10),
        ImageData("/static/images/jedlicska_dalma_collection -140.webp", "mud"),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-32.webp",
            "porcelain",
        ),
        [
            StoryImage("/static/images/jedlicska_dalma_collection -140.webp", "mud"),
            StoryImage(
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
