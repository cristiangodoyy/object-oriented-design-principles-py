import pytest

from dependency_inversion.product_catalog_with_dependency_inversion import (
    ProductCatalog,
    ProductRepository,
)
from dependency_inversion.product_catalog_with_ioc_container import (
    Container,
    configure_container,
)

pytestmark = pytest.mark.unit


class InMemoryProductRepository(ProductRepository):
    """Test double: no database needed to test ProductCatalog."""

    def get_all_product_names(self) -> list[str]:
        return ["test"]


def test_catalog_works_with_any_injected_repository() -> None:
    catalog = ProductCatalog(InMemoryProductRepository())

    assert catalog.list_all_products() == ["test"]


def test_container_resolves_catalog_with_registered_repository() -> None:
    container = Container()
    container.register(ProductRepository, InMemoryProductRepository)
    container.register(
        ProductCatalog,
        lambda: ProductCatalog(container.resolve(ProductRepository)),
    )

    assert container.resolve(ProductCatalog).list_all_products() == ["test"]


def test_default_container_uses_sql_repository() -> None:
    catalog = configure_container().resolve(ProductCatalog)

    assert catalog.list_all_products() == ["jean", "shirt"]
