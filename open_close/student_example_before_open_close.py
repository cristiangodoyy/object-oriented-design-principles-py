"""Discount calculator that violates the Open/Closed Principle.

DiscountCalculator is NOT closed for modification: it knows every type of
student and decides the discount with an if chain over student_type.

Every time a new type of student appears, we have to open
calculate_discount_percentage and add a new branch, modifying code that
already worked and was already tested. That is the violation of the
principle as seen in code.

The definition gives us the guidance to fix it: the calculator should be
open for extension (new types of student) but closed for modification.
"""

import random


class Student:
    """Student without behavior of its own.

    There is no common interface: the type of student is only a string, so
    the behavior of each type has to live somewhere else (in the calculator).
    """

    def __init__(self, name: str, student_type: str) -> None:
        self.name = name
        self.student_type = student_type


class DiscountCalculator:
    """Calculator that knows every type of student.

    Reasons to change:
        1. A change in the discount rule of university students.
        2. A change in the discount rule of high school students.
        3. A change in the discount rule of elementary school students.
        4. A new type of student. -> We have to modify this class every time.
    """

    @staticmethod
    def calculate_discount_percentage(student: Student) -> int:
        if student.student_type == "university":
            return 20 if random.choice([True, False]) else 0

        if student.student_type == "high_school":
            return 20 if random.choice([True, False]) else 0

        # New feature: to support elementary school students we had to
        # MODIFY this method, which already worked and was already tested.
        # The chances of regression are higher.
        if student.student_type == "elementary_school":
            return 20 if random.choice([True, False]) else 0

        return 0


if __name__ == "__main__":
    students = [
        Student("Ana", "university"),
        Student("Juan", "high_school"),
        Student("Sofia", "elementary_school"),
    ]
    for student in students:
        discount = DiscountCalculator.calculate_discount_percentage(student)
        print(f"{student.student_type} percentage discount: {discount}")
