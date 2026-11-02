# S — Responsabilidad única (Single Responsibility)

> Cada componente de software (clase, método o módulo) tiene **una sola razón
> para cambiar**.

## Archivos

| Archivo | Rol |
| --- | --- |
| [employee_example_before_single_responsibility.py](employee_example_before_single_responsibility.py) | Violación: `Employee` guarda sus datos, se persiste y calcula impuestos. |
| [employee_example_with_single_responsibility.py](employee_example_with_single_responsibility.py) | Solución: la responsabilidad se reparte entre `Employee`, `EmployeeRepository` y `TaxCalculator`. |
| [test_single_responsibility.py](../tests/unit/test_single_responsibility.py) | Test: `Employee` solo tiene datos y cada clase hace una sola cosa. |

```bash
uv run python -m single_responsibility.employee_example_before_single_responsibility
uv run python -m single_responsibility.employee_example_with_single_responsibility
```

Las dos versiones imprimen lo mismo. Cambia la estructura, no el
comportamiento.

## El problema (antes)

`Employee` tiene **cuatro razones para cambiar**: el formato del id, el
formato del nombre, la capa de base de datos y las reglas impositivas. Un
cambio en la base de datos obliga a modificar (y volver a probar) la entidad
de dominio.

```text
Employee
 ├─ datos (employee_id, name, address, employee_type)
 ├─ save()            ← persistencia
 └─ calculate_tax()   ← reglas de impuestos
```

## La solución (después)

| Clase | Única responsabilidad | Razón para cambiar |
| --- | --- | --- |
| `Employee` | Datos del empleado | Cambia el formato de los datos |
| `EmployeeRepository` | Persistencia | Cambia la base de datos |
| `TaxCalculator` | Cálculo de impuestos | Cambian las reglas impositivas |

`Employee` no conoce a sus colaboradores: quien necesita guardar o calcular
usa la clase especializada directamente.

```python
employee = Employee(31890233, "Cristian", "Lagos 4567", "full_time")
EmployeeRepository.save(employee)
TaxCalculator.calculate_tax(employee)
```

Resultado: **alta cohesión** (cada clase agrupa solo lo que tiene que ver con
su tarea) y **bajo acoplamiento** (cambiar la BD no toca `Employee`).

## Patrón para reutilizar

1. Enumerá las razones para cambiar de la clase.
2. Si hay más de una, extraé cada una a su propia clase.
3. Dejá la entidad con solo sus datos y reglas propias.
4. Quien necesite persistir o calcular usa la clase especializada directamente
   (o la recibe inyectada, ver
   [inversión de dependencias](../dependency_inversion/README.md)).

Plantilla tipada: [PATTERNS.md → S](../PATTERNS.md#s--responsabilidad-única-single-responsibility).

## Simplificaciones del ejemplo

- `EmployeeRepository.save()` y `TaxCalculator.calculate_tax()` imprimen en
  lugar de guardar o devolver un valor. En código real, el repositorio
  persiste y la calculadora devuelve el impuesto (ver la plantilla de
  `PATTERNS.md`).
- Las dos clases usan `@staticmethod`. Si van a tener dependencias propias
  (una conexión, configuración), conviene usar instancias y recibirlas
  inyectadas.

## Notas originales

### Cohesion

Is the degree to which the various parts of a software component are related.

### Coupling

Is defined as the level of interdependency between various software component.

### Single responsibility

- Every software component(Can be a class, a method, or module) should have one and only one responsibility.
- Always recommends loose coupling.
- High coupling is an undesirable feature in software.
- Loose coupling helps attain(lograr) better adherence to the Single Responsibility.
- When we develop classes, it should cater(atender) to the given functionality well.
If a class is taking care(se ocupa) of two functionalities, it is better to split them. It refers
to functionality as a reason to change.
For example, a class can undergo(sufrir) changes because of the difference in behavior expected
from it, but if a class is getting changed for two reasons(basically, changes in two functionalities),
then the class should be definitely split.

### Advantages

- Whenever there is a change in one functionality, this particular class needs to change, and nothing else.
- Aditionally, if a class has multiple functionalities, the dependent classes will have to undergo changes for
multiple reasons, which gets avoided.
