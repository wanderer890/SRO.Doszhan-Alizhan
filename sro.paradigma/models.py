from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Student:
    id: int
    name: str
    group: str
    grades: Dict[str, List[float]] = field(default_factory=dict)

class GradingPolicy(ABC):
    @abstractmethod
    def calculate_gpa(self, grades: Dict[str, List[float]]) -> float:
        pass

class WeightedPolicy(GradingPolicy):
    def calculate_gpa(self, grades: Dict[str, List[float]]) -> float:
        if not grades: return 0.0
        total, count = 0, 0
        for subj, g_list in grades.items():
            if g_list:
                total += sum(g_list) / len(g_list)
                count += 1
        return round(total / count, 2) if count > 0 else 0.0

class BestAttemptPolicy(GradingPolicy):
    def calculate_gpa(self, grades: Dict[str, List[float]]) -> float:
        if not grades: return 0.0
        total, count = 0, 0
        for subj, g_list in grades.items():
            if g_list:
                total += max(g_list)
                count += 1
        return round(total / count, 2) if count > 0 else 0.0

class GradeBook:
    def __init__(self, policy: GradingPolicy):
        self._students: List[Student] = []
        self.policy = policy

    def add_student(self, student: Student):
        self._students.append(student)

    def get_students(self) -> List[Student]:
        return self._students
