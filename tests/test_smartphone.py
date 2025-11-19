"""Тесты для класса Smartphone."""

from src.smartphone import Smartphone


class TestSmartphone:
    """Тесты Smartphone."""

    def test_smartphone_creation(self):
        """Тест создания смартфона."""
        phone = Smartphone(
            name="iPhone",
            description="Смартфон",
            price=1000,
            quantity=5,
            efficiency="Высокая",
            model="15 Pro",
            memory=256,
            color="Black",
        )

        assert phone.name == "iPhone"
        assert phone.price == 1000
        assert phone.efficiency == "Высокая"
        assert phone.memory == 256
