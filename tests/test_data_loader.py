"""Тесты для модуля data_loader."""

import json
import os
import tempfile

import pytest

from src.data_loader import load_data_from_json


class TestDataLoader:
    """Тесты для загрузки данных из JSON."""

    def test_load_data_success(self):
        """Тест успешной загрузки данных."""
        # Создаем тестовые данные
        test_data = {
            "categories": [
                {
                    "name": "Electronics",
                    "description": "Tech gadgets",
                    "products": [{"name": "Phone", "description": "Smartphone", "price": 500.0, "quantity": 10}],
                }
            ]
        }

        # Создаем временный файл
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False)
            file_path = f.name

        try:
            # Тестируем загрузку
            categories = load_data_from_json(file_path)

            # Проверяем результат
            assert len(categories) == 1
            assert categories[0].name == "Electronics"
            # Вместо len() проверяем содержимое строки
            assert "Phone, 500.0 руб. Остаток: 10 шт." in categories[0].products

        finally:
            # Удаляем временный файл
            if os.path.exists(file_path):
                os.unlink(file_path)

    def test_load_data_file_not_found(self):
        """Тест обработки отсутствующего файла."""
        with pytest.raises(FileNotFoundError):
            load_data_from_json("nonexistent_file.json")
