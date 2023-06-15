import pytest
from task_14_1 import Student, SubjectNotFoundError,\
    InvalidGradeError, InvalidTestScoreError


def test_add_grade_valid():
    """
    Проверяет добавление корректной оценки по предмету.

    1. Создает экземпляр класса Student.
    2. Добавляет оценку "4" по предмету "Math".
    3. Проверяет, что средний балл по предмету "Math" равен 4.

    Ожидаемый результат: Средний балл по предмету "Math" равен 4.
    """
    student = Student('John Doe', 'subjects.csv')
    student.add_grade('Math', 4)
    assert student.average_grade('Math') == 4


def test_add_grade_invalid():
    """
    Проверяет обработку некорректной оценки.

    1. Создает экземпляр класса Student.
    2. Пытается добавить оценку "6" (некорректная оценка) по предмету "Math".
    3. Проверяет, что возникает исключение InvalidGradeError.

    Ожидаемый результат: Возникновение исключения InvalidGradeError.
    """
    student = Student('John Doe', 'subjects.csv')
    with pytest.raises(InvalidGradeError):
        student.add_grade('Math', 6)


def test_add_test_score_valid():
    """
    Проверяет добавление корректного результата теста по предмету.

    1. Создает экземпляр класса Student.
    2. Добавляет результат теста "80" по предмету "Math".
    3. Проверяет, что средний результат тестов по предмету "Math" равен 80.0.

    Ожидаемый результат: Средний результат тестов по предмету "Math" равен 80.0.
    """
    student = Student('John Doe', 'subjects.csv')
    student.add_test_score('Math', 80)
    assert student.average_test_score('Math') == 80.0


def test_add_test_score_invalid():
    """
    Проверяет обработку некорректного результата теста.

    1. Создает экземпляр класса Student.
    2. Пытается добавить результат теста "120" (некорректный результат) по предмету "Math".
    3. Проверяет, что возникает исключение InvalidTestScoreError.

    Ожидаемый результат: Возникновение исключения InvalidTestScoreError.
    """
    student = Student('John Doe', 'subjects.csv')
    with pytest.raises(InvalidTestScoreError):
        student.add_test_score('Math', 120)


if __name__ == '__main__':
    pytest.main()
