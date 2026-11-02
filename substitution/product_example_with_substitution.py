"""Products that apply the Liskov Substitution Principle.

Every subtype can replace Product without affecting the correctness of the
program. The solution to this pattern is called 'Tell, Don't Ask'.
"""


class Product:
    BASE_DISCOUNT: float = 10

    def get_discount(self) -> float:
        return self.BASE_DISCOUNT


class InHouseProduct(Product):
    EXTRA_DISCOUNT: float = 0.5
    BITCOIN_DISCOUNT: float = 2

    def get_discount(self) -> float:
        """Return the discount including the in-house extras.

        get_discount can be substituted by their subtypes without affecting
        the correctness of the program.
        Here is where the Liskov Substitution Principle is applied.
        It is a query: it calculates the value without modifying the state,
        so calling it twice returns the same result.
        """
        return (
            super().get_discount()
            + self.EXTRA_DISCOUNT
            + self.BITCOIN_DISCOUNT
        )


class InCommerceProduct(Product):
    EXTRA_DISCOUNT: float = 1

    def get_discount(self) -> float:
        """Return the discount including the in-commerce extra.

        get_discount can be substituted by their subtypes without affecting
        the correctness of the program.
        Here is where the Liskov Substitution Principle is applied.
        """
        return super().get_discount() + self.EXTRA_DISCOUNT


def client() -> None:
    """Print the discount of each product.

    The client does not need to ask anything.
    This is what we mean by 'Tell, Don't Ask'.
    """
    products: list[Product] = [InCommerceProduct(), InHouseProduct()]

    for product in products:
        print(product.get_discount())


if __name__ == "__main__":
    client()
