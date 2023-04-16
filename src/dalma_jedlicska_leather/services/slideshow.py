from typing import Sequence
from attr import define, field

from dalma_jedlicska_leather.services.models import ImageData, ImageLink


@define
class HomeImageData(ImageData):
    height_percent: int
    height_sixth: int
    z_index: int
    ratio: str
    image_link: ImageLink | None = field(default=None)


def get_slideshow_images() -> Sequence[HomeImageData]:
    return [
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_brown-59.webp",
            "foobar",
            100,
            height_sixth=6,
            z_index=0,
            ratio="3/2",
            image_link=ImageLink("/", "home", 45, 66),
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-18.webp",
            "DUMMY THINGHY",
            66,
            4,
            20,
            ratio="2/3",
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-26.webp",
            "DUMMY THINGHY",
            83,
            5,
            10,
            ratio="1/1",
        ),
        HomeImageData(
            "/static/images/jedlicska_dalma_collection -140.webp",
            "DUMMY THINGHY",
            100,
            6,
            0,
            "3/2",
        ),
    ]
