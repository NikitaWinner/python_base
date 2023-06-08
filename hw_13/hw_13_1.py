import csv
from typing import List, Union
from pathlib import Path


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value: str) -> None:
        """
        Устанавливает значение атрибута и проверяет его корректность.

        :param instance: Экземпляр класса Student.
        :param value: Значение атрибута.
        :raises ValueError: Если значение не соответствует правилам валидации имени.
        :return: None
        """
        if not value[0].isupper():
            raise ValueError(f'{self.name} должно начинаться с заглавной буквы')
        last, first = value.split()
        if not last.isalpha() and not first.isalpha():
            raise ValueError(f'{self.name} должно содержать только буквы')
        instance.__dict__[self.name] = value


class Subject:
    def __init__(self, name: str):
        self.name = name
        self.grades: List[int] = []
        self.test_scores: List[Union[int, float]] = []

    def add_grade(self, grade: int) -> None:
        """
        Добавляет оценку предмету.

        :param grade: Оценка.
        :raises ValueError: Если оценка не в диапазоне от 2 до 5.
        :return: None
        """
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть от 2 до 5')
        self.grades.append(grade)

    def add_test_score(self, score: Union[int, float]) -> None:
        """
        Добавляет результат теста предмету.

        :param score: Результат теста.
        :raises ValueError: Если результат теста не в диапазоне от 0 до 100.
        :return: None
        """
        if score < 0 or score > 100:
            raise ValueError('Результат теста должен быть от 0 до 100')
        self.test_scores.append(score)

    def average_test_score(self) -> float:
        """
        Вычисляет средний результат тестов по предмету.

        :return: Средний результат тестов.
        """
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def average_grade(self) -> float:
        """
        Вычисляет средний балл по предмету.

        :return: Средний балл.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __repr__(self) -> str:
        return f'Subject(name={self.name})'


class Student:
    full_name = NameValidator()

    def __init__(self, full_name: str, subjects_file: str) -> None:
        """
        Инициализирует экземпляр класса Student.

        :param full_name: Полное имя студента.
        :param subjects_file: Путь к файлу с предметами.
        :raises FileNotFoundError: Если файл с предметами не найден.
        :return: None
        """
        self.full_name = full_name
        self.subjects: dict[str, Subject] = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file: str) -> dict[str, Subject]:
        """
        Загружает предметы из файла.

        :param subjects_file: Путь к файлу с предметами.
        :raises FileNotFoundError: Если файл с предметами не найден.
        :return: Словарь предметов.
        """
        subjects = {}
        subjects_file_path = Path(subjects_file)
        if not subjects_file_path.is_file():
            raise FileNotFoundError(f"Файл {subjects_file} не найден")

        with open(subjects_file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                subject_name = row[0]
                subjects[subject_name] = Subject(subject_name)
        return subjects

    def add_grade(self, subject_name: str, grade: int) -> None:
        """
        Добавляет оценку по предмету.

        :param subject_name: Название предмета.
        :param grade: Оценка.
        :raises SubjectNotFoundError: Если предмет не найден.
        :raises InvalidGradeError: Если оценка некорректна.
        :return: None
        """
        if subject_name not in self.subjects:
            raise SubjectNotFoundError(f'Предмет {subject_name} не найден')
        subject = self.subjects[subject_name]
        try:
            subject.add_grade(grade)
        except ValueError as e:
            raise InvalidGradeError(str(e))

    def add_test_score(self, subject_name: str, score: Union[int, float]) -> None:
        """
        Добавляет результат теста по предмету.

        :param subject_name: Название предмета.
        :param score: Результат теста.
        :raises SubjectNotFoundError: Если предмет не найден.
        :raises InvalidTestScoreError: Если результат теста некорректен.
        :return: None
        """
        if subject_name not in self.subjects:
            raise SubjectNotFoundError(f'Предмет {subject_name} не найден')
        subject = self.subjects[subject_name]
        try:
            subject.add_test_score(score)
        except ValueError as e:
            raise InvalidTestScoreError(str(e))

    def remove_subject(self, subject_name: str) -> None:
        """
        Удаляет предмет.

        :param subject_name: Название предмета.
        :raises SubjectNotFoundError: Если предмет не найден.
        :return: None
        """
        if subject_name not in self.subjects:
            raise SubjectNotFoundError(f'Предмет {subject_name} не найден')
        del self.subjects[subject_name]

    def find_subject(self, subject_name: str) -> Subject:
        """
        Находит предмет по названию.

        :param subject_name: Название предмета.
        :raises SubjectNotFoundError: Если предмет не найден.
        :return: Найденный предмет.
        """
        if subject_name not in self.subjects:
            raise SubjectNotFoundError(f'Предмет {subject_name} не найден')
        return self.subjects[subject_name]

    def average_test_score(self, subject_name: str) -> float:
        """
        Вычисляет средний результат тестов по предмету.

        :param subject_name: Название предмета.
        :raises SubjectNotFoundError: Если предмет не найден.
        :return: Средний результат тестов.
        """
        subject = self.find_subject(subject_name)
        return subject.average_test_score()

    def average_grade(self, subject_name: str) -> float:
        """
        Вычисляет средний балл по предмету.

        :param subject_name: Название предмета.
        :raises SubjectNotFoundError: Если предмет не найден.
        :return: Средний балл.
        """
        subject = self.find_subject(subject_name)
        return subject.average_grade()

    def average_grades_all_subjects(self) -> float:
        """
        Вычисляет общий средний балл по всем предметам.

        :return: Общий средний балл.
        """
        grades_sum = 0
        subjects_count = 0
        for subject in self.subjects.values():
            grades_sum += subject.average_grade()
            subjects_count += 1
        return grades_sum / subjects_count

    def __repr__(self) -> str:
        return f'Student(full_name={self.full_name}, subjects={self.subjects})'

    def __str__(self) -> str:
        return f'Student: {self.full_name}'


class FileNotFoundError(Exception):
    """
    Исключение, возникающее при отсутствии файла.

    Attributes:
        message (str): Сообщение об ошибке.

    Methods:
        __str__(): Возвращает строковое представление исключения.
    """

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class SubjectNotFoundError(Exception):
    """
    Исключение, возникающее при отсутствии предмета.

    Attributes:
        message (str): Сообщение об ошибке.

    Methods:
        __str__(): Возвращает строковое представление исключения.
    """

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class InvalidGradeError(Exception):
    """
    Исключение, возникающее при некорректной оценке.

    Attributes:
        message (str): Сообщение об ошибке.

    Methods:
        __str__(): Возвращает строковое представление исключения.
    """

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class InvalidTestScoreError(Exception):
    """
    Исключение, возникающее при некорректном результате теста.

    Attributes:
        message (str): Сообщение об ошибке.

    Methods:
        __str__(): Возвращает строковое представление исключения.
    """

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message



try:
    student = Student("John Doe", "subjects.csv")
    student.add_grade("Math", 4)
    student.add_test_score("Math", 80)
    student.add_grade("English", 5)
    student.add_test_score("English", 90)
    print(f"Средний балл по математике: {student.average_grade('Math')}")
    print(f"Средний балл по английскому: {student.average_grade('English')}")
    print(f"Общий средний балл по предметам: {student.average_grades_all_subjects()}")
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except SubjectNotFoundError as e:
    print(f"Ошибка: {e}")
except InvalidGradeError as e:
    print(f"Ошибка: {e}")
except InvalidTestScoreError as e:
    print(f"Ошибка: {e}")
