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
        Устанавливает значение атрибута с проверкой на правильность ФИО.

        :param instance: Экземпляр класса Student.
        :param value: Значение ФИО.
        :raises ValueError: Если ФИО не начинается с заглавной буквы или содержит не только буквы.
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
        Добавляет оценку по предмету.

        :param grade: Оценка (от 2 до 5).
        :raises ValueError: Если оценка не в диапазоне от 2 до 5.
        """
        if grade < 2 or grade > 5:
            raise ValueError('Оценка должна быть от 2 до 5')
        self.grades.append(grade)

    def add_test_score(self, score: Union[int, float]) -> None:
        """
        Добавляет результат теста по предмету.

        :param score: Результат теста (от 0 до 100).
        :raises ValueError: Если результат теста не в диапазоне от 0 до 100.
        """
        if score < 0 or score > 100:
            raise ValueError('Результат теста должен быть от 0 до 100')
        self.test_scores.append(score)

    def average_test_score(self) -> float:
        """
        Возвращает средний балл по тестам для предмета.

        :return: Средний балл по тестам.
        """
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def average_grade(self) -> float:
        """
        Возвращает средний балл по оценкам для предмета.

        :return: Средний балл по оценкам.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Subject.

        :return: Строковое представление объекта Subject.
        """
        return f'Subject(name={self.name})'


class Student:
    full_name = NameValidator()

    def __init__(self, full_name: str, subjects_file: str) -> None:
        """
        Инициализирует объект Student.

        :param full_name: Полное имя студента.
        :param subjects_file: Путь к файлу CSV с названиями предметов.
        """
        self.full_name = full_name
        self.subjects: dict[str, Subject] = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file: str) -> dict[str, Subject]:
        """
        Загружает предметы из файла CSV.

        :param subjects_file: Путь к файлу CSV с названиями предметов.
        :return: Словарь объектов Subject с ключами-названиями предметов.
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
        :param grade: Оценка (от 2 до 5).
        :raises ValueError: Если предмет не найден или оценка не в диапазоне от 2 до 5.
        """
        subject = self.find_subject(subject_name)
        subject.add_grade(grade)

    def add_test_score(self, subject_name: str, score: Union[int, float]) -> None:
        """
        Добавляет результат теста по предмету.

        :param subject_name: Название предмета.
        :param score: Результат теста (от 0 до 100).
        :raises ValueError: Если предмет не найден или результат теста не в диапазоне от 0 до 100.
        """
        subject = self.find_subject(subject_name)
        subject.add_test_score(score)

    def remove_subject(self, subject_name: str) -> None:
        """
        Удаляет предмет из списка предметов студента.

        :param subject_name: Название предмета.
        :raises ValueError: Если предмет не найден.
        """
        if subject_name not in self.subjects:
            raise ValueError(f'Предмет {subject_name} не найден')
        del self.subjects[subject_name]

    def find_subject(self, subject_name: str) -> Subject:
        """
        Находит объект Subject по названию предмета.

        :param subject_name: Название предмета.
        :return: Объект Subject.
        :raises ValueError: Если предмет не найден.
        """
        if subject_name not in self.subjects:
            raise ValueError(f'Предмет {subject_name} не найден')
        return self.subjects[subject_name]

    def average_test_score(self, subject_name: str) -> float:
        """
        Возвращает средний балл по тестам для предмета.

        :param subject_name: Название предмета.
        :return: Средний балл по тестам.
        :raises ValueError: Если предмет не найден.
        """
        subject = self.find_subject(subject_name)
        return subject.average_test_score()

    def average_grade(self, subject_name: str) -> float:
        """
        Возвращает средний балл по оценкам для предмета.

        :param subject_name: Название предмета.
        :return: Средний балл по оценкам.
        :raises ValueError: Если предмет не найден.
        """
        subject = self.find_subject(subject_name)
        return subject.average_grade()

    def average_grades_all_subjects(self) -> float:
        """
        Возвращает средний балл по оценкам для всех предметов.

        :return: Средний балл по оценкам.
        """
        grades_sum = 0
        subjects_count = 0
        for subject in self.subjects.values():
            grades_sum += subject.average_grade()
            subjects_count += 1
        return grades_sum / subjects_count

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Student.

        :return: Строковое представление объекта Student.
        """
        return f'Student(full_name={self.full_name}, subjects={self.subjects})'

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Student.

        :return: Строковое представление объекта Student.
        """
        return f'Student: {self.full_name}'
