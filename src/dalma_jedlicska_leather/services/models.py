from attr import define


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
