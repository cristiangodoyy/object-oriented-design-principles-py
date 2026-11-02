# O — Abierto/Cerrado (Open/Closed)

> Abierto para extensión, cerrado para modificación: para agregar
> comportamiento **creás una clase nueva**, sin editar el código existente.

## Archivos

| Archivo | Rol |
| --- | --- |
| [student_example_before_open_close.py](student_example_before_open_close.py) | Violación: `DiscountCalculator` conoce todos los tipos de estudiante y decide con una cadena de `if` sobre `student_type`. |
| [student_example_with_open_close.py](student_example_with_open_close.py) | Solución: `DiscountCalculator` trabaja contra la interfaz `StudentProfile`. `ElementarySchoolStudent` se agrega sin tocar la calculadora. |
| [test_open_close.py](../tests/unit/test_open_close.py) | Test: perfiles nuevos, definidos fuera del módulo, funcionan sin modificar `DiscountCalculator`. |

```bash
uv run python -m open_close.student_example_before_open_close
uv run python -m open_close.student_example_with_open_close
```

Las dos versiones imprimen el descuento de los tres tipos de estudiante. La
salida varía entre ejecuciones porque la regla de descuento usa
`random.choice` para simular una regla de negocio.

## El problema (antes)

```python
@staticmethod
def calculate_discount_percentage(student: Student) -> int:
    if student.student_type == "university":
        return 20 if random.choice([True, False]) else 0

    if student.student_type == "high_school":
        return 20 if random.choice([True, False]) else 0

    # New feature: to support elementary school students we had to
    # MODIFY this method, which already worked and was already tested.
    if student.student_type == "elementary_school":
        return 20 if random.choice([True, False]) else 0

    return 0
```

```text
DiscountCalculator
 ├─ if 'university'         ← regla de universitarios
 ├─ if 'high_school'        ← regla de secundaria
 └─ if 'elementary_school'  ← rama nueva: hubo que MODIFICAR la clase
```

- `Student` no tiene comportamiento propio. El tipo es solo un string, así que
  las reglas de cada tipo terminan en la calculadora.
- `DiscountCalculator` tiene **una razón para cambiar por cada tipo de
  estudiante**, más una por cada tipo nuevo (también viola
  [Responsabilidad única](../single_responsibility/README.md)).
- Agregar `elementary_school` obligó a editar un método que ya funcionaba y
  que ya se había probado. Eso aumenta el riesgo de regresiones.

## La solución (después)

```text
DiscountCalculator ──usa──▶ StudentProfile (ABC)
                                 ▲
             ┌───────────────────┼─────────────────────┐
     UniversityStudent   HighSchoolStudent   ElementarySchoolStudent ← extensión nueva
```

- `StudentProfile` define el contrato `has_discount()`.
- Cada tipo de estudiante resuelve su propia regla.
- `DiscountCalculator` **no cambia** cuando aparece un tipo nuevo.

## Patrón para reutilizar

1. Identificá el `if/elif` (o `match`) que crece con cada variante.
2. Convertí cada rama en una clase que implementa una interfaz común.
3. Hacé que el código central dependa solo de la interfaz.
4. Las variantes nuevas son clases nuevas, sin tocar código existente.

Plantilla tipada: [PATTERNS.md → O](../PATTERNS.md#o--abiertocerrado-openclosed).

**Precaución:** no crees abstracciones para variaciones hipotéticas. Aplicá
el principio cuando la variación es real o muy probable (ver la sección
*Caution* del [README principal](../README.md)).

## Simplificaciones del ejemplo

- `random.choice` en las reglas de descuento (en `has_discount()` de la
  versión "después" y en cada rama de la versión "antes") es solo para la
  demo. Las reglas reales deben ser deterministas y testeables.
- En la versión "antes", comparar `student_type` contra strings sueltos es
  frágil: un error de tipeo (`'highschool'`) cae en silencio en `return 0`. Si
  de verdad necesitás un discriminador de tipo, usá un `StrEnum`.
- `DiscountCalculator` usa `@staticmethod`. Si la calculadora va a tener
  dependencias propias (configuración, repositorios), conviene un método de
  instancia con dependencias inyectadas.

## Notas originales

### Questions

- How can something be open and closed at the same time?

### Open/Close

- Classes or objects and methods should be open for extension but close for modification, this means that when you
develop your software application make sure that you write your classes or modules in a generic way so that whenever
you feel the need to extend the behavior of the class or object, then you shouldn't have to change the class itself.
Rather, a simple extension of the class should help you build the new behavior.
- Example: when a developer has to create a class implementation by extending the abstract base class to implement
the required behavior instead of changing the abstract class.

### Open for extension

- A software component(class, module, method) should be extendable to add a new feature or to add a new behavior to it.

### Close for modification

- New features getting added to the software component, should not have to modify existing code.

### Advantages

- Existing classes are not changed and hence the chances of regression are less.
- It also helps maintain backward compatibility for the previous code.

### Key takeaways

- Ease of adding new features
- Open Closed principle often requires decoupling which, in turn, automatically follows the Single Responsibility Principle.
