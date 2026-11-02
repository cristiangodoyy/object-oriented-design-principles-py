"""Intermediate step: abstraction plus a factory.

ProductCatalog(high level module) --> ProductRepository(abstraction)
<-- SQLProductRepository(low level module)

The high level module does not reference SQLProductRepository anymore and
both modules depend on the abstraction.

This is NOT the final solution: ProductCatalog still calls ProductFactory
from inside, and the factory is tied to SQLProductRepository. ProductCatalog
cannot be used with another repository without changing it. The final
solution, where the dependency is injected, is
product_catalog_with_dependency_inversion.py.
"""

from abc import ABC, abstractmethod


class ProductRepository(ABC):  # this is the abstraction
    @abstractmethod
    def get_all_product_names(self) -> list[str]:
        """Return the names of all products.

        Abstractions should not depend on details.
        Details should depend on abstractions.
        """


class SQLProductRepository(ProductRepository):  # low level class
    """Repository backed by SQL.

    The detail, which is the SQLProductRepository class,
    is dependent on the abstraction, which is the ProductRepository class.
    This is strictly as per the definition. -> "Abstractions should not
    depend on details. Details should depend on abstractions."
    """

    def get_all_product_names(self) -> list[str]:
        """Return the names of all products from SQL.

        Los detalles(el codigo del metodo) dependen de implementar el metodo
        definido en la abstraccion(intertface ProductRepository).
        Tenemos que impementar detalles definidos en una abstraccion.
        """
        return ["jean", "shirt"]


class ProductFactory:
    @staticmethod
    def create_sql_product_repository() -> ProductRepository:
        return SQLProductRepository()


class ProductCatalog:  # high level class
    """Catalog that obtains its repository from the factory.

    Our reference object is ProductRepository, so we don't have any
    tight coupling with SQLProductRepository anywhere in the
    ProductCatalog class. But it is still coupled to ProductFactory.
    """

    def list_all_products(self) -> None:
        # Our reference is ProductRepository, so we don't have any tight
        # coupling with SQLProductRepository.
        product_repository = ProductFactory.create_sql_product_repository()
        all_product_names = product_repository.get_all_product_names()

        print(f"All products names: {all_product_names}")


if __name__ == "__main__":
    ProductCatalog().list_all_products()
