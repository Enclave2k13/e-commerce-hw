"""Тесты для абстрактного класса Purchase."""

import pytest

from src.category import Category
from src.product import Product
from src.purchase import Purchase


class TestPurchase:
    """Тесты Purchase."""

    def test_purchase_interface(self):
        """Тест что Purchase действительно абстрактный."""
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            Purchase()  # нельзя создать экземпляр абстрактного класса

    def test_category_implements_purchase(self):
        """Тест что Category реализует Purchase интерфейс."""
        product = Product("Телефон", "Смартфон", 500, 10)
        category = Category("Электроника", "Техника", [product])

        # Проверяем что Category имеет методы Purchase
        assert hasattr(category, "get_total_quantity")
        assert hasattr(category, "get_total_price")

        # Проверяем что методы работают
        assert category.get_total_quantity() == 10
        assert category.get_total_price() == 5000  # 500 * 10
