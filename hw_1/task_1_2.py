def composite_or_simple(number: int) -> str:
    """ Функция определяет, является число составным или простым
    :return: 'composite', если число составное,
             'simple', если число простое.
    """
    counter_divisor = 1
    for i in range(2, number+1):
        if not number % i:
            counter_divisor += 1
            if counter_divisor > 2:
                return 'composite'
    return 'simple'


def is_correct_number(number):
    return 0 < number < 100_000


user_number = int(input('Введите число для проверки: '))
while True:
    if is_correct_number(user_number):
        result = composite_or_simple(user_number)
        print(f'Введенное число является {result}')
    else:
        print('Введенное значение некорректно')
        print('Введите число в диапазоне от 1 до 100000')
    user_number = int(input('Введите число для проверки: '))