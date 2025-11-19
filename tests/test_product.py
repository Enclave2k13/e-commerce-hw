"""Модуль для тестирования продукта."""

import pytest

from lawn_grass import LawnGrass
from product import Product
from smartphone import Smartphone


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self):
        """Проверяем, что товар создается с правильными атрибутами."""
        product = Product("Телефон", "Смартфон", 500.0, 10)

        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 500.0
        assert product.quantity == 10

    def test_product_default_values(self):
        """Проверяем разные значения товара."""
        product = Product("Ноутбук", "Игровой", 1500.99, 1)

        assert product.name == "Ноутбук"
        assert product.price == 1500.99
        assert product.quantity == 1

    def test_private_price_access(self):
        """Тест приватности атрибута цены."""
        product = Product("Телефон", "Смартфон", 500, 10)

        # Нельзя обратиться напрямую к __price
        with pytest.raises(AttributeError):
            _ = product.__price

    def test_price_getter(self):
        """Тест геттера цены."""
        product = Product("Телефон", "Смартфон", 500, 10)
        assert product.price == 500

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением."""
        product = Product("Телефон", "Смартфон", 500, 10)
        product.price = 600
        assert product.price == 600

    def test_price_setter_negative(self):
        """Тест сеттера цены с отрицательным значением."""
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
            product.price = -100

    def test_price_setter_zero(self):
        """Тест сеттера цены с нулевым значением."""
        product = Product("Телефон", "Смартфон", 500, 10)

        with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
            product.price = 0

    def test_new_product_from_dict(self):
        """Тест создания товара из словаря."""
        data = {"name": "Телефон", "description": "Смартфон", "price": 500.0, "quantity": 10}

        product = Product.new_product(data)

        assert product.name == "Телефон"
        assert product.price == 500.0
        assert product.quantity == 10

    def test_new_product_duplicate_merge(self):
        """Тест объединения дубликатов с созданием нового объекта."""
        existing_product = Product("Телефон", "Старый", 500, 10)
        products_list = [existing_product]

        new_data = {"name": "Телефон", "description": "Новый", "price": 600.0, "quantity": 5}

        result = Product.new_product(new_data, products_list)

        assert result is not existing_product
        assert result.name == "Телефон"
        assert result.quantity == 15
        assert result.price == 600.0
        assert result.description == "Новый"

    def test_product_str_representation(self):
        """Тест строкового представления Product."""
        product = Product("Телефон", "Смартфон", 500, 10)
        expected = "Телефон, 500 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_addition(self):
        """Тест сложения продуктов."""
        product1 = Product("Телефон", "Смартфон", 100, 10)
        product2 = Product("Ноутбук", "Игровой", 200, 2)

        total_value = product1 + product2
        assert total_value == 1400  # 100*10 + 200*2

    def test_product_addition_type_error(self):
        """Тест ошибки при сложении с неправильным типом."""
        product = Product("Телефон", "Смартфон", 100, 10)

        with pytest.raises(TypeError):
            product + "не продукт"

    def test_product_addition_same_types(self):
        """Тест сложения одинаковых типов продуктов."""
        smartphone1 = Smartphone("iPhone", "Смартфон", 100, 10, "Высокая", "15", 256, "Black")
        smartphone2 = Smartphone("Samsung", "Смартфон", 200, 2, "Средняя", "S20", 128, "White")

        total = smartphone1 + smartphone2
        assert total == 1400

    def test_product_addition_different_types(self):
        """Тест ошибки при сложении разных типов продуктов."""
        smartphone = Smartphone("iPhone", "Смартфон", 100, 10, "Высокая", "15", 256, "Black")
        grass = LawnGrass("Трава", "Газонная", 15, 100, "Россия", 14, "Зеленый")

        with pytest.raises(TypeError):
            smartphone + grass

        with pytest.raises(TypeError):
            grass + smartphone

    def test_product_addition_inheritance_works(self):
        """Тест на проверку, что наследование не ломает сложение."""
        # Обычные продукты
        product1 = Product("Товар1", "Описание", 50, 20)
        product2 = Product("Товар2", "Описание", 30, 10)

        total = product1 + product2
        assert total == 1300
