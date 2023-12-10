from attrs import define
from pathlib import Path


@define
class ImageData:
    source: str
    description: str

    @property
    def low_res_source(self) -> str:
        p = Path(self.source)
        low_res_path = p.with_stem(f"{p.stem}_blur")
        if Path(f".{low_res_path}").exists():
            return str(low_res_path)

        # TODO: raise error on this, to ensure image is persent
        return self.source

