# Employee SRP Before

> 12 nodes

## Key Concepts

- **Employee** (7 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **employee_example_before_single_responsibility.py** (3 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **typing** (3 connections)
- **.calculate_tax()** (2 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **.__init__()** (2 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **.save()** (2 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **knows (ambiguous AST entity, before SRP)** (1 connections) — `.codesight/CODESIGHT.md`
- **EmployeeType** (1 connections)
- **Employee class that violates the Single Responsibility Principle. Employee…** (1 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **Employee with too many responsibilities. Responsibilities: 1. handle core…** (1 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **Save the employee in the database. Employee class is tightly coupled with the…** (1 connections) — `single_responsibility/employee_example_before_single_responsibility.py`
- **Calculate the tax of the employee. Employee class is tightly coupled with the…** (1 connections) — `single_responsibility/employee_example_before_single_responsibility.py`

## Relationships

- [Project Docs and AI Context](Project_Docs_and_AI_Context.md) (1 shared connections)
- [Dependency Inversion Catalog](Dependency_Inversion_Catalog.md) (1 shared connections)
- [Employee SRP Example](Employee_SRP_Example.md) (1 shared connections)

## Source Files

- `.codesight/CODESIGHT.md`
- `single_responsibility/employee_example_before_single_responsibility.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 1 (7%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*