"""Модуль товаров для интернет-магазина."""


class Product:
    """Представляет товар в магазине."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует товар с названием, описанием, ценой и количеством."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Геттер."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер с проверками"""
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")

        if new_price < self.__price:
            answer = input("Вы уверены? (y/n)")
            if answer.lower() != "y":
                print("Отмена")
                return
        self.__price = new_price

    @staticmethod
    def _merge_product_data(existing_obj, new_data: dict) -> dict:
        """Объединяет данные существующего товара с новыми данными."""
        return {
            "name": existing_obj.name,
            "description": new_data.get("description", existing_obj.description),
            "price": max(existing_obj.price, new_data["price"]),
            "quantity": existing_obj.quantity + new_data["quantity"],
        }

    @classmethod
    def _create_product(cls, product_data: dict):
        """Базовое создание товара."""
        required_fields = ["name", "description", "price", "quantity"]

        for field in required_fields:
            if field not in product_data:
                raise ValueError(f"Отсутствует поле: {field}")

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """Создает товар с проверкой дубликатов."""
        for existing in existing_products or []:
            if existing.name == product_data["name"]:
                # Трансформируем → Создаём
                merged_data = cls._merge_product_data(existing, product_data)
                return cls._create_product(merged_data)

        return cls._create_product(product_data)
