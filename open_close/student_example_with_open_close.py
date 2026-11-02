"""Discount calculator that applies the Open/Closed Principle.

We get robust designs that are easy to extend in future.
"""

import random

from abc import ABC, abstractmethod


class StudentProfile(ABC):
    """Common interface class."""

    @abstractmethod
    def has_discount(self) -> bool:
        """Tell whether the student has a discount."""


class DiscountCalculator:
    """Calculator closed for modification.

    We did not have to change any other class to handle discount percentage.
    Adding to the software component, should not have to modify existing
    code. Adding a new type of Student, not modify the code of
    calculate_discount_percentage.
    """

    @staticmethod
    def calculate_discount_percentage(student: StudentProfile) -> int:
        if student.has_discount():
            return 20
        return 0


class UniversityStudent(StudentProfile):
    def has_discount(self) -> bool:
        return random.choice([True, False])


class HighSchoolStudent(StudentProfile):
    def has_discount(self) -> bool:
        return random.choice([True, False])


class ElementarySchoolStudent(StudentProfile):
    """New feature added by extension.

    A software component(class, module, method) should be extendable to add a
    new feature or to add a new behavior to it.
    This is the new feature: ElementarySchoolStudent that implement the
    StudentProfile interface.
    """

    def has_discount(self) -> bool:
        return random.choice([True, False])


if __name__ == "__main__":
    students: list[StudentProfile] = [
        UniversityStudent(),
        HighSchoolStudent(),
        ElementarySchoolStudent(),
    ]
    for student in students:
        discount = DiscountCalculator.calculate_discount_percentage(student)
        print(f"{type(student).__name__} percentage discount: {discount}")
