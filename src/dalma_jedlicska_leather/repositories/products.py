from typing import Iterable, Protocol
from dalma_jedlicska_leather.domain.locale import Locale, Price
from dalma_jedlicska_leather.domain.images import ImageData
from dalma_jedlicska_leather.domain.product import Model, Product

_kleio_bp_model = Model(
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
        )

_kleio_sd_model = Model(
    name="kleio",
    description="""A KLEIO kis oldaltáska erős kontúrja a finom, íves vonalvezetéssel ad nőies határozottságot.

Belsejében egy lapos kis zseb található. Elejét teljesen elfedő fedele mágnessel záródik. Állítható hosszúságú vállpánttal rendelkezik, így vállon, illetve testen átvetve is viselhető hétköznapokon és alkalmakon egyaránt.
    """,
    details="""Egy lapos kis belső zseb
Levehető, állítható hosszúságú vállpánt
Fedeles, mágneses záródás
Vágott festett széleldolgozás

Méretek
MA 24 x SZ 16 x MÉ 7cm
Állítható hosszúságú vállpánt""",
    category="oldaltáska",
    prices=[Price(Locale.HU, 70000)]
)

_kleio_bsd_model = Model(
    name="kleio",
    description="""A KLEIO kis válltáska továbbgondolásaként született a nagyobb, több rekesszel rendelkező KLEIO közepes válltáska.

Geometrikus kompozícióját a vonalak egyidejű össze- és széttartása jellemzi. A KLEIO közepes válltáskát markánssáng és funkcionalitás jellemzi, minden hétköznapi igénynek helyet adva. 
Belsejében két főrekeszt egy kisebb, cipzáras zseb választ el. Fedele mágneszárral rögzül. Állítható vállpántja segítségével vállon és testen átvetve is viselhetó. Fedele mágnessel záródik""",
    details="""Két belső főrekesz
Egy zipzáras, lapos belső zseb
Állítható hosszúságú vállpánt
Fedeles, mágneses záródás
Vágott festett széleldolgozás

Méretek
MA 22 x SZ 24-28 x MÉ 10 cm
Állítható hosszúságú vállpánt""",
    category="oldaltáska",
    prices=[Price(Locale.HU, 100000)]
)

_ava_xb_model = Model(
    name="ava",
    description="""Az AVA crossbody egyediségét a hajlítás által alakított forma és két oldalsó „szárnyacskája” adja, amelyek a pántokat fogadják magukba. 

Kivételesen kényelmes mind a háton, mind elöl viselve, a felsőtestet követő és körbeölelő kialakításának köszönhetően. Mindemelett a hátulján elhelyezett cipzáras záródásának köszönhetően teljes biztonságban tudhatjuk értékeinket.
""",
    details="""Belső fő rekesz
Egy lapos belső zseb
Egy lapos külső zseb
Állítható hosszúságú vállpánt
Fém cipzáras záródás
Vágott festett széleldolgozás

Méretek
MA 19 x SZ 25-50 x MÉ 10 cm
Állítható hosszúságú keresztpánt 
""",
    category="crossbody",
    prices=[Price(Locale.HU, 80000)]
)

_ava_shd_model = Model(
    name="ava",
    description="""A visszafogott luxus koncepciójához hűen az AVA válltáska elegáns, mégis nyugodt kialakítását a letisztultság és a funkcionalitás jellemzi.

Egy minimalista válltáska minden hétköznapi szükséglethez, rengeteg helyet kínál a nélkülözhetetlen dolgoknak. Belső óriási főrekesze mellett egy lapos belső és egy cipzáras belső zseb található.
""",
    details="""Belső nagy fő rekesz
Egy lapos belső zseb
Egy lapos belső zseb cipzáras záródással
Fém cipzáras záródás
Vágott festett széleldolgozás

Méretek
MA 25 x SZ 36 x MÉ 16 cm
71 cm hosszú vállpánt
""",
    category="válltáska",
    prices=[Price(Locale.HU, 100000)]
)

