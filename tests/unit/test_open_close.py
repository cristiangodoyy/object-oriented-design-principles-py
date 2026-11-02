import pytest

from open_close.student_example_with_open_close import (
    DiscountCalculator,
    StudentProfile,
)

pytestmark = pytest.mark.unit


class ScholarshipStudent(StudentProfile):
    """New profile defined outside the module: extension, not modification."""

    def has_discount(self) -> bool:
        return True


class FullFeeStudent(StudentProfile):
    def has_discount(self) -> bool:
        return False


@pytest.mark.parametrize(
    ("student", "expected"),
    [(ScholarshipStudent(), 20), (FullFeeStudent(), 0)],
)
def test_new_profiles_work_without_modifying_the_calculator(
    student: StudentProfile, expected: int
) -> None:
    assert (
        DiscountCalculator.calculate_discount_percentage(student) == expected
    )
