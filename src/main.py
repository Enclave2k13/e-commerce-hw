"""Главный модуль приложения интернет-магазина."""

import os

from .category import Category
from .data_loader import load_data_from_json


def main():
    """Основная функция для тестирования загрузки данных из json."""
    print("🚀 Тестируем загрузку данных из JSON...\n")

    try:
        # Получаем абсолютный путь к products.json
        current_dir = os.path.dirname(__file__)
        project_root = os.path.dirname(current_dir)  # поднимаемся на уровень выше
        json_path = os.path.join(project_root, "products.json")

        # Загружаем данные
        categories = load_data_from_json(json_path)

        # Выводим результат
        print(f"✅ Успешно загружено категорий: {len(categories)}")
        print(f"📊 Всего категорий в системе: {Category.category_count}")
        print(f"📦 Всего товаров в системе: {Category.product_count}")
        print("\n" + "=" * 50 + "\n")

        # Детальная информация по каждой категории
        for i, category in enumerate(categories, 1):
            print(f"🏷️  Категория {i}: {category.name}")
            print(f"📝 Описание: {category.description}")
            print(f"🛍️  Товаров в категории: {len(category.products)}")

            for j, product in enumerate(category.products, 1):
                print(f"   {j}. {product.name}")
                print(f"      💰 Цена: {product.price} руб.")
                print(f"      📦 В наличии: {product.quantity} шт.")
                print(f"      📋 Описание: {product.description}")
            print("-" * 30)

    except FileNotFoundError:
        print("❌ Ошибка: Файл products.json не найден!")
    except Exception as e:
        print(f"❌ Ошибка при загрузке данных: {e}")


if __name__ == "__main__":
    main()
