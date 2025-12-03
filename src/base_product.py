"""Абстрактный базовый класс для товаров."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов."""

    def __init__(self, *args, **kwargs):
        """Просто чтобы цепочка super() работала."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление товара."""
        pass
