from typing import Iterable, Protocol
from dalma_jedlicska_leather.domain.locale import Locale, Price
from dalma_jedlicska_leather.domain.images import ImageData
from dalma_jedlicska_leather.domain.product import Model, Product


class ProductQuery(Protocol):
    model: str | None
    color: str | None


_products = [
    Product(
        id="foo1",
        description="""A KLEIO közepes méretű hátitáska geometriai sziluettje izgalmas kontrasztot alkot a lágy ívekkel. A hosszan futó cipzáras záródás megkönnyíti a belső tér használatát, míg a bőrbetétek biztosítják, hogy a táska szélesen kinyíljon, miközben minden érték biztonságban marad.

Válogatott olasz marhabőrből készül, belseje teljes felületen sertés bőrrel kasírozott. A nagy főrekeszen kívül egy belső lapos kis zsebbel és egy külső kis cipzáras zsebbel rendelkezik. Záródása fémcipzárral biztosított. Vállpántja állítható hosszúságú.  """,
        model=Model(
            name="capacitor",
            category="crossbody",
            prices=[Price(Locale.HU, 90000)],
        ),
        color="blue",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            ),
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            ),
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            ),
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            ),
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "clutch", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
    Product(
        id="bar2",
        description="asdfb",
        model=Model("akela", "crossbody", [Price(Locale.HU, 90000)]),
        color="grey",
        material_description="glitter glitter glitter",
        display_images=[
            ImageData(
                "/static/images/jedlicska_dalma_collection -3.webp",
                "/static/images/jedlicska_dalma_collection -3.webp",
                "DUMMY THINGHY",
            )
        ],
    ),
]


def _filter_product(product_query: ProductQuery, product: Product) -> bool:
    return all(
        [
            product.model.category == product_query.model
            if product_query.model
            else True,
            product.color == product_query.color if product_query.color else True,
        ]
    )


async def get_products(product_query: ProductQuery) -> Iterable[Product]:
    return [p for p in _products if _filter_product(product_query, p)]


async def get_gap_images(_: ProductQuery) -> Iterable[ImageData]:
    return [
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "foobar",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "foobar",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "foobar",
        ),
    ]
