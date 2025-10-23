import pytest

from category import Category
from product import Product


class TestCategory:
    """Тесты для класса Category"""

    # Фикстура - подготовка данных для тестов
    @pytest.fixture
    def sample_products(self):
        """Создаем тестовые товары"""
        return [Product("Телефон", "Смартфон", 500.0, 10), Product("Ноутбук", "Игровой", 1500.0, 5)]

    def test_category_creation(self, sample_products):
        """Проверяем создание категории"""
        category = Category("Электроника", "Техника", sample_products)

        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert len(category.products) == 2

    def test_category_count(self, sample_products):
        """Проверяем подсчет категорий"""
        # Сбрасываем счетчик перед тестом
        Category.category_count = 0

        category1 = Category("Электроника", "Техника", sample_products)
        category2 = Category("Одежда", "Модная одежда", [])

        assert Category.category_count == 2

    def test_product_count(self, sample_products):
        """Проверяем подсчет товаров"""
        # Сбрасываем счетчик перед тестом
        Category.category_count = 0
        Category.product_count = 0

        category = Category("Электроника", "Техника", sample_products)

        assert Category.product_count == 2
        assert len(category.products) == 2
