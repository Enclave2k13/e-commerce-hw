"""Модуль для тестирования продукта."""

import pytest

from product import Product


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

        with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
            product + "не продукт"
