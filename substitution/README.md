# L — Sustitución de Liskov (Liskov Substitution)

> Los objetos se tienen que poder reemplazar por sus subtipos **sin afectar la
> corrección del programa** y sin que el cliente pregunte de qué subtipo se
> trata.

## Archivos

| Archivo | Rol |
| --- | --- |
| [product_example_before_substitution.py](product_example_before_substitution.py) | Violación: el cliente usa `isinstance` para saber qué métodos llamar según el subtipo. |
| [product_example_with_substitution.py](product_example_with_substitution.py) | Solución: cada subtipo sobrescribe `get_discount()` y el cliente trata a todos como `Product`. |
| [test_substitution.py](../tests/unit/test_substitution.py) | Test: cada subtipo sustituye a `Product` y `get_discount()` no tiene efectos secundarios. |

```bash
uv run python -m substitution.product_example_before_substitution
uv run python -m substitution.product_example_with_substitution
```

Las dos versiones imprimen `11` y `12.5`.

## El problema (antes)

```python
for product in products:
    if isinstance(product, InHouseProduct):
        product.apply_extra_discount()
        product.apply_extra_discount_buying_with_bitcoin()
    if isinstance(product, InCommerceProduct):
        product.apply_extra_discount()
    print(product.get_discount())
```

- El cliente conoce todos los subtipos concretos.
- Cada subtipo nuevo obliga a agregar otro `isinstance` (también viola
  [Abierto/Cerrado](../open_close/README.md)).
- Un `Product` no es realmente intercambiable por sus subtipos: hay que
  tratarlos distinto.

## La solución (después): "Tell, Don't Ask"

Cada subtipo sobrescribe `get_discount()` y aplica internamente sus reglas. El
cliente **le pide** el descuento al objeto en lugar de **preguntarle** qué es:

```python
class InHouseProduct(Product):
    def get_discount(self) -> float:
        return (
            super().get_discount()
            + self.EXTRA_DISCOUNT
            + self.BITCOIN_DISCOUNT
        )


for product in products:
    print(product.get_discount())
```

`get_discount()` es una consulta: calcula el valor sin modificar el estado,
así que llamarlo varias veces al mismo objeto siempre devuelve lo mismo.

## Patrón para reutilizar

1. Buscá `isinstance(obj, Subclase)` o chequeos de tipo en el código cliente.
2. Mové el comportamiento que varía a un método del tipo base.
3. Hacé que cada subclase lo sobrescriba respetando el contrato: mismos
   parámetros, mismo tipo de retorno, sin excepciones nuevas.
4. El cliente llama solo a métodos del tipo base.

Plantilla tipada: [PATTERNS.md → L](../PATTERNS.md#l--sustitución-de-liskov-liskov-substitution).

## Simplificaciones del ejemplo

- Los descuentos son constantes de clase. En código real suelen venir de
  configuración o de otra fuente, y se reciben por el constructor.
- En la versión "antes", los métodos `apply_*` modifican el descuento del
  objeto: es parte de la violación (el cliente tiene que llamarlos en el
  orden correcto según el subtipo).

## Notas originales

### The substitution principle

- Object should be replaceable with their subtypes without affecting
the correctness of the program.
- Derived class must be able to completely substitute the base classes.
- This principle is pretty straightforward(sencillo) in the sense(dice)
that it says when application developers write derived classes, they should
extend the base class.
- It also suggests that the derived class should as close(cerca)
to the base class as possible so much so that the derived class itself
should replace the base class without any code changes.
