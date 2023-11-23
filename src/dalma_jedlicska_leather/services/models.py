from attr import define


@define
class ImageLink:
    to: str
    alt: str
    x_offset: int
    y_offset: int
