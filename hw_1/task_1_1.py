def is_exist_triangle(edge_a, edge_b, edge_c) -> bool:
    """ Функция доказывает теорему неравенства треугольников.
    :return: True, если треугольник существует, иначе False.
    """
    return edge_a + edge_b > edge_c \
        and edge_a + edge_c + edge_b \
        and edge_b + edge_c > edge_a


a = float(input('Введите сторону а: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

if is_exist_triangle(a, b, c):
    if a == b == c:
        print('Equilateral triangle.')
    elif a != b != c != a:
        print('Scalene triangle.')
    else:
        print('Isosceles triangle.')
else:
    print('triangle not exist')



