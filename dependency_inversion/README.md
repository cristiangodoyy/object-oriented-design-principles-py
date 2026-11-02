# D — Inversión de dependencias (Dependency Inversion)

> Los módulos de alto nivel no dependen de los de bajo nivel: **ambos dependen
> de abstracciones**. Las abstracciones no dependen de los detalles; los
> detalles dependen de las abstracciones.

![Módulos de alto y bajo nivel](high_low_level_modules.png)

## Archivos (en orden de lectura)

| # | Archivo | Rol |
| --- | --- | --- |
| 1 | [product_catalog_before_dependency_inversion.py](product_catalog_before_dependency_inversion.py) | Violación: `ProductCatalog` crea `SQLProductRepository()` directamente. |
| 2 | [product_catalog_with_factory.py](product_catalog_with_factory.py) | Paso intermedio: aparece la abstracción `ProductRepository`, pero `ProductCatalog` sigue llamando a una fábrica desde adentro. |
| 3 | [product_catalog_with_dependency_inversion.py](product_catalog_with_dependency_inversion.py) | **Solución a seguir:** la dependencia se **inyecta** por el constructor, tipada con la abstracción. |
| 4 | [product_catalog_with_ioc_container.py](product_catalog_with_ioc_container.py) | Extra: qué es IoC y un contenedor mínimo que arma `ProductCatalog` fuera del flujo principal. |
| — | [test_dependency_inversion.py](../tests/unit/test_dependency_inversion.py) | Test: se inyecta un repositorio en memoria sin tocar `ProductCatalog`, directamente y desde el contenedor. |

```bash
uv run python -m dependency_inversion.product_catalog_before_dependency_inversion
uv run python -m dependency_inversion.product_catalog_with_factory
uv run python -m dependency_inversion.product_catalog_with_dependency_inversion
uv run python -m dependency_inversion.product_catalog_with_ioc_container
```

Los cuatro imprimen `All products names: ['jean', 'shirt']`.

## El problema (antes)

```text
ProductCatalog (alto nivel) ──▶ SQLProductRepository (bajo nivel)
```

La regla de negocio ("listar productos") queda atada a un detalle técnico (SQL).
Cambiar de base de datos o testear sin una BD real obliga a modificar
`ProductCatalog`.

## La solución

```text
ProductCatalog (alto nivel) ──▶ ProductRepository (abstracción) ◀── SQLProductRepository (bajo nivel)
```

La solución tiene tres piezas:

1. **Abstracción:** `ProductRepository` define `get_all_product_names()`.
2. **Detalle:** `SQLProductRepository` implementa la abstracción.
3. **Inyección:** el código de arranque (`ecommerce_main_application`) crea el
   repositorio concreto y se lo pasa a `ProductCatalog`, que solo lo usa.

```python
class ProductCatalog:  # high level class
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def list_all_products(self) -> list[str]:
        return self._product_repository.get_all_product_names()


product_catalog = ProductCatalog(product_repository=SQLProductRepository())
```

## Inyección de dependencias vs. inversión de control

| Concepto | Quién crea e inyecta la dependencia | En este repo |
| --- | --- | --- |
| Inyección de dependencias (DI) | Tu propio código, en la *composition root* | `product_catalog_with_dependency_inversion.py` |
| Inversión de control (IoC) | Un contenedor o framework (Spring en Java; `dependency-injector` o FastAPI `Depends` en Python) | `product_catalog_with_ioc_container.py`, con un `Container` propio de unas 20 líneas |

Con IoC, la configuración (`configure_container`) registra cómo se construye
cada abstracción, y el flujo principal solo pide lo que necesita:

```python
container = configure_container()
product_catalog = container.resolve(ProductCatalog)
```

En Python, la DI manual por constructor suele ser suficiente. Usá un
contenedor solo cuando el grafo de dependencias sea grande.

## Patrón para reutilizar

1. Definí la abstracción (`Protocol` o `ABC`) con los métodos que necesita el
   módulo de alto nivel.
2. Hacé que la implementación concreta cumpla esa abstracción.
3. Recibí la dependencia por el constructor, **tipada con la abstracción**.
4. Creá y conectá los objetos concretos en un único lugar (`main()` o el
   arranque de la app).
5. En los tests, inyectá una implementación en memoria.

Plantilla tipada con test: [PATTERNS.md → D](../PATTERNS.md#d--inversión-de-dependencias-dependency-inversion).

## Simplificaciones del ejemplo

- `product_catalog_with_factory.py` es un **paso intermedio**: `ProductCatalog`
  llama a `ProductFactory` desde adentro y sigue acoplado a la fábrica (y, a
  través de ella, a SQL). No lo copies: seguí
  `product_catalog_with_dependency_inversion.py`.
- `SQLProductRepository` devuelve una lista fija en lugar de consultar una
  base de datos.
- El `Container` del ejemplo IoC no resuelve dependencias automáticamente ni
  maneja ciclos de vida (singleton, por request). Para eso existen librerías
  como `dependency-injector`.
- mypy rechaza pasar una ABC donde se espera `type[T]` (mypy#4717), aunque es
  Python válido. Por eso `pyproject.toml` desactiva el código `type-abstract`.

## Notas originales

### Dependecy inversion

- High Level class should not depend on Low Level class. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.
- High level class and dependents class should be decoupled with an abstraction layer in between.

### Advantages

- The tight coupling of classes is no more prevalent and hence no complexity/rigidity in the system.
- As there is a clear abstraction layer between dependent classes(provided by a hook or parameter),
it's easy to deal(tratar) with dependencies across classes in a better way.

### Coupling

Is level of dependency between software component.
