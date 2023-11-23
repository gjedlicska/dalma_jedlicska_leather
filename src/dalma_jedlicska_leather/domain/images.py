from attrs import define


@define
class ImageData:
    source: str
    description: str
    low_res_source: str
