# Libraries

> **Navigation aid.** Library inventory extracted via AST. Read the source files listed here before modifying exported functions.

**12 library files** across 5 modules

## Dependency_inversion (4 files)

- `dependency_inversion/product_catalog_with_dependency_inversion.py` — ecommerce_main_application, ProductRepository, SQLProductRepository, ProductCatalog
- `dependency_inversion/product_catalog_with_factory.py` — ProductRepository, SQLProductRepository, ProductFactory, ProductCatalog
- `dependency_inversion/product_catalog_with_ioc_container.py` — configure_container, ecommerce_main_application, Container
- `dependency_inversion/product_catalog_before_dependency_inversion.py` — SQLProductRepository, ProductCatalog

## Interface_segregation (2 files)

- `interface_segregation/printer_example_with_interface_segregation.py` — Print, Scan, Fax, XeroxWorkCentre, HPPrinterScanner, CannonPrinter
- `interface_segregation/printer_example_before_interface_segregation.py` — Multifunction, CannonPrinter, HPPrinterScanner, XeroxWorkCentre

## Open_close (2 files)

- `open_close/student_example_with_open_close.py` — StudentProfile, DiscountCalculator, UniversityStudent, HighSchoolStudent, ElementarySchoolStudent
- `open_close/student_example_before_open_close.py` — Student, DiscountCalculator

## Single_responsibility (2 files)

- `single_responsibility/employee_example_with_single_responsibility.py` — Employee, EmployeeRepository, TaxCalculator
- `single_responsibility/employee_example_before_single_responsibility.py` — knows, Employee

## Substitution (2 files)

- `substitution/product_example_before_substitution.py` — client, Product, InHouseProduct, InCommerceProduct
- `substitution/product_example_with_substitution.py` — client, Product, InHouseProduct, InCommerceProduct

---
_Back to [overview.md](./overview.md)_