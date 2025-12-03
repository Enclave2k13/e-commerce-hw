"""Тесты для пользовательского исключения ZeroQuantityError."""

from src.zero_quantity_error import ZeroQuantityError


def test_zero_quantity_error_creation():
    """Тест создания исключения с сообщением по умолчанию."""
    error = ZeroQuantityError()
    assert str(error) == "Товар с нулевым количеством не может быть добавлен"
    assert isinstance(error, ValueError)


def test_zero_quantity_error_custom_message():
    """Тест создания исключения с пользовательским сообщением."""
    custom_message = "Товар не может иметь нулевое количество"
    error = ZeroQuantityError(custom_message)
    assert str(error) == custom_message
