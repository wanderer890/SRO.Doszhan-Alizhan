import json
import random
from models import Student, GradeBook, WeightedPolicy, BestAttemptPolicy
from logic import report_generator, get_top_students, calculate_average_procedural, calculate_average_functional, calculate_average_oop

def generate_mock_data() -> List[Student]:
    students = []
    names = ["Алижан", "Аружан", "Дамир", "Санжар", "Динара", "Азамат", "Мадина", "Тимур", "Айгерим", "Руслан"]
    groups = ["ТИИ25-21", "ТИИ25-22"]
    
    for i in range(1, 21):
        name = names[i % len(names)] + f" {i}"
        group = groups[i % len(groups)]
        grades = {
            "Машинное обучение": [random.randint(50, 100) for _ in range(3)],
            "Алгоритмы ИИ": [random.randint(50, 100) for _ in range(2)],
            "Программирование Python": [random.randint(60, 100) for _ in range(4)]
        }
        students.append(Student(i, name, group, grades))
        
    # Внедрение конкретных данных
    students[0].name = "Досжан Алижан"
    students[0].group = "ТИИ25-21"
    
    return students

def cli_menu():
    policy = WeightedPolicy()
    gradebook = GradeBook(policy)
    
    # Загрузка данных
    for student in generate_mock_data():
        gradebook.add_student(student)
        
    while True:
        print("\n=== Аналитическая система успеваемости студентов ===")
        print("1. Показать отчет по всем студентам (Генератор)")
        print("2. Рейтинг группы (Топ студенты)")
        print("3. Сравнение парадигм (Процедурная vs ООП vs Функциональная)")
        print("4. Сменить политику оценивания (Weighted -> BestAttempt)")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            print("\n--- Отчет ---")
            for line in report_generator(gradebook.get_students()):
                print(line)
        elif choice == '2':
            threshold = float(input("Введите порог среднего балла (например, 75): "))
            top = get_top_students(gradebook.get_students(), threshold)
            print("\n--- Топ студенты ---")
            for s in top:
                print(f"{s.name} - {calculate_average_functional(s):.2f}")
        elif choice == '3':
            student = gradebook.get_students()[0]
            print(f"\n--- Сравнение для студента {student.name} ---")
            print(f"Процедурный подход (все оценки): {calculate_average_procedural(student):.2f}")
            print(f"ООП подход (текущая политика): {calculate_average_oop(gradebook, student):.2f}")
            print(f"Функциональный подход (чистая функция): {calculate_average_functional(student):.2f}")
        elif choice == '4':
            gradebook.policy = BestAttemptPolicy()
            print("Политика изменена на 'Лучшая попытка'.")
        elif choice == '5':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    cli_menu()
