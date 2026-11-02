import pytest

from single_responsibility.employee_example_with_single_responsibility import (
    Employee,
    EmployeeRepository,
    EmployeeType,
    TaxCalculator,
)

pytestmark = pytest.mark.unit


@pytest.fixture
def employee() -> Employee:
    return Employee(1, "Ana", "Lagos 4567", "contract")


def test_employee_only_holds_data(employee: Employee) -> None:
    assert not hasattr(employee, "save")
    assert not hasattr(employee, "calculate_tax")


def test_repository_saves_employee(
    employee: Employee, capsys: pytest.CaptureFixture[str]
) -> None:
    EmployeeRepository.save(employee)

    assert "Saving employee" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("employee_type", "expected"),
    [
        ("full_time", "Tax calc for full time employee"),
        ("contract", "Tax calc for contractors"),
    ],
)
def test_tax_calculator_depends_on_employee_type(
    employee_type: EmployeeType,
    expected: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    employee = Employee(1, "Ana", "Lagos 4567", employee_type)

    TaxCalculator.calculate_tax(employee)

    assert expected in capsys.readouterr().out