_ava_clt_model = Model(
    name="ava",
    description="""Az AVA váll- ás borítéktáska egyszerre kínál finom eleganciát és ..oldott.. stílust.

Állítható és levehető vállpántjával az AVA borítéktáska ideális társ nemcsak a kézben, hanem a vállon vagy testen átvetve is, akár nappal, akár éjszaka.
Cipzárral nyitható
""",
    details="""Belső fő rekesz
Egy lapos belső zseb
Négy kártyatartó rekesz
Állítható hosszúságú, lecsatolható vállpánt
Fém cipzáras záródás
Vágott festett széleldolgozás

Méretek
MA 14 x SZ 32 x MÉ 6 cm
Állítható hosszúságú váll- vagy keresztpánt 
""",
    category="clutch",
    prices=[Price(Locale.HU, 50000)]
)

_bear_model = Model(
    name="bear",
    description="""Maci taska loerm 
""",
    details="""
""",
    category="hátitáska",
    prices=[Price(Locale.HU, 40000)]
)

class ProductQuery(Protocol):
    model: str | None
    color: str | None


_products = [
    Product(
        "kleio-bp-brown-01",
        model=_kleio_bp_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/dj_webshop-2.webp",
            "kleio barna hátizsák",
        ),
        material_description="""100% marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/dj_webshop-1.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-3.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-4.webp",
                "kleio barna hátizsák",
            ),
            ImageData(
                "/static/images/dj_webshop-5.webp",
                "kleio barna hátizsák",
            ),
        ],
    ),
    Product(
        "kleio-bp-purple-01",
        model=_kleio_bp_model,
        color="padlizsán",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-7.jpg",
            "kleio padlizsán hátizsák",
        ),
        material_description="""100% marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-6.jpg",
                "kleio padlizsán hátizsák",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-8.jpg",
                "kleio padlizsán hátizsák",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-9.jpg",
                "kleio padlizsán hátizsák",
            ),
        ],
    ),
    Product(
        "kleio-bp-veg-01",
        model=_kleio_bp_model,
        color="natúr",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-12.jpg",
            "kleio növényi cserzésű hátizsák",
        ),
        material_description="""100% növényi cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-10.jpg",
                "kleio padlizsán hátizsák",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-11.jpg",
                "kleio padlizsán hátizsák",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-13.jpg",
                "kleio padlizsán hátizsák",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-15.jpg",
                "kleio padlizsán hátizsák",
            ),
        ],
    ),
    Product(
        "kleio-sd-black-brown-01",
        model=_kleio_sd_model,
        color="fekete és barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-17.jpg",
            "kleio fekete barna oldaltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-18.jpg",
                "kleio fekete barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-19.jpg",
                "kleio fekete barna oldaltáska",
            ),
        ],
    ),
    Product(
        "kleio-sd-brown-01",
        model=_kleio_sd_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-21.jpg",
            "kleio barna oldaltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-20.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-22.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-23.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-24.jpg",
                "kleio barna oldaltáska",
            ),
        ],
    ),
    Product(
        "kleio-sd-brown-02",
        model=_kleio_sd_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-25.jpg",
            "kleio barna oldaltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-26.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-27.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-28.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-29.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-30.jpg",
                "kleio barna oldaltáska",
            ),
        ],
    ),
    Product(
        "kleio-sd-mauve-02",
        model=_kleio_sd_model,
        color="mályva",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-38.jpg",
            "kleio mályva oldaltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-39.jpg",
                "kleio mályva oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-40.jpg",
                "kleio mályva oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-41.jpg",
                "kleio mályva oldaltáska",
            ),
        ],
    ),
    Product(
        "kleio-bsd-brown-01",
        model=_kleio_bsd_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-31.jpg",
            "kleio barna oldaltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-32.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-33.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-34.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-35.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-36.jpg",
                "kleio barna oldaltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-37.jpg",
                "kleio barna oldaltáska",
            ),
        ],
    ),
    Product(
        "ava-xbd-brown-01",
        model=_ava_xb_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-76.jpg",
            "ava barna crossbody",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek
        """,
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-77.jpg",
                "ava barna crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-78.jpg",
                "ava barna crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-79.jpg",
                "ava barna crossbody",
            ),
        ],
    ),
    Product(
        "ava-xbd-veg-01",
        model=_ava_xb_model,
        color="natúr",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-80.jpg",
            "ava natúr crossbody",
        ),
        material_description="""100% növényi cserzésű marhabőr bélés nélkül
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-81.jpg",
                "ava natúr crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-82.jpg",
                "ava natúr crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-83.jpg",
                "ava natúr crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-83.jpg",
                "ava natúr crossbody",
            ),
        ],
    ),
    Product(
        "ava-xbd-black-01",
        model=_ava_xb_model,
        color="fekete",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-85.jpg",
            "ava fekete crossbody",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-86.jpg",
                "ava fekete crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-87.jpg",
                "ava fekete crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-88.jpg",
                "ava fekete crossbody",
            ),
        ],
    ),
    Product(
        "ava-xbd-green-01",
        model=_ava_xb_model,
        color="zöld",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-89.jpg",
            "ava zöld crossbody",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-90.jpg",
                "ava zöld crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-91.jpg",
                "ava zöld crossbody",
            ),
        ],
    ),
    Product(
        "ava-xbd-aub-01",
        model=_ava_xb_model,
        color="padilizsán",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-93.jpg",
            "ava padlizsán crossbody",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-92.jpg",
                "ava padlizsán crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-94.jpg",
                "ava padlizsán crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-94.jpg",
                "ava padlizsán crossbody",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-95.jpg",
                "ava padlizsán crossbody",
            ),
        ],
    ),
    Product(
        "ava-shd-green-01",
        model=_ava_shd_model,
        color="zöld",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-53.jpg",
            "ava zöld válltáska",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-51.jpg",
                "ava zöld válltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-52.jpg",
                "ava zöld válltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-68.jpg",
                "ava zöld válltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-69.jpg",
                "ava zöld válltáska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-70.jpg",
                "ava zöld válltáska",
            ),
        ],
    ),
    Product(
        "ava-clt-rose-01",
        model=_ava_clt_model,
        color="pasztell rózsaszín",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-71.jpg",
            "ava pasztell rózsaszín clutch",
        ),
        material_description="""100% króm cserzésű marhabőr
