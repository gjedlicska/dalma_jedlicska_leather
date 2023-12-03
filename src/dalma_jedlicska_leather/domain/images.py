from attrs import define


@define
class ImageData:
    source: str
    low_res_source: str
    description: str
