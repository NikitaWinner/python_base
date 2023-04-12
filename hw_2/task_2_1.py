def convert_to_hex(user_number: int) -> str:
    """
    Функция принимает целое число и возвращает его
    шестнадцатеричное строковое представление с префиксом '0x'.
    """
    hex_digits = '0123456789abcdef'  # строка со всеми шестнадцатеричными символами
    hex_number = ''  # переменная для хранения шестнадцатеричного значения
    while user_number > 0:
        hex_number = hex_digits[user_number % 16] + hex_number
        user_number //= 16
    return '0x' + hex_number if hex_number else '0x0'

# unit-тесты
def test_convert_to_hex():
    assert convert_to_hex(0) == hex(0)
    assert convert_to_hex(10) == hex(10)
    assert convert_to_hex(16) == hex(16)
    assert convert_to_hex(255) == hex(255)
    assert convert_to_hex(4096) == hex(4096)
    assert convert_to_hex(65535) == hex(65535)
    assert convert_to_hex(10**6) == hex(10**6)


if __name__ == '__main__':
    test_convert_to_hex()