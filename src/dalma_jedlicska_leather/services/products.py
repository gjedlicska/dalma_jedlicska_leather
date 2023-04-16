from typing import Sequence

from attrs import define
from dalma_jedlicska_leather.services.locales import Locale
from dalma_jedlicska_leather.services.models import ImageData


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
