"""Модуль категорий для интернет-магазина."""

from product import Product


class Category:
    """Представляет категорию товаров."""

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует категорию с названием, описанием и списком товаров."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
