"""Миксины для расширения функциональности классов."""


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __repr__(self):
        """Возвращает строковое представление как в примере задания."""
        if hasattr(super(), "__repr__"):
            return super().__repr__()
        return object.__repr__(self)

    def __init__(self, *args, **kwargs):
        """Инициализация с логированием создания объекта."""
        super().__init__(*args, **kwargs)
        print(f"Создан: {repr(self)}")
