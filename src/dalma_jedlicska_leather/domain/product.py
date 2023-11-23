from typing import List
from attrs import define
from dalma_jedlicska_leather.domain.locale import Price
from dalma_jedlicska_leather.domain.images import ImageData


@define
class Model:
    name: str
    category: str
    prices: List[Price]


@define
class Product:
    id: str
    description: str
    model: Model
    color: str
    material_description: str
    display_images: List[ImageData]
