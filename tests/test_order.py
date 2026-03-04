"""Тесты для класса Order."""

import pytest

from src.order import Order
from src.product import Product
from src.smartphone import Smartphone
from zero_quantity_error import ZeroQuantityError


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

    def test_order_cannot_have_zero_quantity(self):
        """Тест: Order нельзя создать с quantity=0."""
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(ZeroQuantityError) as error:
            Order(product, 0)

        assert "Количество должно быть > 0" in str(error.value)

    def test_order_cannot_have_negative_quantity(self):
        """Тест: Order нельзя создать с quantity<0."""
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(ZeroQuantityError) as error:
            Order(product, -5)

        assert "Количество должно быть > 0" in str(error.value)

    def test_order_creation_success(self):
        """Тест: успешное создание Order."""
        product = Product("Телефон", "Смартфон", 500, 10)
        order = Order(product, 3)

        assert order.product == product
        assert order.quantity == 3
        assert order.get_total_price() == 500 * 3
        assert order.get_total_quantity() == 3
