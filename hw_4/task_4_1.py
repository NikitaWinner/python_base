def transpose_matrix(matrix: list[list]) -> list[list]:
    """
    Функция для транспонирования матрицы.

    :param matrix: Список списков - матрица.
    :return: список списков - транспонированная матрица.
    """
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]


def test_transpose_matrix() -> None:
    """ Тесты """

    # Тест матрицы 2x2
    matrix = [[1, 2],
              [3, 4]]
    expected_result = [[1, 3],
                       [2, 4]]
    assert transpose_matrix(matrix) == expected_result

    # Тест матрицы 3x3
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    expected_result = [[1, 4, 7],
                       [2, 5, 8],
                       [3, 6, 9]]
    assert transpose_matrix(matrix) == expected_result

    # Тест матрицы 2x3
    matrix = [[1, 2, 3],
              [4, 5, 6]]
    expected_result = [[1, 4],
                       [2, 5],
                       [3, 6]]
    assert transpose_matrix(matrix) == expected_result

