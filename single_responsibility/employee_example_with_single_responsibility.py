"""Employee example that applies the Single Responsibility Principle.

Each class has only one responsibility.
High Cohesion: each class groups only what is related to its own task.
Loose coupling: Employee does not know EmployeeRepository nor
TaxCalculator. Whoever needs to save or calculate uses them directly.
"""

from typing import Literal

EmployeeType = Literal["full_time", "contract"]


class Employee:
    """Core employee profile data.

    Responsibility: only handle core employee profile data.
    Reasons to change:
        1. A change in the employee id format.
        2. A change in the employee name format.
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


class EmployeeRepository:
    """Persistence of employees.

    Responsibility: only dealing with database operations.
    Reasons to change:
        1. A change in the database layer.
    We have removed the tight coupling and made it loose.
    So now if we change the underlying database, the Employee class does NOT
    need to get changed. You only need to change the Repository class.
    """

    @staticmethod
    def save(employee: Employee) -> None:
        print(f"Saving employee: {employee.__dict__} in database")


class TaxCalculator:
    """Tax calculation of employees.

    Responsibility: only dealing with calculate tax.
    Reasons to change:
        1. A change in the tax rules.
    We have removed the tight coupling and made it loose.
    So now if we change the underlying calculate_tax, the Employee class does
    NOT need to get changed. You only need to change the TaxCalculator class.
    """

    @staticmethod
    def calculate_tax(employee: Employee) -> None:
        print(f"Tax calc for employee: {employee.__dict__}")
        if employee.employee_type == "full_time":
            print("Tax calc for full time employee")

        if employee.employee_type == "contract":
            print("Tax calc for contractors")


if __name__ == "__main__":
    employee = Employee(31890233, "Cristian", "Lagos 4567", "full_time")
    # The caller uses each specialized class directly: Employee only holds
    # data and does not know how it is saved or how its tax is calculated.
    EmployeeRepository.save(employee)
    TaxCalculator.calculate_tax(employee)
