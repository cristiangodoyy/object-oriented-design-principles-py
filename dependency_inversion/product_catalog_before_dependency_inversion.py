"""Product catalog that violates the Dependency Inversion Principle.

ProductCatalog directly depends on SQLProductRepository, so this is the
violation of the principle as seen in code.

So the definition gives us some guidance on how to fix this violation as
well: Both should depend on abstractions.
"""


class SQLProductRepository:  # low level class
    def get_all_product_names(self) -> list[str]:
        return ["jean", "shirt"]


class ProductCatalog:  # high level class
    """ProductCatalog directly depends on SQLProductRepository."""

    def list_all_products(self) -> None:
        # We have tight coupling with SQLProductRepository.
        sql_repository = SQLProductRepository()
        all_product_names = sql_repository.get_all_product_names()
        print(f"All products names: {all_product_names}")


if __name__ == "__main__":
    ProductCatalog().list_all_products()
