"""Printers that apply the Interface Segregation Principle.

Each printer implements only the small interfaces it can fulfill.
"""

from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print(self, document: str) -> None: ...

    @abstractmethod
    def get_print_spool_details(self) -> str: ...


class Scan(ABC):
    @abstractmethod
    def scan(self) -> bytes: ...

    @abstractmethod
    def scan_photo(self) -> bytes: ...


class Fax(ABC):
    @abstractmethod
    def fax(self, number: str, document: str) -> None: ...

    @abstractmethod
    def internet_fax(self, email: str, document: str) -> None: ...


class XeroxWorkCentre(Print, Scan, Fax):
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


class HPPrinterScanner(Print, Scan):
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


class CannonPrinter(Print):
    def print(self, document: str) -> None:
        """Assume real code here."""

    def get_print_spool_details(self) -> str:
        """Assume real code here."""
        return ""
