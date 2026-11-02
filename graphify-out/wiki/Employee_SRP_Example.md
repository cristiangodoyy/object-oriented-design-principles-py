# Employee SRP Example

> 21 nodes

## Key Concepts

- **Employee** (11 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **test_single_responsibility.py** (9 connections) — `tests/unit/test_single_responsibility.py`
- **test_tax_calculator_depends_on_employee_type()** (7 connections) — `tests/unit/test_single_responsibility.py`
- **employee_example_with_single_responsibility.py** (6 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **test_repository_saves_employee()** (6 connections) — `tests/unit/test_single_responsibility.py`
- **EmployeeRepository** (5 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **TaxCalculator** (5 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **employee()** (5 connections) — `tests/unit/test_single_responsibility.py`
- **.save()** (3 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **.calculate_tax()** (3 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **test_employee_only_holds_data()** (3 connections) — `tests/unit/test_single_responsibility.py`
- **CaptureFixture** (2 connections)
- **.__init__()** (2 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **fixture** (1 connections)
- **EmployeeType** (1 connections)
- **Employee example that applies the Single Responsibility Principle. Each class…** (1 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **Core employee profile data. Responsibility: only handle core employee profile…** (1 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **Persistence of employees. Responsibility: only dealing with database…** (1 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **Tax calculation of employees. Responsibility: only dealing with calculate tax.…** (1 connections) — `single_responsibility/employee_example_with_single_responsibility.py`
- **EmployeeType** (1 connections)
- **parametrize** (1 connections)

## Relationships

- [Employee SRP Before](Employee_SRP_Before.md) (1 shared connections)
- [Project Docs and AI Context](Project_Docs_and_AI_Context.md) (1 shared connections)
- [Test Suite and Docs Sync](Test_Suite_and_Docs_Sync.md) (1 shared connections)

## Source Files

- `single_responsibility/employee_example_with_single_responsibility.py`
- `tests/unit/test_single_responsibility.py`

## Audit Trail

- EXTRACTED: 33 (85%)
- INFERRED: 6 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*