"""Модуль товаров для интернет-магазина."""


class Product:
    """Представляет товар в магазине."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует товар с названием, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
