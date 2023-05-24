import csv
import json
from math import sqrt
from random import randint
from typing import Callable


def quadratic_roots(a: int, b: int, c: int) -> tuple | None | float:
    """
    Нахождение корней квадратного уравнения.

    :param a: число a
    :param b: число b
    :param c: число c
    :return: корни квадратного уравнения
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        sqrt_discriminant = sqrt(discriminant)
        x_1 = (-b + sqrt_discriminant) / (2 * a)
        x_2 = (-b - sqrt_discriminant) / (2 * a)
        return x_1, x_2


def generate_csv(filename: str, rows: int = 100) -> None:
    """
    Генерация csv файла с тремя случайными числами в каждой строке.

    :param filename: имя файла
    :param rows: количество строк
    """
    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


def csv_decorator(func: Callable):
    """
    Декоратор, запускающий функцию нахождения корней квадратного уравнения
    с каждой тройкой чисел из csv файла.

    :param func: функция нахождения корней квадратного уравнения
    :return: декорированная функция
    """
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            answer = {}
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                answer[f'{a}x^2 + {b}x + {c} = 0'] = result
                # print(f'Equation: {a}x^2 + {b}x + {c} = 0')
                # print(f'Answer: {result}')
                # print('=' * 30)
            return answer

    return wrapper

def save_to_json(filename: str) -> Callable:
    """
    :param filename: Имя для json файла
    """
    def wrapper_(func) -> Callable:
        """
        Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

        :param func: декорируемая функция
        :return: декорированная функция
        """
        def wrapper(*args, **kwargs):
            parameters = {'args': args, 'kwargs': kwargs}
            result = func(*args, **kwargs)
            data = {'parameters': parameters, 'result': result}
            with open(filename + '.json', 'w') as file:
                json.dump(data, file, indent=4)
        return wrapper
    return wrapper_


@save_to_json('result')
def quadratic_logging(a, b, c):
    return quadratic_roots(a, b, c)

# if __name__ == '__main__':
    # отладка
    # roots = quadratic_roots(1, -5, 6)
    # print(f"Ответ: {roots}")
    #
    # generate_csv("data", 100)
    #
    # decorated_func = csv_decorator(quadratic_roots)
    # decorated_func("data.csv")
    #
    # quadratic_logging(2, -7, 3)