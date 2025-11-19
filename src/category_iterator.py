"""Модуль для итерации продуктов внутри категории."""


class CategoryIterator:
    """Представляет итератор продуктов внутри категории."""

    def __init__(self, category):
        """Инициализирует итератор."""
        self.products = category.get_products()
        self.index = 0

    def __iter__(self):
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующий продукт в категории."""
        if self.index < len(self.products):
            item = self.products[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
