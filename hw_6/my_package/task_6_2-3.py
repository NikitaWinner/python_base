"""
Модуль для решения задачи о 8 ферзях.
"""

import itertools
import random


# Задаем список столбцов и количество ферзей
COLUMNS = "abcdefgh"
NQUEENS = len(COLUMNS)
ACCEPT = "accept"
CONTINUE = "continue"
ABANDON = "abandon"


def main() -> None:
    """ Функция для запуска решения задачи. """
    solve([], n=1)


def solve(partial_solution: list[str], n: int) -> None:
    """
    Рекурсивная функция для решения задачи.

    :param partial_solution: Частичное решение.
    :param n: Количество оставшихся ферзей для размещения.
    """
    exam = examine(partial_solution)
    # Проверяем частичное решение
    if exam == ACCEPT:
        # Если решение найдено, выводим его
        print(partial_solution)
    # Если еще не все ферзи размещены и решение может быть продолжено
    elif exam == CONTINUE and n > 0:
        # Расширяем текущее решение и рекурсивно вызываем solve для каждого расширения
        for p in extend(partial_solution):
            solve(p, n - 1)


def examine(partial_solution: list[str]) -> str:
    """
    Функция для проверки частичного решения.

    :param partial_solution: Частичное решение.
    :return: Результат проверки: "accept", "continue" или "abandon".
    """
    # Проверяем, не атакуют ли ферзи друг друга
    for p1, p2 in itertools.combinations(partial_solution, 2):
        if attacks(p1, p2):
            return ABANDON
    # Если решение содержит 8 ферзей, то оно завершено
    if len(partial_solution) == NQUEENS:
        return ACCEPT
    else:
        return CONTINUE


def attacks(p1: str, p2: str) -> bool:
    """
    Функция для проверки возможности атаки ферзя.

    :param p1: Координаты первого ферзя.
    :param p2: Координаты второго ферзя.
    :return: Результат проверки: True,
             если ферзи могут атаковать друг друга, иначе False.
    """
    # Проверяем, находятся ли ферзи на одной горизонтали, вертикали или диагонали
    if p1 == p2:
        return False
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return (row1 == row2 or column1 == column2 or
            abs(row1 - row2) == abs(column1 - column2))


def extend(partial_solution: list[str]) -> list[list[str]]:
    """
    Функция для расширения частичного решения.

    :param partial_solution: Частичное решение.
    :return: Список возможных расширений частичного решения.
    """
    # Создаем новые возможные решения, добавляя ферзей в следующий ряд на каждую колонку
    results = []
    row = len(partial_solution) + 1
    for column in COLUMNS:
        new_solution = list(partial_solution)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results


def solve_queens(n: int) -> list[tuple]:
    for _ in range(100):  # Попробуем 100 случайных расстановок
        positions = random.sample(range(1, NQUEENS + 1), n)
        solution = [(COLUMNS[i], row) for i, row in enumerate(positions, start=0)]
        exam = examine(solution)
        if exam == ACCEPT:
            return solution
    return []  # Если решение не найдено, возвращаем пустой список


if __name__ == '__main__':
    count = 0
    i = 0
    while count < 4:
        solution = solve_queens(8)
        if solution:
            print(f"Решение {i + 1}: {solution}")
            count += 1
        else:
            print(f"Решение {i + 1}: Решение не найдено")
        i += 1