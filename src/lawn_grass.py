"""Модуль газонной травы."""

from .product import Product


class LawnGrass(Product):
    """Представляет газонною траву в магазине."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
