# Guía de patrones SOLID para otros proyectos

Esta guía es la **referencia prescriptiva** del repositorio: dice qué hacer, qué
evitar y trae plantillas listas para copiar. Los ejemplos de cada carpeta
muestran el razonamiento paso a paso (versión "antes" y "después"); este
documento resume las reglas que otros proyectos deben seguir.

> Si solo vas a leer un archivo, lee este.

## Cómo usar esta guía en tu proyecto

1. Copiá este archivo (o enlazalo) en la documentación de tu proyecto.
2. Referencialo desde las instrucciones para agentes de IA (`CLAUDE.md`,
   `AGENTS.md`, `.cursorrules`), por ejemplo:
   `Seguir los patrones de diseño de PATTERNS.md al crear o modificar clases.`
3. Usá la [lista de revisión](#lista-de-revisión-para-code-review) en los
   code reviews.
4. Ante la duda, abrí el ejemplo "antes/después" de la carpeta del principio
   correspondiente para ver el razonamiento completo.

Los tests de [`tests/unit/`](tests/unit/) son la versión ejecutable de esta
guía: hay uno por principio, y
[`test_patterns_snippets.py`](tests/unit/test_patterns_snippets.py) ejecuta
cada plantilla de este documento. Si cambiás una plantilla, corré
`uv run pytest -q`.

## Convenciones generales

Las plantillas siguen estas convenciones (Python ≥ 3.12):

| Tema | Convención |
| --- | --- |
| Contratos de comportamiento | `typing.Protocol` para contratos nuevos (no obliga a heredar). `abc.ABC` + `@abstractmethod` cuando querés que Python impida instanciar una implementación incompleta, o cuando la base comparte código. Los ejemplos del repo usan `ABC`. Las dos opciones son válidas. |
| Dependencias | Se reciben por el constructor (`__init__`), tipadas con la **abstracción**, nunca con la clase concreta. |
| Creación de objetos | En un único lugar, la *composition root* (`main()`, el arranque de la app, una fábrica). Las clases de negocio no hacen `Concreto()`. |
| Tipos | Anotaciones explícitas en métodos públicos. Nada de `Any` sin justificación. |
| Consultas | Un método que devuelve un valor (`get_*`, `calculate_*`) no debe modificar el estado del objeto. |
| Nombres | Las implementaciones concretas llevan en el nombre el detalle que las distingue: `SQLProductRepository`, `InMemoryProductRepository`. |

### Relación entre las plantillas y los ejemplos del repo

Las plantillas usan los **mismos nombres de clases y métodos** que los
ejemplos "después" (por eso podés buscarlos en el repo), pero son la versión
a copiar: corrigen las simplificaciones de demo.

| Principio | Qué cambia en la plantilla respecto del ejemplo |
| --- | --- |
| S | `Employee` es un `dataclass(frozen=True)`, `EmployeeRepository` es un `Protocol` y `TaxCalculator.calculate_tax` **devuelve** el impuesto (el ejemplo imprime y usa `@staticmethod`). |
| O | `Protocol` en lugar de `ABC`, método de instancia en lugar de `@staticmethod` y reglas deterministas en lugar de `random.choice`. Solo se muestran dos perfiles. |
| L | Igual que el ejemplo. |
| I | `Protocol` en lugar de `ABC`. Se omiten `XeroxWorkCentre` (implementa todo) y los cuerpos de marcador `"""Assume real code here."""`. |
| D | `Protocol` en lugar de `ABC` y `main()` en lugar de `ecommerce_main_application()`. |

Cada principio también tiene su sección "Simplificaciones del ejemplo" en el
README de su carpeta.

---

## S — Responsabilidad única (Single Responsibility)

**Regla:** cada clase tiene **una sola razón para cambiar**.

**Señales de que se está violando**

- La clase mezcla datos de dominio con persistencia, cálculos, formato o E/S.
- Para describir qué hace la clase necesitás usar "y".
- Un cambio de base de datos o de reglas impositivas obliga a tocar la
  entidad de dominio.

**Plantilla**

```python
from dataclasses import dataclass
from typing import Literal, Protocol

EmployeeType = Literal["full_time", "contract"]


@dataclass(frozen=True)
class Employee:
    """Responsabilidad: solo los datos del empleado."""

    employee_id: int  # no `id` ni `type`: ocultan funciones built-in
    name: str
    address: str
    employee_type: EmployeeType


class EmployeeRepository(Protocol):
    """Responsabilidad: solo la persistencia."""

    def save(self, employee: Employee) -> None: ...


class TaxCalculator:
    """Responsabilidad: solo el cálculo de impuestos."""

    def calculate_tax(self, employee: Employee) -> float:
        if employee.employee_type == "full_time":
            return 0.30
        return 0.15
```

`Employee` no tiene métodos `save()` ni `calculate_tax()`: quien necesita
guardar o calcular usa `EmployeeRepository` o `TaxCalculator` directamente.

Ejemplo completo: [single_responsibility/](single_responsibility/README.md) ·
Test: [test_single_responsibility.py](tests/unit/test_single_responsibility.py)

---

## O — Abierto/Cerrado (Open/Closed)

**Regla:** para agregar comportamiento, **creás una clase nueva**. No
modificás el código que ya funciona.

**Señales de que se está violando**

- Cadenas `if/elif` o `match` sobre un "tipo"
  (`if student.student_type == "university"`).
- Cada variante nueva obliga a editar la misma función central.

**Plantilla**

```python
from typing import Protocol


class StudentProfile(Protocol):
    def has_discount(self) -> bool: ...


class DiscountCalculator:
    """Cerrada para modificación: no cambia al aparecer perfiles nuevos."""

    def calculate_discount_percentage(self, student: StudentProfile) -> int:
        return 20 if student.has_discount() else 0


class UniversityStudent:
    def has_discount(self) -> bool:
        return False


class ElementarySchoolStudent:
    """Extensión: comportamiento nuevo sin tocar DiscountCalculator."""

    def has_discount(self) -> bool:
        return True
```

**Precaución:** no apliques este principio a ciegas. Una abstracción por cada
posible variación termina en un exceso de clases. Abstraé cuando la variación
es real o muy probable.

Ejemplo completo: [open_close/](open_close/README.md) ·
Test: [test_open_close.py](tests/unit/test_open_close.py)

---

## L — Sustitución de Liskov (Liskov Substitution)

**Regla:** cualquier subtipo tiene que poder usarse donde se espera el tipo
base **sin que el cliente pregunte cuál es**.

**Señales de que se está violando**

- `isinstance(obj, SubclaseConcreta)` en el código cliente para decidir qué
  llamar.
- Subclases que agregan métodos públicos que el cliente está obligado a llamar.
- Subclases que lanzan `NotImplementedError` en métodos heredados.

**Solución: "Tell, Don't Ask".** El cliente le pide un resultado al objeto
("decime tu descuento") y cada subtipo resuelve internamente cómo calcularlo.

**Plantilla**

```python
class Product:
    BASE_DISCOUNT: float = 10

    def get_discount(self) -> float:
        return self.BASE_DISCOUNT


class InHouseProduct(Product):
    EXTRA_DISCOUNT: float = 0.5
    BITCOIN_DISCOUNT: float = 2

    def get_discount(self) -> float:
        # Calcula sin mutar estado: llamar dos veces devuelve lo mismo.
        return (
            super().get_discount()
            + self.EXTRA_DISCOUNT
            + self.BITCOIN_DISCOUNT
        )


class InCommerceProduct(Product):
    EXTRA_DISCOUNT: float = 1

    def get_discount(self) -> float:
        return super().get_discount() + self.EXTRA_DISCOUNT


def client(products: list[Product]) -> None:
    for product in products:  # sin isinstance
        print(product.get_discount())
```

Ejemplo completo: [substitution/](substitution/README.md) ·
Test: [test_substitution.py](tests/unit/test_substitution.py)

---

## I — Segregación de interfaces (Interface Segregation)

**Regla:** ninguna clase debe estar obligada a implementar métodos que no usa.
Preferí **varias interfaces pequeñas y cohesivas** antes que una grande.

**Señales de que se está violando**

- Implementaciones con métodos vacíos, `pass` o `raise NotImplementedError`
  solo para cumplir el contrato.
- Una interfaz que agrupa capacidades independientes (imprimir, escanear,
  enviar fax).

**Plantilla**

```python
from typing import Protocol


class Print(Protocol):
    def print(self, document: str) -> None: ...

    def get_print_spool_details(self) -> str: ...


class Scan(Protocol):
    def scan(self) -> bytes: ...

    def scan_photo(self) -> bytes: ...


class Fax(Protocol):
    def fax(self, number: str, document: str) -> None: ...

    def internet_fax(self, email: str, document: str) -> None: ...


class HPPrinterScanner:
    """Implementa solo Print y Scan. No sabe nada de Fax."""

    def print(self, document: str) -> None: ...

    def get_print_spool_details(self) -> str:
        return ""

    def scan(self) -> bytes:
        return b""

    def scan_photo(self) -> bytes:
        return b""


class CannonPrinter:
    """Implementa solo Print."""

    def print(self, document: str) -> None: ...

    def get_print_spool_details(self) -> str:
        return ""


def print_report(printer: Print) -> None:
    """El cliente pide solo la capacidad que necesita."""
    printer.print("report")


print_report(CannonPrinter())
```

En el ejemplo del repo las tres interfaces son `ABC` y hay una cuarta clase,
`XeroxWorkCentre(Print, Scan, Fax)`, que sí implementa todo.

Ejemplo completo: [interface_segregation/](interface_segregation/README.md) ·
Test: [test_interface_segregation.py](tests/unit/test_interface_segregation.py)

---

## D — Inversión de dependencias (Dependency Inversion)

**Regla:** los módulos de alto nivel (reglas de negocio) y los de bajo nivel
(BD, APIs, archivos) dependen de una **abstracción**. La dependencia concreta
se **inyecta** desde afuera.

```
ProductCatalog (alto nivel) ──▶ ProductRepository (abstracción) ◀── SQLProductRepository (bajo nivel)
```

**Señales de que se está violando**

- `self.repo = SQLProductRepository()` dentro de una clase de negocio.
- El constructor está tipado con la clase concreta en lugar de la abstracción.
- No se puede testear la clase sin una base de datos real.

**Plantilla (tres piezas: abstracción, implementación, composition root)**

```python
from typing import Protocol


class ProductRepository(Protocol):  # abstracción
    def get_all_product_names(self) -> list[str]: ...


class SQLProductRepository:  # detalle (bajo nivel)
    def get_all_product_names(self) -> list[str]:
        return ["jean", "shirt"]


class ProductCatalog:  # alto nivel
    def __init__(self, product_repository: ProductRepository) -> None:
        self._product_repository = product_repository

    def list_all_products(self) -> list[str]:
        return self._product_repository.get_all_product_names()


def main() -> None:  # composition root: el único lugar que conoce lo concreto
    catalog = ProductCatalog(product_repository=SQLProductRepository())
    print(catalog.list_all_products())
```

**Beneficio en tests:** se inyecta un doble sin tocar `ProductCatalog`.

```python
class InMemoryProductRepository:
    def get_all_product_names(self) -> list[str]:
        return ["test"]


def test_list_all_products() -> None:
    catalog = ProductCatalog(InMemoryProductRepository())
    assert catalog.list_all_products() == ["test"]
```

**Paso intermedio, no lo copies:** en
[`product_catalog_with_factory.py`](dependency_inversion/product_catalog_with_factory.py)
`ProductCatalog` llama a `ProductFactory` desde adentro, así que sigue
acoplada a la fábrica. La versión a seguir es
[`product_catalog_with_dependency_inversion.py`](dependency_inversion/product_catalog_with_dependency_inversion.py).

**¿Y un contenedor IoC?** En Python, la inyección manual en la composition
root suele alcanzar. Si el grafo de dependencias crece, un contenedor registra
cómo se construye cada abstracción y el flujo principal solo pide lo que
necesita (`container.resolve(ProductCatalog)`). Hay un contenedor mínimo, sin
dependencias, en
[`product_catalog_with_ioc_container.py`](dependency_inversion/product_catalog_with_ioc_container.py).

Ejemplo completo: [dependency_inversion/](dependency_inversion/README.md) ·
Test: [test_dependency_inversion.py](tests/unit/test_dependency_inversion.py)

---

## Lista de revisión para code review

- [ ] **S**: ¿La clase tiene una sola razón para cambiar? ¿Persistencia,
      cálculos y E/S están fuera de la entidad?
- [ ] **O**: ¿Agregar una variante nueva significa crear una clase nueva, sin
      editar un `if/elif` central?
- [ ] **L**: ¿El cliente trata a todos los subtipos igual, sin `isinstance`?
      ¿Los métodos de consulta no tienen efectos secundarios?
- [ ] **I**: ¿Ninguna implementación tiene métodos vacíos o
      `NotImplementedError` solo para cumplir una interfaz?
- [ ] **D**: ¿Las dependencias llegan por el constructor, tipadas con
      abstracciones? ¿Los objetos concretos se crean solo en la composition
      root?
- [ ] **Equilibrio**: ¿Cada abstracción nueva resuelve una variación real, o
      es complejidad especulativa?

## Glosario

| Término | Definición |
| --- | --- |
| Cohesión | Cuánto se relacionan entre sí las partes de un componente. Conviene **alta**. |
| Acoplamiento | Cuánto depende un componente de otros. Conviene **bajo**. |
| Componente de software | Una clase, un método, un módulo o un paquete. |
| Alto nivel / bajo nivel | Reglas de negocio / detalles técnicos (BD, red, archivos). |
| Inyección de dependencias (DI) | Pasarle a una clase los objetos que necesita en lugar de que los cree ella. |
| Inversión de control (IoC) | Delegar la creación e inyección de dependencias a un contenedor o framework. Ver [`product_catalog_with_ioc_container.py`](dependency_inversion/product_catalog_with_ioc_container.py). |
| Composition root | El único punto de la aplicación donde se crean y conectan los objetos concretos. |
| Tell, Don't Ask | Pedirle al objeto que haga algo en lugar de consultar su tipo o estado y decidir desde afuera. |
