from typing import Iterable, Protocol
from dalma_jedlicska_leather.domain.locale import Locale, Price
from dalma_jedlicska_leather.domain.images import ImageData
from dalma_jedlicska_leather.domain.product import Model, Product


class ProductQuery(Protocol):
    model: str | None
    color: str | None


_products = [
    Product(
        "kleio-bp-brown-01",
        model=Model(
            name="kleio",
            details="""Egy lapos kis belső zseb
Egy kis cipzáras külső zseb
Kézi fogó
Állítható vállpánt
Fémcipzáras záródás
Vágott festett széleldolgozás

Méretek
MA 33 x SZ 25 x MÉ 11cm
Állítható hosszúságú vállpánt""",
            description="""A KLEIO közepes méretű hátitáska geometriai sziluettje izgalmas kontrasztot alkot a lágy ívekkel.
A hosszan futó cipzáras záródás megkönnyíti a belső tér használatát, míg a bőrbetétek biztosítják, hogy a táska szélesen kinyíljon, miközben minden érték biztonságban marad.

Válogatott olasz marhabőrből készül, belseje teljes felületen sertés bőrrel kasírozott. A nagy főrekeszen kívül egy belső lapos kis zsebbel és egy külső kis cipzáras zsebbel rendelkezik. Záródása fémcipzárral biztosított. Vállpántja állítható hosszúságú.""",
            category="hátitáska",
            prices=[Price(Locale.HU, 110000)],
        ),
        color="barna",
        cover_image=ImageData(
            "/static/images/dj_webshop-2.webp",
            "/static/images/dj_webshop-2_blur.webp",
            "kleio barna hátizsák",
        ),
        material_description="""100% marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/dj_webshop-1.webp",
                "/static/images/dj_webshop-1_blur.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-3.webp",
                "/static/images/dj_webshop-3_blur.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-4.webp",
                "/static/images/dj_webshop-4_blur.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-5.webp",
                "/static/images/dj_webshop-5_blur.webp",
                "kleio barna hátizsák",
            ),
        ],
    ),
    Product(
        id="foo1",
        model=Model(
            name="capacitor",
            category="crossbody",
            details="asdfasdf",
            description="asdfasdfasdf",
            prices=[Price(Locale.HU, 90000)],
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
        model=Model(
            "akela", "crossbody", [Price(Locale.HU, 90000)], "asdfasdfasa", "asdfasdf"
        ),
        cover_image=ImageData(
            "/static/images/jedlicska_dalma_collection -3.webp",
            "/static/images/jedlicska_dalma_collection -3.webp",
            "DUMMY THINGHY",
        ),
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
