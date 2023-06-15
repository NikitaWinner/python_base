import unittest
from task_14_1 import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.subjects_file = 'subjects.csv'

    def test_average_test_score(self):
        """
        Проверяет метод average_test_score.

        Убеждается, что метод возвращает правильное среднее значение результатов тестов для предмета.

        """
        student = Student('John Doe', self.subjects_file)
        student.add_test_score('Math', 80)
        student.add_test_score('Math', 90)
        average_score = student.average_test_score('Math')
        self.assertEqual(average_score, 85.0)

    def test_average_grade(self):
        """
        Проверяет метод average_grade.

        Убеждается, что метод возвращает правильное среднее значение оценок для предмета.

        """
        student = Student('John Doe', self.subjects_file)
        student.add_grade('Math', 4)
        student.add_grade('Math', 5)
        average_grade = student.average_grade('Math')
        self.assertEqual(average_grade, 4.5)

    def test_add_grade(self):
        """
        Проверяет метод add_grade.

        Убеждается, что оценка добавляется в список оценок предмета.

        """
        student = Student('John Doe', self.subjects_file)
        student.add_grade('Math', 4)
        self.assertIn('Math', student.subjects)
        self.assertEqual(len(student.subjects['Math'].grades), 1)
        self.assertEqual(student.subjects['Math'].grades[0], 4)

    def test_add_test_score(self):
        """
        Проверяет метод add_test_score.

        Убеждается, что результат теста добавляется в список результатов тестов предмета.

        """
        student = Student('John Doe', self.subjects_file)
        student.add_test_score('Math', 80)
        self.assertIn('Math', student.subjects)
        self.assertEqual(len(student.subjects['Math'].test_scores), 1)
        self.assertEqual(student.subjects['Math'].test_scores[0], 80)

    def test_remove_subject(self):
        """
        Проверяет метод remove_subject.

        Убеждается, что предмет удаляется из словаря предметов.

        """
        student = Student('John Doe', self.subjects_file)
        student.remove_subject('Math')
        self.assertNotIn('Math', student.subjects)

    def test_find_subject(self):
        """
        Проверяет метод find_subject.

        Убеждается, что метод возвращает правильный объект предмета для заданного названия предмета.

        """
        student = Student('John Doe', self.subjects_file)
        math_subject = student.find_subject('Math')
        self.assertIsNotNone(math_subject)
        self.assertEqual(math_subject.name, 'Math')


if __name__ == "__main__":
    unittest.main()