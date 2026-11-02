# ProductRepository

> God node · 10 connections · `dependency_inversion/product_catalog_with_dependency_inversion.py`

**Community:** [Dependency Inversion Catalog](Dependency_Inversion_Catalog.md)

## Connections by Relation

### contains
- product_catalog_with_dependency_inversion.py `EXTRACTED`

### imports
- product_catalog_with_ioc_container.py `EXTRACTED`
- test_dependency_inversion.py `EXTRACTED`

### inherits
- SQLProductRepository `EXTRACTED`
- InMemoryProductRepository `EXTRACTED`
- ABC `EXTRACTED`

### method
- .get_all_product_names() `EXTRACTED`

### references
- .__init__() `EXTRACTED`

### uses
- configure_container() `INFERRED`
- test_container_resolves_catalog_with_registered_repository() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*