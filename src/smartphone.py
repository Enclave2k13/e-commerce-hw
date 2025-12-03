"""Модуль смартфонов."""

from .product import Product


class Smartphone(Product):
    """Представляет смартфоны в магазине."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
