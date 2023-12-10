from typing import Awaitable, Iterable, List, Sequence, Callable

from attrs import define
from dalma_jedlicska_leather.domain.locale import Locale, Price
from dalma_jedlicska_leather.domain.images import ImageData
from dalma_jedlicska_leather.domain.product import Product


@define
class ProductQuery:
    cursor: str | None = None
    model: str | None = None
    color: str | None = None


@define
class ProductDisplayInformation:
    price: Price
    product_data: Product
    display_images: Sequence[ImageData]


@define
class PaginatedProductDisplayInformation:
    items: Sequence[ProductDisplayInformation | ImageData]
    cursor: str | None


@define
class ProductHandler:
    _product_getter: Callable[[ProductQuery], Awaitable[Iterable[Product]]]
    _gap_image_getter: Callable[[ProductQuery], Awaitable[Iterable[ImageData]]]

    async def get_paginated_translated_products_with_gap_images(
        self, product_query: ProductQuery, locale: Locale, frequency=3
    ) -> PaginatedProductDisplayInformation:
        product_or_gap_images = []
        gap_images = (i for i in await self._gap_image_getter(product_query))
        matching_products = 0
        for product in await self._product_getter(product_query):
            # every 3rd image, not including 0
            if matching_products and matching_products % frequency == 0:
                gap_image = next(gap_images, None)
                if gap_image:
                    product_or_gap_images.append(gap_image)

            if price := next(
                (p for p in product.model.prices if p.locale == locale), None
            ):
                matching_products += 1
                product_or_gap_images.append(
                    ProductDisplayInformation(price, product, product.display_images)
                )
        return PaginatedProductDisplayInformation(product_or_gap_images, cursor=None)

    async def get_all_model_categories(self) -> List[str]:
        products = await self._product_getter(ProductQuery())
        return list(set(p.model.category for p in products))

    async def get_product_by_id(self, product_id: str) -> Product | None:
        return next(
            (
                p
                for p in await self._product_getter(ProductQuery())
                if p.id == product_id
            ),
            None,
        )

    async def get_related_products(self, _: str) -> List[Product]:
        related_products = []
        max_products = 4
        for i, product in enumerate(await self._product_getter(ProductQuery())):
            if i == max_products:
                break
            related_products.append(product)
        return related_products
