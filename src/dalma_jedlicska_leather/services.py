from typing import Sequence

from attrs import define


@define
class ImageData:
    source: str
    description: str


def get_slideshow_images() -> Sequence[ImageData]:
    return [
        ImageData("/images/jedlicska_dalma_collection -3.webp", "DUMMY THINGHY"),
        ImageData("/images/jedlicska_dalma_collection -138.webp", "DUMMY THINGHY"),
        ImageData("/images/jedlicska_dalma_collection -140.webp", "DUMMY THINGHY"),
    ]
