"""Тесты для CategoryIterator."""

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


class TestCategoryIterator:
    """Тесты итератора категорий."""

    def test_iterator_basic_functionality(self):
        """Тест базовой функциональности итератора."""
        product1 = Product("Телефон", "Смартфон", 500, 10)
        product2 = Product("Ноутбук", "Игровой", 1000, 5)
        category = Category("Электроника", "Техника", [product1, product2])

        iterator = CategoryIterator(category)

        # Проверяем что итератор возвращает все товары
        products = list(iterator)
        assert len(products) == 2
        assert products[0] == product1
        assert products[1] == product2

    def test_empty_category_iterator(self):
        """Тест итератора для пустой категории."""
        category = Category("Пустая", "Нет товаров", [])

        iterator = CategoryIterator(category)

        # Должен вернуть пустой список
        products = list(iterator)
        assert len(products) == 0

    def test_multiple_iterations(self):
        """Тест нескольких итераций по одной категории."""
        product = Product("Телефон", "Смартфон", 500, 10)
        category = Category("Электроника", "Техника", [product])

        # Первая итерация
        products1 = list(CategoryIterator(category))

        # Вторая итерация (должна работать независимо)
        products2 = list(CategoryIterator(category))

        assert products1 == products2
        assert len(products1) == 1
