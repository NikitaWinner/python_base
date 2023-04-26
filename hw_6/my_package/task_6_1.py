from sys import argv


def is_leap(year: int) -> bool | int:
    """
    Функция проверки года на високосность.

    :param year: Год (от 1 до 9999).
    :return: 1(True), если год високосный, иначе 0(False).
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date_string: str) -> bool:
    """
    Функция проверки валидности даты в формате DD.MM.YYYY.

    :param date_string: строка, содержащая дату в формате "DD.MM.YYYY".
    :return: True, если дата может существовать,
             и False, если такая дата невозможна
    :raise ValueError: Если строка не соответствует формату DD.MM.YYYY
            или год не в диапазоне [1, 9999]
    """
    # Проверяем формат даты
    try:
        day, month, year = map(int, date_string.split('.'))
    except ValueError:
        raise ValueError("Некорректный формат даты. Используйте формат DD.MM.YYYY")

    if year < 1 or year > 9999:
        raise ValueError("Год должен быть в диапазоне [1, 9999]")
    if month < 1 or month > 12:
        raise ValueError("Месяц должен быть в диапазоне [1, 12]")
    days_in_month = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month - 1]:
        return False
    return True


if __name__ == '__main__':
    data = ''.join(argv[1:])
    print(is_valid_date(data))
