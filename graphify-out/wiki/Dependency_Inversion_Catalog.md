# Dependency Inversion Catalog

> 34 nodes

## Key Concepts

- **ProductCatalog** (12 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **product_catalog_with_ioc_container.py** (11 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **test_dependency_inversion.py** (11 connections) — `tests/unit/test_dependency_inversion.py`
- **ProductRepository** (10 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **configure_container()** (10 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **Container** (10 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **product_catalog_with_dependency_inversion.py** (8 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **SQLProductRepository** (6 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **test_container_resolves_catalog_with_registered_repository()** (6 connections) — `tests/unit/test_dependency_inversion.py`
- **.resolve()** (5 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **ecommerce_main_application()** (5 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **InMemoryProductRepository** (5 connections) — `tests/unit/test_dependency_inversion.py`
- **ecommerce_main_application()** (4 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **.register()** (4 connections) — `dependency_inversion/product_catalog_with_ioc_container.py`
- **.__init__()** (3 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **test_catalog_works_with_any_injected_repository()** (3 connections) — `tests/unit/test_dependency_inversion.py`
- **test_default_container_uses_sql_repository()** (3 connections) — `tests/unit/test_dependency_inversion.py`
- **.get_all_product_names()** (2 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **ABC** (2 connections)
- **T** (2 connections)
- **collections_abc** (1 connections)
- **.list_all_products()** (1 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **Product catalog that applies the Dependency Inversion Principle.…** (1 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **Return the names of all products.** (1 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- **Receive the repository to use. We don't want the ProductCatalog to worry about…** (1 connections) — `dependency_inversion/product_catalog_with_dependency_inversion.py`
- *... and 9 more nodes in this community*

## Relationships

- [Project Docs and AI Context](Project_Docs_and_AI_Context.md) (2 shared connections)
- [Employee SRP Before](Employee_SRP_Before.md) (1 shared connections)
- [Test Suite and Docs Sync](Test_Suite_and_Docs_Sync.md) (1 shared connections)

## Source Files

- `dependency_inversion/product_catalog_with_dependency_inversion.py`
- `dependency_inversion/product_catalog_with_ioc_container.py`
- `tests/unit/test_dependency_inversion.py`

## Audit Trail

- EXTRACTED: 60 (86%)
- INFERRED: 10 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*