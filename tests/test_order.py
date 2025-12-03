"""Тесты для класса Order."""

import pytest

from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


class TestOrder:
    """Тесты Order."""

    def test_order_creation(self):
        """Тест создания заказа."""
        product = Product("Телефон", "Смартфон", 500, 10)
        order = Order(product, 2)

        assert order.product == product
        assert order.quantity == 2
        assert order.get_total_price() == 1000  # 500 * 2

    def test_order_with_smartphone(self):
        """Тест заказа смартфона."""
        smartphone = Smartphone("iPhone", "Смартфон", 1000, 5, "Высокая", "15", 256, "Black")
        order = Order(smartphone, 1)

        assert order.get_total_price() == 1000
        assert isinstance(order.product, Smartphone)

    def test_order_invalid_quantity(self):
        """Тест заказа с невалидным количеством."""
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(ValueError, match="Количество должно быть > 0"):
            Order(product, 0)

        with pytest.raises(ValueError, match="Количество должно быть > 0"):
            Order(product, -5)
