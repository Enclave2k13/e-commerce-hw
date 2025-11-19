"""Модуль категорий для интернет-магазина."""

from product import Product


class Category:
    """Представляет категорию товаров."""

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализирует категорию с названием, описанием и списком товаров."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Форматированный вывод категорий и количества продуктов в ней."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для вывода информации о товарах."""
        return "\n".join(str(product) for product in self.__products)

    def get_products(self):
        """Возвращает список товаров категории."""
        return self.__products
