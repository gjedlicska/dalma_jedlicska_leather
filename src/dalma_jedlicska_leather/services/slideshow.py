from typing import Sequence
from attr import define, field

from dalma_jedlicska_leather.services.models import ImageLink
from dalma_jedlicska_leather.domain.images import ImageData


@define
class HomeImageData(ImageData):
    height_sixth: int
    z_index: int
    ratio: str
    alignment: str = "center"
    image_link: ImageLink | None = field(default=None)


def get_slideshow_images() -> Sequence[HomeImageData]:
    return [
        HomeImageData(
            "/static/images/home/jedlicska_dalma_film_look_brown-64.webp",
            "foobar",
            height_sixth=6,
            z_index=0,
            ratio="3 / 2",
            image_link=ImageLink("/", "home", 45, 66),
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_film_look_porcelain-18.webp",
            "DUMMY THINGHY",
            4,
            3,
            ratio="2 / 3",
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_film_look_porcelain-26.webp",
            "DUMMY THINGHY",
            5,
            2,
            ratio="1 / 1",
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_film_look_porcelain-51.webp",
            "DUMMY THINGHY",
            6,
            0,
            ratio="3 / 2",
        ),
        HomeImageData(
            "/static/images/home/dalma_jedlicska_leather-95.webp",
            "DUMMY THINGHY",
            5,
            2,
            ratio="1 / 1",
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_collection -141 2.webp",
            "DUMMY THINGHY",
            4,
            1,
            ratio="1 / 1",
            alignment="start"
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_collection -173.webp",
            "DUMMY THINGHY",
            4,
            3,
            ratio="2 / 3",
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_collection-136.webp",
            "DUMMY THINGHY",
            6,
            0,
            ratio="3 / 2",
        ),

        HomeImageData(
            "/static/images/home/dalma_jedlicska_leather-129.webp",
            "DUMMY THINGHY",
            5,
            1,
            ratio="1 / 1",
        ),
        HomeImageData(
            "/static/images/home/jedlicska_dalma_film_look_brown-64.webp",
            "DUMMY THINGHY",
            6,
            0,
            ratio="3 / 2",
        ),
    ]
