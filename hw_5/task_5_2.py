from typing import List


def premium_calculation(names: List[str], rates: List[int], bonuses: List[str]) -> dict:
    """
    Рассчитывает сумму премии для каждого сотрудника и возвращает словарь с именем в качестве ключа
    и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.

    :param names: Список имен сотрудников.
    :param rates: Список ставок сотрудников.
    :param bonuses: Список премий сотрудников в виде строк с указанием процентов вида "10.25%".
    :return: Словарь с именем в качестве ключа и суммой премии в качестве значения.
    """
    return {name: rate * float(bonus[:-1]) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

def test_calculate_bonus():
    names = ["Alice", "Bob", "Charlie"]
    rates = [1000, 2000, 3000]
    bonuses = ["10.5%", "5%", "12.75%"]
    expected = {"Alice": 105.0, "Bob": 100.0, "Charlie": 382.5}
    assert premium_calculation(names, rates, bonuses) == expected

    names = ["Frank"]
    rates = [3000]
    bonuses = ["15%"]
    expected = {"Frank": 450.0}
    assert premium_calculation(names, rates, bonuses) == expected

if __name__ == '__main__':
    test_calculate_bonus()