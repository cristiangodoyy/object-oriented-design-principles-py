import pytest

from substitution.product_example_with_substitution import (
    InCommerceProduct,
    InHouseProduct,
    Product,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    ("product", "expected"),
    [(Product(), 10), (InCommerceProduct(), 11), (InHouseProduct(), 12.5)],
)
def test_every_subtype_substitutes_product(
    product: Product, expected: float
) -> None:
    assert product.get_discount() == expected


@pytest.mark.parametrize("product", [InCommerceProduct(), InHouseProduct()])
def test_get_discount_has_no_side_effects(product: Product) -> None:
    results = {product.get_discount() for _ in range(3)}

    assert len(results) == 1
