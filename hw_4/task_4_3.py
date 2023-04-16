transactions = []

def calculate_withdrawal_fee(amount: int) -> int:
    """
    Функция для расчета комиссии за снятие денег

    :param amount: сумма, которую нужно снять
    :return: размер комиссии за снятие денег
    """
    withdrawal_fee = int(amount * 0.015)
    if withdrawal_fee < 30:
        withdrawal_fee = 30
    elif withdrawal_fee > 600:
        withdrawal_fee = 600
    return withdrawal_fee


def calculate_interest(amount: int, interest_rate: float) -> int:
    """
    Функция для расчета процентов на счету

    :param amount: сумма на счету
    :param interest_rate: процентная ставка
    :return: размер процентов на счету
    """
    interest = int(amount * interest_rate)
    return interest


def deposit_money(balance: int, amount: int) -> int:
    """
    Функция для пополнения счета

    :param balance: текущий баланс
    :param amount: сумма для пополнения
    :return: новый баланс
    """
    balance += amount
    transactions.append(amount)
    return balance


def withdraw_money(balance: int, amount: int) -> int:
    """
    Функция для снятия денег со счета

    :param balance: текущий баланс
    :param amount: сумма для снятия
    :return: новый баланс
    """
    if amount > balance:
        print("Нельзя снять больше, чем на счету")
        return balance
    else:
        withdrawal_fee = calculate_withdrawal_fee(amount)
        total_sum = amount + withdrawal_fee
        balance -= total_sum
        transactions.append(-total_sum)
        return balance


def add_taxes(balance: int) -> int:
    """
    Функция для вычета налога на богатство

    :param balance: текущий баланс
    :return: новый баланс
    """
    taxes = int(balance * 0.1)
    transactions.append(-taxes)
    balance -= taxes
    print(f"Вычитаем налог на богатство в размере {taxes} у.е.")
    return balance


def is_third_operation(number_operation: int) -> bool:
    """
    Функция для проверки номера операции

    :param number_operation: Номер текущей операции
    :return: True, если третья операция, иначе False
    """
    return not number_operation % 3


def is_multiple_fifty(sum_: int) -> bool:
    """
    Функция для проверки корректности суммы для снятия.

    :param sum_: Сумма для снятия
    :return: True, если кратна 50, иначе False
    """
    return not sum_ % 50


def exit_program() -> None:
    """Завершение программы"""
    print('Рады видеть вас снова!')
    exit()


def main():
    balance = 0
    operations_count = 0

    while True:
        print(f"Баланс: {balance} у.е.")
        print(f'История операций {transactions}')
        operation = input("Введите действие (пополнить, снять, выйти): ")
        if operation == "выйти":
            exit_program()
        elif operation == "пополнить":
            amount = int(input("Введите сумму: "))
            if not is_multiple_fifty(amount):
                print("Сумма должна быть кратна 50 у.е.")
                continue
            balance = deposit_money(balance, amount)
            operations_count += 1
            if is_third_operation(operations_count):
                interest = calculate_interest(balance, 0.03)
                balance += interest
                print(f"Начислены проценты в размере {interest} у.е.")
        elif operation == "снять":
            amount = int(input("Введите сумму: "))
            if not is_multiple_fifty(amount):
                print("Сумма должна быть кратна 50 у.е.")
                continue
            if balance + amount > 5_000_000:
                balance = add_taxes(balance)
            balance = withdraw_money(balance, amount)
            operations_count += 1
            if is_third_operation(operations_count):
                interest = calculate_interest(balance, 0.03)
                balance += interest
                print(f"Начислены проценты в размере {interest} у.е.")
        else:
            print("Некорректная операция, повторите попытку")


main()
