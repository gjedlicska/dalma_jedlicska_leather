from typing import Sequence
from attr import define, field

from dalma_jedlicska_leather.services.models import ImageLink
from dalma_jedlicska_leather.domain.images import ImageData


@define
class HomeImageData(ImageData):
    height_sixth: int
    z_index: int
    ratio: str
    image_link: ImageLink | None = field(default=None)


def get_slideshow_images() -> Sequence[HomeImageData]:
    return [
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_brown-59.webp",
            "/static/images/jedlicska_dalma_film_look_brown-59_blur.webp",
            "foobar",
            height_sixth=6,
            z_index=0,
            ratio="3 / 2",
            image_link=ImageLink("/", "home", 45, 66),
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-18.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-18_blur.webp",
            "DUMMY THINGHY",
            4,
            3,
            ratio="2 / 3",
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-26.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-26_blur.webp",
            "DUMMY THINGHY",
            5,
            2,
            ratio="1 / 1",
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_collection -141.webp",
            "/static/images/jedlicska_dalma_collection -141_blur.webp",
            "DUMMY THINGHY",
            6,
            1,
            ratio="1 / 1",
        ),
        HomeImageData(
            "/static/images/dalma-jedlicska-leather-15.webp",
            "/static/images/dalma-jedlicska-leather-15_blur.webp",
            "DUMMY THINGHY",
            4,
            2,
            ratio="3 / 2",
        ),
    ]
