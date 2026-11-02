# Principios de diseño orientado a objetos (SOLID) en Python

Repositorio de referencia con ejemplos mínimos y ejecutables de los cinco
principios SOLID. Cada principio tiene una versión **antes** (que lo viola) y
una versión **después** (que lo aplica), para que otros proyectos puedan
reconocer el problema y copiar la solución.

- **¿Querés las reglas y plantillas para tu proyecto?** Leé
  [PATTERNS.md](PATTERNS.md).
- **¿Querés entender el razonamiento?** Recorré las carpetas en el orden de
  la tabla.

## Mapa del repositorio

| Principio | Carpeta | Antes (violación) | Después (solución) |
| --- | --- | --- | --- |
| **S** Responsabilidad única | [single_responsibility/](single_responsibility/README.md) | [employee_example_before_single_responsibility.py](single_responsibility/employee_example_before_single_responsibility.py) | [employee_example_with_single_responsibility.py](single_responsibility/employee_example_with_single_responsibility.py) |
| **O** Abierto/Cerrado | [open_close/](open_close/README.md) | [student_example_before_open_close.py](open_close/student_example_before_open_close.py) | [student_example_with_open_close.py](open_close/student_example_with_open_close.py) |
| **L** Sustitución de Liskov | [substitution/](substitution/README.md) | [product_example_before_substitution.py](substitution/product_example_before_substitution.py) | [product_example_with_substitution.py](substitution/product_example_with_substitution.py) |
| **I** Segregación de interfaces | [interface_segregation/](interface_segregation/README.md) | [printer_example_before_interface_segregation.py](interface_segregation/printer_example_before_interface_segregation.py) | [printer_example_with_interface_segregation.py](interface_segregation/printer_example_with_interface_segregation.py) |
| **D** Inversión de dependencias | [dependency_inversion/](dependency_inversion/README.md) | [product_catalog_before_dependency_inversion.py](dependency_inversion/product_catalog_before_dependency_inversion.py) | [product_catalog_with_dependency_inversion.py](dependency_inversion/product_catalog_with_dependency_inversion.py) (pasos extra: [con fábrica](dependency_inversion/product_catalog_with_factory.py) y [con contenedor IoC](dependency_inversion/product_catalog_with_ioc_container.py)) |

Cada carpeta tiene un `README.md` con: la idea del principio, el problema, la
solución, el patrón para reutilizar, advertencias sobre las simplificaciones
del ejemplo y un link a su test.

> **Nombres de archivo.** Todos siguen el esquema
> `<ejemplo>_before_<principio>.py` / `<ejemplo>_with_<principio>.py`. Si
> tenés links a nombres anteriores: `student_example_*_single_responsibility`
> pasó a ser `employee_example_*`, `printer_example_before.py` pasó a ser
> `printer_example_before_interface_segregation.py`, y en
> `dependency_inversion/` el antiguo `dependency_injection.py` es ahora
> `product_catalog_with_dependency_inversion.py` (el paso intermedio quedó
> como `product_catalog_with_factory.py` e `inversion_of_control.py` pasó a
> ser `product_catalog_with_ioc_container.py`).

## Cómo ejecutar los ejemplos

Requisitos: Python ≥ 3.12 y [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run python -m single_responsibility.employee_example_with_single_responsibility
uv run python -m open_close.student_example_with_open_close
uv run python -m substitution.product_example_with_substitution
uv run python -m dependency_inversion.product_catalog_with_dependency_inversion
```

Todos los módulos se ejecutan como `uv run python -m <carpeta>.<archivo>`
(sin `.py`). Los ejemplos de `interface_segregation` solo definen clases y no
imprimen nada.

## Tests y validación

Los tests de [tests/unit/](tests/unit/) son la versión ejecutable de la guía:

- Un archivo por principio, que demuestra su beneficio. Por ejemplo, en
  [test_dependency_inversion.py](tests/unit/test_dependency_inversion.py) se
  inyecta un repositorio en memoria sin tocar `ProductCatalog`.
- [test_examples_run.py](tests/unit/test_examples_run.py) ejecuta todos los
  ejemplos como scripts.
- [test_patterns_snippets.py](tests/unit/test_patterns_snippets.py) ejecuta
  las plantillas de `PATTERNS.md`, para que la guía no quede desactualizada.
- [test_docs_in_sync.py](tests/unit/test_docs_in_sync.py) verifica que cada
  ejemplo y cada clase estén documentados en su README y en este mapa, y que
  las plantillas de `PATTERNS.md` no usen nombres como `id` o `type`.

### Documentación sincronizada automáticamente

Si cambiás o agregás una clase sin actualizar la documentación:

- **Al hacer commit:** pre-commit corre `test_docs_in_sync.py` y frena el
  commit, con un mensaje que dice qué README falta actualizar. También
  regenera el mapa de codesight.
- **Si el cambio lo hace Claude Code:** el hook de
  [.claude/settings.json](.claude/settings.json) corre el mismo test después
  de cada edición. Si falla, Claude recibe el error y actualiza la
  documentación en ese mismo turno. Podés revisarlo o desactivarlo con
  `/hooks`.

```bash
uv run pytest -q                  # tests
uv run ruff check .               # lint
uv run ruff format --check .      # formato
uv run mypy .                     # tipos (modo strict)
uv run pre-commit install         # una vez: corre ruff y mypy en cada commit
uv run pre-commit run --all-files
```

## Cómo usar este repositorio desde otro proyecto

1. Copiá o enlazá [PATTERNS.md](PATTERNS.md) en tu proyecto.
2. Referencialo en las instrucciones para agentes (`CLAUDE.md`, `AGENTS.md`,
   `.cursorrules`) para que el código generado siga estos patrones.
3. Usá la lista de revisión de `PATTERNS.md` en los code reviews.

## Conceptos generales

### SOLID

- When these principles are applied together, a developer is more likely to create a system
that is easy to maintain and expand over time.
- SOLID principles are all intertwined(entrelazados) and interdependent.
- They are most effective when they are combined together.
- It is important that you get a wholesome view of all the SOLID principles.
- Single responsibility, Open-closed, Liskov substitution, Interface segregation and Dependency inversion

### Caution

- Do not follow the open-closed Principle blindly(ciegamente).
- You will end up with a huge(gran) number of classes that can complicate your overall(general) design.
- Make a subjective, rather than an objective decision, to decide when and where to apply the Open Closed Principle
to your design.

### Cohesion

Is the degree to which the various parts of a software component are
related.

### Coupling

Is level of dependency between software component.

### Software components

- Can be classes, methods, packages, modules.

### Dependecy inversion

- High Level class should not depend on Low Level class. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.
- High level class and dependents class should be decoupled with an abstraction layer in between.

### Inyeccion de dependencias (en ingles Dependency Injection, DI)

- Es un patrón en el que se suministran objetos
a una clase en lugar de ser la propia clase la que cree dichos objetos.
