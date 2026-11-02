"""Product catalog that applies the Dependency Inversion Principle.

ProductCatalog(high level module) --> ProductRepository(abstraction)
<-- SQLProductRepository(low level module)

The dependency is injected INTO ProductCatalog through its constructor,
instead of ProductCatalog worrying about instantiating the dependency.
This is the concept of dependency injection.
"""

from abc import ABC, abstractmethod


class ProductRepository(ABC):
    """The abstraction."""

    @abstractmethod
    def get_all_product_names(self) -> list[str]:
        """Return the names of all products."""


class SQLProductRepository(ProductRepository):
    """Low level class."""

    def get_all_product_names(self) -> list[str]:
        return ["jean", "shirt"]


class ProductCatalog:
    """High level class."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Receive the repository to use.

        We don't want the ProductCatalog to worry about how and when to
        trigger the instantiation of SQLProductRepository.
        ProductCatalog does NOT need to worry about any instantiation.
        The type hint is the abstraction (ProductRepository), never the
        concrete class, so any repository can be injected.
        """
        self._product_repository = product_repository

    def list_all_products(self) -> list[str]:
        return self._product_repository.get_all_product_names()


def ecommerce_main_application() -> None:
    """Composition root: the only place that knows the concrete classes.

    This function creates SQLProductRepository and injects it in
    ProductCatalog.
    """
    product_catalog = ProductCatalog(product_repository=SQLProductRepository())
    print(f"All products names: {product_catalog.list_all_products()}")


if __name__ == "__main__":
    ecommerce_main_application()
