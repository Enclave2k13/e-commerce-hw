"""Enum с emoji-иконками для интернет-магазина."""

from enum import Enum


class Icons(Enum):
    """Список иконок для быстрого использования в приложении."""

    # Категории и товары
    CATEGORY = "🏷️"
    PRODUCT = "📦"
    CART = "🛒"

    # Финансы
    PRICE = "💰"
    SALE = "🤑"
    DISCOUNT = "🎯"

    # Статусы
    SUCCESS = "✅"
    ERROR = "❌"
    WARNING = "⚠️"
    INFO = "ℹ️"

    # Действия
    ADD = "➕"
    REMOVE = "➖"
    EDIT = "✏️"
    DELETE = "🗑️"

    # Навигация
    SEARCH = "🔍"
    FILTER = "🧹"
    SORT = "📊"

    # Состояния
    IN_STOCK = "✅"
    OUT_OF_STOCK = "❌"
    LOW_STOCK = "⚠️"

    # Процессы
    LOADING = "⏳"
    COMPLETED = "🎉"
    START = "🚀"
    SETTINGS = "🔧"

    # Описания
    DESCRIPTION = "📝"
    DETAILS = "📋"
    TAGS = "🏷️"


# Для быстрого доступа
CATEGORY = Icons.CATEGORY.value
PRODUCT = Icons.PRODUCT.value
PRICE = Icons.PRICE.value
SUCCESS = Icons.SUCCESS.value
ERROR = Icons.ERROR.value
WARNING = Icons.WARNING.value
DESCRIPTION = Icons.DESCRIPTION.value
CART = Icons.CART.value
START = Icons.START.value
