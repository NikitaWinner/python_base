import sys
import random


def guess_number(low: int, high: int, tries: int) -> bool:
    """
    Игра "Угадай число".

    :param low: Нижняя граница диапазона чисел.
    :param high: Верхняя граница диапазона чисел.
    :param tries: Количество попыток.
    :return: Возвращает True, если число угадано,
             и False, если попытки исчерпаны.
    """
    secret_number = random.randint(low, high)
    print(f"Я загадал число от {low} до {high}. Угадай его за {tries} попыток.")

    for attempt in range(1, tries + 1):
        guess = int(input(f"Попытка {attempt}: "))
        if guess == secret_number:
            print(f'Поздравляю, вы угадали число "{secret_number}"!')
            return True
        elif guess < secret_number:
            print("Загаданное число больше!")
        else:
            print("Загаданное число меньше!")

    else:
        print(f"К сожалению, вы не угадали число. Я загадал число {secret_number}.")
        return False


__all__ = ['guess_number']

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        print("Недостаточно аргументов. "
              "Введите границы диапазона и количество попыток через пробел.")
    elif len(args) > 3:
        print("Слишком много аргументов. "
              "Введите границы диапазона и количество попыток через пробел.")
    else:
        try:
            lower, upper, attempts = (int(arg) for arg in args)
            guess_number(lower, upper, attempts)
        except ValueError:
            print("Некорректный ввод. "
                  "Введите границы диапазона и количество попыток через пробел, "
                  "используя целые числа.")
