import pytest

from product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Проверяем, что товар создается с правильными атрибутами"""
        product = Product("Телефон", "Смартфон", 500.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 500.0
        assert product.quantity == 10

    def test_product_default_values(self):
        """Проверяем разные значения товара"""
        product = Product("Ноутбук", "Игровой", 1500.99, 1)

        assert product.name == "Ноутбук"
        assert product.price == 1500.99
        assert product.quantity == 1
