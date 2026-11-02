"""Employee class that violates the Single Responsibility Principle.

Employee class is coupled with the database layer because the Employee
class knows the low level details related to dealing(manejo) with the
database layer and the calculate tax layer.
Tight(estrecho,ajustado) coupling is an undesirable feature in software.
"""

from typing import Literal

EmployeeType = Literal["full_time", "contract"]


class Employee:
    """Employee with too many responsibilities.

    Responsibilities:
        1. handle core employee profile data.
        2. dealing with database operations. -> The Employee class should
        NOT be made cognizant of the low level details related to dealing
        with database layer.
        3. dealing with calculate tax -> The Employee class should NOT be
        made cognizant of the low level details related to calculate tax.

    Reasons to change:
        1. A change in the employee id format.
        2. A change in the employee name format.
        3. A change in the database layer.
        4. A change in the calculate tax.
    """

    def __init__(
        self,
        employee_id: int,
        name: str,
        address: str,
        employee_type: EmployeeType,
    ) -> None:
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.employee_type = employee_type

    def save(self) -> None:
        """Save the employee in the database.

        Employee class is tightly coupled with the database layer because
        the Employee class knows the low level details related to the
        database layer.
        """
        print(f"Saving employee: {self.__dict__} in database")

    def calculate_tax(self) -> None:
        """Calculate the tax of the employee.

        Employee class is tightly coupled with the calculate tax because the
        Employee class is made cognizant of the low level details related to
        calculate tax.
        """
        print(f"Tax calc for employee: {self.__dict__}")
        if self.employee_type == "full_time":
            print("Tax calc for full time employee")

        if self.employee_type == "contract":
            print("Tax calc for contractors")


if __name__ == "__main__":
    employee = Employee(31890233, "Cristian", "Lagos 4567", "full_time")
    employee.save()
    employee.calculate_tax()
