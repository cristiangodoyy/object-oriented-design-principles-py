import pytest

from interface_segregation.printer_example_with_interface_segregation import (
    CannonPrinter,
    Fax,
    HPPrinterScanner,
    Print,
    Scan,
    XeroxWorkCentre,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    ("printer", "supported", "not_supported"),
    [
        (CannonPrinter(), (Print,), (Scan, Fax)),
        (HPPrinterScanner(), (Print, Scan), (Fax,)),
        (XeroxWorkCentre(), (Print, Scan, Fax), ()),
    ],
)
def test_each_printer_implements_only_what_it_supports(
    printer: Print,
    supported: tuple[type, ...],
    not_supported: tuple[type, ...],
) -> None:
    assert all(isinstance(printer, interface) for interface in supported)
    assert not any(isinstance(printer, i) for i in not_supported)


def test_client_depends_only_on_the_capability_it_needs() -> None:
    def scan_document(scanner: Scan) -> bytes:
        return scanner.scan()

    assert scan_document(HPPrinterScanner()) == b""
