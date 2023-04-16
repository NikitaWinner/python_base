from typing import Any
from collections.abc import Hashable

def kwarg_to_dict(**kwargs: Any) -> dict:
    """
    Функция для преобразования ключевых параметров в словарь.

    :param kwargs: Ключевые параметры
    :return: словарь с ключом, равным значению параметра, и значением, равным имени параметра
    """
    return {str(kwargs[key]) if not isinstance(key, Hashable) else kwargs[key]: key for key in kwargs}

# print(kwarg_to_dict(физика=5, русский=4))

