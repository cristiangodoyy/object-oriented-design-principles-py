# Dependency Graph

## Most Imported Files (change these carefully)

- `dependency_inversion/product_catalog_with_dependency_inversion.py` — imported by **2** files
- `dependency_inversion/product_catalog_with_ioc_container.py` — imported by **1** files
- `interface_segregation/printer_example_with_interface_segregation.py` — imported by **1** files
- `open_close/student_example_with_open_close.py` — imported by **1** files
- `single_responsibility/employee_example_with_single_responsibility.py` — imported by **1** files
- `substitution/product_example_with_substitution.py` — imported by **1** files

## Import Map (who imports what)

- `dependency_inversion/product_catalog_with_dependency_inversion.py` ← `dependency_inversion/product_catalog_with_ioc_container.py`, `tests/unit/test_dependency_inversion.py`
- `dependency_inversion/product_catalog_with_ioc_container.py` ← `tests/unit/test_dependency_inversion.py`
- `interface_segregation/printer_example_with_interface_segregation.py` ← `tests/unit/test_interface_segregation.py`
- `open_close/student_example_with_open_close.py` ← `tests/unit/test_open_close.py`
- `single_responsibility/employee_example_with_single_responsibility.py` ← `tests/unit/test_single_responsibility.py`
- `substitution/product_example_with_substitution.py` ← `tests/unit/test_substitution.py`
