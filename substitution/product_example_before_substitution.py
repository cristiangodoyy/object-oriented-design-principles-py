"""Products that violate the Liskov Substitution Principle.

Is NOT a good design. This is against the Substitution Principle.
We should have been able to deal with all the objects as Product
objects itself instead of call isinstance() method to apply
each discount for each product.
"""


class Product:
    def __init__(self) -> None:
        self.percentage_discount: float = 10

    def get_discount(self) -> float:
        return self.percentage_discount


class InHouseProduct(Product):
    def apply_extra_discount(self) -> None:
        self.percentage_discount += 0.5

    def apply_extra_discount_buying_with_bitcoin(self) -> None:
        self.percentage_discount += 2


class InCommerceProduct(Product):
    def apply_extra_discount(self) -> None:
        self.percentage_discount += 1


def client() -> None:
    """Print the discount of each product.

    Client does need to ask if each product is instance of the specific
    class.
    """
    products: list[Product] = [InCommerceProduct(), InHouseProduct()]

    for product in products:
        # We are asking or enquiring about the subtype. Client does need to
        # ask if each product is instance of the specific class.
        if isinstance(product, InHouseProduct):
            product.apply_extra_discount()
            product.apply_extra_discount_buying_with_bitcoin()
        if isinstance(product, InCommerceProduct):
            product.apply_extra_discount()

        print(product.get_discount())


if __name__ == "__main__":
    client()
