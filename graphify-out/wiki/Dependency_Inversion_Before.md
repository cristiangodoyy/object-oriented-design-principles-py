# Dependency Inversion Before

> 7 nodes

## Key Concepts

- **ProductCatalog** (4 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **product_catalog_before_dependency_inversion.py** (3 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **SQLProductRepository** (3 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **.list_all_products()** (2 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **Product catalog that violates the Dependency Inversion Principle.…** (1 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **ProductCatalog directly depends on SQLProductRepository.** (1 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`
- **.get_all_product_names()** (1 connections) — `dependency_inversion/product_catalog_before_dependency_inversion.py`

## Relationships

- [Project Docs and AI Context](Project_Docs_and_AI_Context.md) (1 shared connections)

## Source Files

- `dependency_inversion/product_catalog_before_dependency_inversion.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*