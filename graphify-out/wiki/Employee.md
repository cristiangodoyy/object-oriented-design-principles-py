# Employee

> God node · 11 connections · `single_responsibility/employee_example_with_single_responsibility.py`

**Community:** [Employee SRP Example](Employee_SRP_Example.md)

## Connections by Relation

### contains
- employee_example_with_single_responsibility.py `EXTRACTED`

### imports
- test_single_responsibility.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Core employee profile data. Responsibility: only handle core employee profile… `EXTRACTED`

### references
- Single Responsibility README (S) `EXTRACTED`
- .save() `EXTRACTED`
- .calculate_tax() `EXTRACTED`

### uses
- test_tax_calculator_depends_on_employee_type() `INFERRED`
- test_repository_saves_employee() `INFERRED`
- employee() `INFERRED`
- test_employee_only_holds_data() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*