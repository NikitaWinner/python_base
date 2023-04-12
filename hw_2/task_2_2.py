from fractions import Fraction
from typing import List, Tuple


def calculate_fractions_using_fraction_module(a: str, b: str) -> Tuple[str, str]:
    """ Вычисляет сумму и произведение двух дробей, используя модуль fractions.

    :param a: Строка с первой дробью в формате "числитель/знаменатель".
    :param b: Строка со второй дробью в формате "числитель/знаменатель".
    :return: Кортеж из двух строк - суммы и произведения двух дробей.
    """
    x = Fraction(a)
    y = Fraction(b)
    return str(x + y), str(x * y)


def calculate_fractions(fraction1: str, fraction2: str) -> Tuple[str, str]:
    """ Вычисляет сумму и произведение двух дробей.

    :param fraction1: Строка с первой дробью в формате "числитель/знаменатель".
    :param fraction2: Строка со второй дробью в формате "числитель/знаменатель".
    :return: Кортеж из двух строк - суммы и произведения двух дробей.
    """
    # Преобразуем строки в числитель и знаменатель
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    # Вычисляем сумму
    sum_num = num1 * denom2 + num2 * denom1
    sum_denom = denom1 * denom2

    # Вычисляем произведение
    prod_num = num1 * num2
    prod_denom = denom1 * denom2

    # Сокращаем дроби, если возможно
    for i in range(2, min(sum_num, sum_denom) + 1):
        while sum_num % i == 0 and sum_denom % i == 0:
            sum_num //= i
            sum_denom //= i
        while prod_num % i == 0 and prod_denom % i == 0:
            prod_num //= i
            prod_denom //= i

    # Возвращаем кортеж с суммой и произведением
    return (str(Fraction(sum_num, sum_denom)), str(Fraction(prod_num, prod_denom)))


def test_calculate_fractions() -> None:
    """ Тестирует функцию calculate_fractions() и сравнивает её
    результаты с функцией calculate_fractions_using_fraction_module().
    Проверяет, что результаты являются корректными дробями.
    """
    # Тестовые данные
    data: List[Tuple[str, str]] = [('2/3', '1/4'), ('1/2', '3/4'), ('4/5', '1/10'), ('1/10', '2/7'), ('-1/2', '-1/2')]

    for fraction1, fraction2 in data:
        # Сравниваем результаты двух функций
        result1 = calculate_fractions(fraction1, fraction2)
        result2 = calculate_fractions_using_fraction_module(fraction1, fraction2)
        assert result1 == result2, f'Error: {result1} != {result2}'

        # Проверяем, что результаты являются корректными дробями
        assert isinstance(Fraction(result1[0]), Fraction) \
               and isinstance(Fraction(result1[1]), Fraction), \
               f'Error: {result1[0]} or {result1[1]} is not a fraction'


if __name__ == '__main__':
    test_calculate_fractions()

