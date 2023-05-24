from random import randint
from typing import Callable
from functools import wraps
import json
import os


def validator(func):
    @wraps(func)
    def wrapper():
        min_number = 1
        max_number = 100
        min_attempts = 1
        max_attempts = 10

        number = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Введите количество попыток от 1 до 10: "))

        if min_number <= number <= max_number and min_attempts <= attempts <= max_attempts:
            func(number, attempts)
        else:
            print("Введены некорректные значения. Запускаю игру со случайными числами.")
            func(randint(min_number, max_number), randint(min_attempts, max_attempts))

    return wrapper

def save_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = func.__name__ + ".json"
        data = []
        # загружаем данные из существующего файла, если он существует, что бы обеспечить корректную перезапись
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                data = json.load(file)
        parameters = {
            "args": args,
            "kwargs": kwargs
        }
        result = func(*args, **kwargs)
        data.append({
            "param": parameters,
            "return": result
        })

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        return result

    return wrapper


def count_call(number: int) -> Callable:
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = 'Функция вызвана 0 раз'
            for i in range(number):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return deco


@validator
@count_call(number=5)
@save_to_json
def number_guessing_game(number: int, attempts: int):
    print("Загаданное число:", number)
    print("Количество попыток:", attempts)
    print("У вас есть", attempts, "попыток.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Попытка №{attempt}: Введите ваше предположение: "))

        if guess == number:
            print("Поздравляю! Вы угадали число!")
            return

        if guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    print("К сожалению, вы исчерпали все попытки. Загаданное число было:", number)