100% sertésbőr bélés teljes felületen kasírozva
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-72.jpg",
                "ava pasztell rózsaszín clutch",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-73.jpg",
                "ava pasztell rózsaszín clutch",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-74.jpg",
                "ava pasztell rózsaszín clutch",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-75.jpg",
                "ava pasztell rózsaszín clutch",
            ),
        ],
    ),
    Product(
        "bear-brown-01",
        model=_bear_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-44.jpg",
            "maci taska",
        ),
        material_description="""100% króm cserzésű marhabőr
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-43.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-45.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-42.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-46.jpg",
                "maci taska",
            ),
        ],
    ),
    Product(
        "bear-brown-01",
        model=_bear_model,
        color="barna",
        cover_image=ImageData(
            "/static/images/jpg/dj_webshop-47.jpg",
            "maci taska",
        ),
        material_description="""100% króm cserzésű marhabőr
Nikkelezett fémkellékek""",
        display_images=[
            ImageData(
                "/static/images/jpg/dj_webshop-48.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-49.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-42.jpg",
                "maci taska",
            ),
            ImageData(
                "/static/images/jpg/dj_webshop-50.jpg",
                "maci taska",
            ),
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
            "foobar",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "foobar",
        ),
        ImageData(
            "/static/images/jedlicska_dalma_film_look_porcelain-51.webp",
            "foobar",
        ),
    ]
