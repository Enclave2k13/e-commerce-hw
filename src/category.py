"""Модуль категорий для интернет-магазина."""

from zero_quantity_error import ZeroQuantityError

from .product import Product
from .purchase import Purchase


class Category(Purchase):
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
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты и их наследников")

        try:
            if product.quantity == 0:
                raise ZeroQuantityError(f"Товар '{product.name}' имеет нулевое количество")
            self.__products.append(product)
            Category.product_count += 1

        except ZeroQuantityError as e:
            print(f"Ошибка при добавлении товара: {e}")
            raise

        else:
            print(f"Товар '{product.name}' успешно добавлен в категорию '{self.name}'")

        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        """Геттер для вывода информации о товарах."""
        return "\n".join(str(product) for product in self.__products)

    def get_products(self):
        """Возвращает список товаров категории."""
        return self.__products

    def get_total_quantity(self):
        """Возвращает общее количество товаров."""
        return sum(p.quantity for p in self.__products)

    def get_total_price(self):
        """Возвращает общую сумму товаров."""
        return sum(p.price * p.quantity for p in self.__products)

    def average_price(self) -> float:
        """Возвращает среднюю цену товаров в категории."""
        try:
            total_price = self.get_total_price()
            total_quantity = self.get_total_quantity()
            return total_price / total_quantity

        except ZeroDivisionError:
            return 0
