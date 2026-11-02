# I — Segregación de interfaces (Interface Segregation)

> Los clientes no deben estar obligados a depender de métodos que no usan.
> Preferí **varias interfaces pequeñas** antes que una grande.

## Archivos

| Archivo | Rol |
| --- | --- |
| [printer_example_before_interface_segregation.py](printer_example_before_interface_segregation.py) | Violación: una única interfaz `Multifunction` con seis métodos que todas las impresoras deben implementar. |
| [printer_example_with_interface_segregation.py](printer_example_with_interface_segregation.py) | Solución: interfaces `Print`, `Scan` y `Fax`. Cada impresora implementa solo lo que soporta. |
| [test_interface_segregation.py](../tests/unit/test_interface_segregation.py) | Test: cada impresora implementa solo sus interfaces y un cliente pide solo la capacidad que usa. |

```bash
uv run python -m interface_segregation.printer_example_before_interface_segregation
uv run python -m interface_segregation.printer_example_with_interface_segregation
```

Los módulos solo definen clases y no imprimen nada. El valor del ejemplo está
en la estructura.

## El problema (antes)

`Multifunction` obliga a `CannonPrinter`, que en la realidad solo imprime, a
implementar `scan`, `scan_photo`, `fax` e `internet_fax`. En la práctica eso
termina en métodos vacíos (en el ejemplo están marcados como *"Not supported:
implemented only to satisfy the interface"*) o en `raise NotImplementedError`,
que además rompe
[Liskov](../substitution/README.md): el objeto no cumple el contrato que
promete.

## La solución (después)

| Clase | `Print` | `Scan` | `Fax` |
| --- | :-: | :-: | :-: |
| `XeroxWorkCentre` | ✔ | ✔ | ✔ |
| `HPPrinterScanner` | ✔ | ✔ | |
| `CannonPrinter` | ✔ | | |

Cada clase hereda solo las interfaces que puede cumplir. Los clientes pueden
pedir exactamente la capacidad que necesitan (por ejemplo, una función que
recibe un `Scan`).

## Patrón para reutilizar

1. Buscá implementaciones con métodos vacíos, `pass` o `NotImplementedError`.
2. Agrupá los métodos de la interfaz grande por capacidad cohesiva.
3. Creá una interfaz por capacidad.
4. Cada clase implementa (o hereda de) varias interfaces pequeñas, y los
   clientes tipan sus parámetros con la interfaz mínima que necesitan.

Plantilla tipada: [PATTERNS.md → I](../PATTERNS.md#i--segregación-de-interfaces-interface-segregation).

## Simplificaciones del ejemplo

- Los cuerpos `"""Assume real code here."""` son marcadores de posición:
  devuelven valores vacíos (`""`, `b""`) para cumplir los tipos.

## Notas originales

### Interface segregation principle

- Clients should not be forced to depend on interface they don't use.
- This principle talks about software developers writing their interface well.
- For instance, it reminds the developers/architects to developer methods that relate to the functionality.

### Problem

- If there is any method that is not related to the interface, the class dependent on the interface has to implement
it unnecessarily.
