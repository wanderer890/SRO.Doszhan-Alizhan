from models import Student, GradeBook
from typing import List, Generator
from functools import reduce

# Лекция 3: Процедурное программирование (Декомпозиция)
def calculate_average_procedural(student: Student) -> float:
    total = 0
    count = 0
    for grades in student.grades.values():
        for grade in grades:
            total += grade
            count += 1
    return total / count if count > 0 else 0.0

# Лекции 5, 6: Объектно-ориентированное программирование
def calculate_average_oop(gradebook: GradeBook, student: Student) -> float:
    return gradebook.policy.calculate_gpa(student.grades)

# Лекция 7: Функциональное программирование (Чистые функции, неизменяемость)
def get_all_grades(student: Student) -> List[float]:
    # Использование reduce для объединения списков
    if not student.grades:
        return []
    return reduce(lambda x, y: x + y, student.grades.values(), [])

def calculate_average_functional(student: Student) -> float:
    grades = get_all_grades(student)
    return sum(grades) / len(grades) if grades else 0.0

# Лекция 8: Функции высшего порядка, map, filter, замыкания
def get_top_students(students: List[Student], threshold: float) -> List[Student]:
    # Замыкание
    def is_above_threshold(student: Student) -> bool:
        return calculate_average_functional(student) >= threshold
    
    # Конвейер обработки данных (filter)
    return sorted(filter(is_above_threshold, students), key=calculate_average_functional, reverse=True)

def generate_group_rating(students: List[Student]) -> List[dict]:
    # Использование map для трансформации
    return list(map(lambda s: {"name": s.name, "avg": calculate_average_functional(s)}, students))

# Лекция 8: Ленивые вычисления (генераторы)
def report_generator(students: List[Student]) -> Generator[str, None, None]:
    for student in students:
        avg = calculate_average_functional(student)
        status = "Допущен" if avg >= 50 else "Не допущен"
        yield f"Студент: {student.name} | Группа: {student.group} | Средний балл: {avg:.2f} | Статус: {status}"
