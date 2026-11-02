# ProductCatalog

> God node · 12 connections · `dependency_inversion/product_catalog_with_dependency_inversion.py`

**Community:** [Dependency Inversion Catalog](Dependency_Inversion_Catalog.md)

## Connections by Relation

### calls
- configure_container() `EXTRACTED`
- test_container_resolves_catalog_with_registered_repository() `EXTRACTED`
- ecommerce_main_application() `EXTRACTED`
- test_catalog_works_with_any_injected_repository() `EXTRACTED`

### contains
- product_catalog_with_dependency_inversion.py `EXTRACTED`

### imports
- product_catalog_with_ioc_container.py `EXTRACTED`
- test_dependency_inversion.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- .list_all_products() `EXTRACTED`

### references
- [Dependency Inversion README (D)](Dependency_Inversion_README_D.md) `EXTRACTED`

### uses
- ecommerce_main_application() `INFERRED`
- test_default_container_uses_sql_repository() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*