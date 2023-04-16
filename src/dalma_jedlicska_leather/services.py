from typing import Sequence
from attr import field

from attrs import define
from enum import Enum


class Locale(Enum):
    """
    These are the currently supported locale slugs.
    """

    HU = "hu"
    EN = "en"


@define
class ImageData:
    source: str
    description: str


@define
class ImageLink:
    to: str
    alt: str
    x_offset: int
    y_offset: int


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


@define
class ModelData:
    category: str


@define
class ProductData:
    id: str
    image: ImageData
    description: str
    model: ModelData
    price: float
    material_description: str


def get_products(locale: Locale) -> Sequence[ProductData]:
    return [
        ProductData(
            "foo1",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
        ProductData(
            "bar2",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
        ProductData(
            "bar1",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
        ProductData(
            "foo1",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
        ProductData(
            "bar2",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
        ProductData(
            "bar1",
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"
            ),
            "asdfb",
            ModelData("capacitor"),
            123.123,
            "glitter glitter glitter",
        ),
    ]
