"""Модуль заказов для интернет-магазина."""

from zero_quantity_error import ZeroQuantityError

from .product import Product
from .purchase import Purchase


class Order(Purchase):
    """Представляет заказ в магазине."""

    def __init__(self, product: Product, quantity: int):
        """Инициализирует заказ."""
        if not isinstance(product, Product):
            raise TypeError("Заказ может содержать только продукты")
        try:
            if quantity <= 0:
                raise ZeroQuantityError(
                    f"Нельзя создать заказ с количеством {quantity}. " "Количество должно быть > 0"
                )
            self.product = product
            self.quantity = quantity

        except ZeroQuantityError as e:
            print(f"Ошибка при создании заказа: {e}")
            raise

        else:
            print(f"Заказ на товар '{product.name}' создан успешно")

        finally:
            print("Обработка создания заказа завершена")

    def get_total_quantity(self):
        """Возвращает итоговую стоимость товаров."""
        return self.quantity

    def get_total_price(self):
        """Возвращает количество купленного товара."""
        return self.product.price * self.quantity
