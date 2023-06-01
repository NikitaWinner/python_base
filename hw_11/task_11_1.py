class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self) -> str:
        """
        Возвращает строковое представление матрицы.

        :return: Строковое представление матрицы.
        """
        return '\n'.join([' '.join([str(val) for val in row]) for row in self.data])

    def __eq__(self, other: 'Matrix') -> bool:
        """
        Проверяет, равна ли текущая матрица другой матрице.

        :param other: Другая матрица для сравнения.
        :return: True, если матрицы равны. Иначе False.
        """
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for row_self, row_other in zip(self.data, other.data):
            for val_self, val_other in zip(row_self, row_other):
                if val_self != val_other:
                    return False
        return True

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Выполняет сложение матриц.

        :param other: Матрица для сложения.
        :return: Результирующая матрица.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Можно складывать только матрицы")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера")
        result = Matrix(self.rows, self.cols)
        for i, row_self in enumerate(self.data):
            for j, val_self in enumerate(row_self):
                result.data[i][j] = val_self + other.data[i][j]
        return result

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """
        Выполняет умножение матриц.

        :param other: Матрица для умножения.
        :return: Результирующая матрица.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Можно умножать только матрицы")
        if self.cols != other.rows:
            raise ValueError("Матрицы не согласованы. \n"
                             "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i, row_self in enumerate(self.data):
            for j in range(other.cols):
                for k, val_self in enumerate(row_self):
                    result.data[i][j] += val_self * other.data[k][j]
        return result


def test_matrix_operations():
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(2, 3)
    matrix3 = Matrix(3, 2)
    matrix4 = Matrix(3, 2)
    matrix5 = Matrix(2, 2)

    # Заполняем матрицы
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    matrix2.data = [[7, 8, 9], [10, 11, 12]]
    matrix3.data = [[1, 2], [3, 4], [5, 6]]
    matrix4.data = [[7, 8], [9, 10], [11, 12]]
    matrix5.data = [[1, 2], [3, 4]]

    # Проверяем операции

    # Проверка вывода на печать
    print("Матрица 1:")
    print(matrix1)
    print("Матрица 2:")
    print(matrix2)
    print("Матрица 3:")
    print(matrix3)
    print("Матрица 4:")
    print(matrix4)
    print("Матрица 5:")
    print(matrix5)
    print()

    # Проверка сложения матриц
    print("Сумма матриц 1 и 2:")
    print(matrix1 + matrix2)
    print()



# Запуск тестов
test_matrix_operations()