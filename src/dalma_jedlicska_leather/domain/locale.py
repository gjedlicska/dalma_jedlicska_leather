from attrs import define
from enum import Enum


class Locale(Enum):
    """
    These are the currently supported locale slugs.
    """

    HU = "hu"
    EN = "en"


@define
class Price:
    locale: Locale
    value: float

    @property
    def currency(self) -> str:
        return "huf" if self.locale == Locale.HU else "eur"
