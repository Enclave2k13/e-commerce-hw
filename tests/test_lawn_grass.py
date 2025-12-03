"""Тесты для класса LawnGrass."""

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product


class TestLawnGrass:
    """Тесты LawnGrass."""

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы."""
        grass = LawnGrass(
            name="Газонная трава Премиум",
            description="Мягкая газонная трава",
            price=15.50,
            quantity=100,
            country="Россия",
            germination_period=14,
            color="Зеленый",
        )

        assert grass.name == "Газонная трава Премиум"
        assert grass.price == 15.50
        assert grass.quantity == 100
        assert grass.country == "Россия"
        assert grass.germination_period == 14
        assert grass.color == "Зеленый"

    def test_lawn_grass_str_representation(self):
        """Тест строкового представления LawnGrass."""
        grass = LawnGrass("Трава", "Описание", 20, 50, "Россия", 10, "Зеленый")

        result = str(grass)
        assert "Трава, 20 руб. Остаток: 50 шт." in result

    def test_lawn_grass_addition(self):
        """Тест сложения газонной травы."""
        grass1 = LawnGrass("Трава1", "Описание", 10, 100, "Россия", 14, "Зеленый")
        grass2 = LawnGrass("Трава2", "Описание", 15, 50, "Беларусь", 10, "Темно-зеленый")

        total = grass1 + grass2
        assert total == 1750

    def test_lawn_grass_addition_different_types(self):
        """Тест ошибки при сложении с другими типами."""
        grass = LawnGrass("Трава", "Описание", 10, 100, "Россия", 14, "Зеленый")
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(TypeError):
            grass + product
