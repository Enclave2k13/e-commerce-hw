"""Абстрактный модуль для покупок."""

from abc import ABC, abstractmethod


class Purchase(ABC):
    """Абстрактный класс для сущностей, связанных с покупкой товаров."""

    @abstractmethod
    def get_total_price(self) -> float:
        """Получить общую стоимость."""
        pass

    @abstractmethod
    def get_total_quantity(self) -> int:
        """Получить общее количество."""
        pass
