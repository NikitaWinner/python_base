from random import randint


_guessed_riddles = {}


def guess_riddle(riddle: str, options: list[str], attempts: int) -> int:
    """Функция угадывания загадки.

    :param riddle: строка - загадка, которую нужно отгадать.
    :param options: Список с возможными вариантами ответов.
    :param attempts: Количество попыток на отгадку.
    :return: Номер попытки, на которой отгадана загадка, или 0, если попытки исчерпаны.
    """
    print(f"Загадка: {riddle}")
    print(f"Угадайте с {attempts}-х попыток")
    options = list(map(str.lower, options))
    for i in range(1, attempts+1):
        answer = input(f"Попытка №{i}. Пишите отгадку :) ").strip().lower()
        if answer in options:
            return i
        else:
            print(f"Неправильно, это не {answer}. Попробуйте еще раз.")
    else:
        print("Попытки исчерпаны")
        return 0


def guess_riddles(riddles: dict) -> None:
    """
    Функция, которая играет в игру "Угадай загадку" с
    переданными словарём загадок и максимальным количеством попыток.

    :param riddles: Словарь, где ключ - загадка, значение - список с вариантами ответов на загадку
    """
    for riddle, options in riddles.items():
        attempt = guess_riddle(riddle, options, randint(3, 6))
        if attempt > 0:
            print(f"Вы угадали загадку с {attempt} попытки!")
            count_riddle(riddle, attempt)
        else:
            print("К сожалению, вы не смогли отгадать загадку.")
            count_riddle(riddle, attempt)


def count_riddle(riddle: str, attempts: int | str) -> None:
    """
    Функция формирует словарь с информацией о результатах отгадывания.

    :param riddle: Строка с загадкой.
    :param attempts: Номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
    """
    _guessed_riddles[riddle] = attempts


def get_guessed_riddles() -> dict:
    """
    Функция выводит результаты угадывания загадок в удобном для чтения виде.

    :return: Cловарь с информацией о результатах отгадывания.
    """
    return {f"{key} ({_guessed_riddles[key]})": "Угадано" if _guessed_riddles[key] else "Не угадано"
            for key in _guessed_riddles}

__all__ = ['guess_riddles']

if __name__ == '__main__':

    riddles_dict = {
        "Зимой и летом одним цветом": ["ёлка", "елка", "ель", "елена", "елень"],
        "Какой месяц имеет 28 дней?": ["февраль", "февральский"],
        "Сто одежек и все без застежек": ["капуста"],
        "Что можно сломать только сказав её имя?": ["молчание", "тишина"],
    }
    guess_riddles(riddles_dict)
    print(_guessed_riddles)
