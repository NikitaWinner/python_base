from typing import Generator

def fibonacci() -> Generator[int]:
    """ Функция-генератор чисел фибоначи
    с бесконенчой выдачей """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for i in range(10):
    print(next(fib))