"""Модуль для тестирования категорий товара."""

import pytest

from category import Category
from product import Product


class TestCategory:
    """Тесты для класса Category."""

    # Фикстура - подготовка данных для тестов
    @pytest.fixture
    def sample_products(self):
        """Создаем тестовые товары."""
        return [Product("Телефон", "Смартфон", 500.0, 10), Product("Ноутбук", "Игровой", 1500.0, 5)]

    def test_category_creation(self, sample_products):
        """Проверяем создание категории."""
        category = Category("Электроника", "Техника", sample_products)

        assert category.name == "Электроника"
        assert category.description == "Техника"
        # Вместо len(category.products) проверяем содержимое строки
        assert "Телефон, 500.0 руб. Остаток: 10 шт." in category.products
        assert "Ноутбук, 1500.0 руб. Остаток: 5 шт." in category.products

    def test_category_count(self, sample_products):
        """Проверяем подсчет категорий."""
        # Сбрасываем счетчик перед тестом
        Category.category_count = 0

        category1 = Category("Электроника", "Техника", sample_products)
        category2 = Category("Одежда", "Модная одежда", [])

        assert Category.category_count == 2
        assert category1.name == "Электроника"
        assert category2.name == "Одежда"

    def test_product_count(self, sample_products):
        """Проверяем подсчет товаров."""
        Category.category_count = 0
        Category.product_count = 0

        Category("Электроника", "Техника", sample_products)

        assert Category.product_count == 2

    def test_private_products_access(self):
        """Тест приватности атрибута продуктов."""
        product = Product("Телефон", "Смартфон", 500, 10)
        category = Category("Электроника", "Техника", [product])

        # Нельзя обратиться напрямую к __products
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_products_getter_format(self):
        """Тест формата вывода геттера продуктов."""
        product1 = Product("Телефон", "Смартфон", 500, 10)
        product2 = Product("Ноутбук", "Игровой", 1000, 5)
        category = Category("Электроника", "Техника", [product1, product2])

        products_str = category.products
        assert "Телефон, 500 руб. Остаток: 10 шт." in products_str
        assert "Ноутбук, 1000 руб. Остаток: 5 шт." in products_str

    def test_add_product_method(self):
        """Тест метода add_product."""
        category = Category("Электроника", "Техника", [])
        product = Product("Телефон", "Смартфон", 500, 10)

        initial_count = Category.product_count
        category.add_product(product)

        assert "Телефон, 500 руб. Остаток: 10 шт." in category.products
        assert Category.product_count == initial_count + 1

    def test_category_str_representation(self, sample_products):
        """Тест строкового представления Category."""
        category = Category("Электроника", "Техника", sample_products)

        # Проверяем что выводится название и общее количество
        result = str(category)
        assert "Электроника" in result
        assert "количество продуктов: 15 шт." in result  # 10 + 5

    def test_get_products_method(self, sample_products):
        """Тест метода get_products."""
        category = Category("Электроника", "Техника", sample_products)

        products_list = category.get_products()
        assert len(products_list) == 2
        assert isinstance(products_list, list)
