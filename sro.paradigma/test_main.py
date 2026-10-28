import unittest
from models import Student, WeightedPolicy, BestAttemptPolicy, GradeBook
from logic import (calculate_average_procedural, calculate_average_functional, 
                   calculate_average_oop, get_top_students, get_all_grades)

class TestGradeSystem(unittest.TestCase):
    def setUp(self):
        self.s1 = Student(1, "Досжан Алижан", "ТИИ25-21", {"AI": [90, 80], "Python": [100, 90]})
        self.s2 = Student(2, "Иван", "ТИИ25-22", {"AI": [40, 50], "Python": [60, 60]})
        self.s3 = Student(3, "Анна", "ТИИ25-21", {})

    def test_procedural_avg(self):
        self.assertEqual(calculate_average_procedural(self.s1), 90.0)

    def test_functional_avg(self):
        self.assertEqual(calculate_average_functional(self.s1), 90.0)

    def test_empty_grades_procedural(self):
        self.assertEqual(calculate_average_procedural(self.s3), 0.0)
        
    def test_empty_grades_functional(self):
        self.assertEqual(calculate_average_functional(self.s3), 0.0)

    def test_weighted_policy(self):
        policy = WeightedPolicy()
        self.assertEqual(policy.calculate_gpa(self.s1.grades), 90.0)

    def test_best_attempt_policy(self):
        policy = BestAttemptPolicy()
        # Max of AI is 90, Max of Python is 100. Avg of maxes = 95.0
        self.assertEqual(policy.calculate_gpa(self.s1.grades), 95.0)

    def test_get_all_grades(self):
        self.assertEqual(get_all_grades(self.s1), [90, 80, 100, 90])

    def test_top_students(self):
        top = get_top_students([self.s1, self.s2], 85)
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0].name, "Досжан Алижан")

    def test_gradebook_add(self):
        gb = GradeBook(WeightedPolicy())
        gb.add_student(self.s1)
        self.assertEqual(len(gb.get_students()), 1)

    def test_best_attempt_empty(self):
        policy = BestAttemptPolicy()
        self.assertEqual(policy.calculate_gpa({}), 0.0)

    def test_weighted_empty(self):
        policy = WeightedPolicy()
        self.assertEqual(policy.calculate_gpa({}), 0.0)

    def test_get_top_students_empty(self):
        self.assertEqual(get_top_students([], 50), [])

if __name__ == '__main__':
    unittest.main()
