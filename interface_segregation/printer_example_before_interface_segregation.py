"""Printers that violate the Interface Segregation Principle.

Multifunction forces every printer to implement print, scan and fax, even
the printers that can only print.
"""

from abc import ABC, abstractmethod


class Multifunction(ABC):
    @abstractmethod
    def print(self, document: str) -> None: ...

    @abstractmethod
    def get_print_spool_details(self) -> str: ...

    @abstractmethod
    def scan(self) -> bytes: ...

    @abstractmethod
    def scan_photo(self) -> bytes: ...

    @abstractmethod
    def fax(self, number: str, document: str) -> None: ...

    @abstractmethod
    def internet_fax(self, email: str, document: str) -> None: ...


class CannonPrinter(Multifunction):
    """Printer that can only print, but is forced to scan and fax."""

    def print(self, document: str) -> None:
        """Assume real code here."""

    def get_print_spool_details(self) -> str:
        """Assume real code here."""
        return ""

    def scan(self) -> bytes:
        """Not supported: implemented only to satisfy the interface."""
        return b""

    def scan_photo(self) -> bytes:
        """Not supported: implemented only to satisfy the interface."""
        return b""

    def fax(self, number: str, document: str) -> None:
        """Not supported: implemented only to satisfy the interface."""

    def internet_fax(self, email: str, document: str) -> None:
        """Not supported: implemented only to satisfy the interface."""


class HPPrinterScanner(Multifunction):
    """Printer and scanner, but is forced to fax."""

    def print(self, document: str) -> None:
        """Assume real code here."""

    def get_print_spool_details(self) -> str:
        """Assume real code here."""
        return ""

    def scan(self) -> bytes:
        """Assume real code here."""
        return b""

    def scan_photo(self) -> bytes:
        """Assume real code here."""
        return b""

    def fax(self, number: str, document: str) -> None:
        """Not supported: implemented only to satisfy the interface."""

    def internet_fax(self, email: str, document: str) -> None:
        """Not supported: implemented only to satisfy the interface."""


class XeroxWorkCentre(Multifunction):
    """Multifunction device: the only one that uses the whole interface."""

    def print(self, document: str) -> None:
        """Assume real code here."""

    def get_print_spool_details(self) -> str:
        """Assume real code here."""
        return ""

    def scan(self) -> bytes:
        """Assume real code here."""
        return b""

    def scan_photo(self) -> bytes:
        """Assume real code here."""
        return b""

    def fax(self, number: str, document: str) -> None:
        """Assume real code here."""

    def internet_fax(self, email: str, document: str) -> None:
        """Assume real code here."""
