"""Загрузчик JSON данных для интернет-магазина."""

import json

from category import Category
from product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Загружает данные о категориях и товарах из JSON файла."""
    categories = []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        for category_data in data["categories"]:
            products = []
            for product_data in category_data["products"]:
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)

            category = Category(
                name=category_data["name"], description=category_data["description"], products=products
            )
            categories.append(category)

    return categories
