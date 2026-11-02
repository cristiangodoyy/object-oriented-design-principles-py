# Product Factory Pattern

> 15 nodes

## Key Concepts

- **product_catalog_with_factory.py** (6 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **ProductRepository** (5 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **SQLProductRepository** (5 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **ProductCatalog** (4 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **.create_sql_product_repository()** (4 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **.list_all_products()** (2 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **ProductFactory** (2 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **.get_all_product_names()** (2 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **ABC** (2 connections)
- **.get_all_product_names()** (2 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **Intermediate step: abstraction plus a factory. ProductCatalog(high level…** (1 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **Return the names of all products. Abstractions should not depend on details.…** (1 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **Repository backed by SQL. The detail, which is the SQLProductRepository class,…** (1 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **Return the names of all products from SQL. Los detalles(el codigo del metodo)…** (1 connections) — `dependency_inversion/product_catalog_with_factory.py`
- **Catalog that obtains its repository from the factory. Our reference object is…** (1 connections) — `dependency_inversion/product_catalog_with_factory.py`

## Relationships

- [Project Docs and AI Context](Project_Docs_and_AI_Context.md) (1 shared connections)

## Source Files

- `dependency_inversion/product_catalog_with_factory.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*