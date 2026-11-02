"""Inversion of control (IoC) with a minimal container.

Inversion of control(IOC) in Java:
It is closely related, so we'll cover it quickly.

The ProductCatalog had a constructor which took in a ProductRepository object.
The class that calls the ProductCatalog will provide or 'inject' the object.

But even though the injection happens outside of ProductCatalog, the injection
still happens during the main control flow of the program. i.e. injection is
happening in the main thread of program execution.

What if we want all the injections to happen in a separate thread or a
separate context altogether,
so that the main control flow is kept completely isolated from injection?
This can be achieved using frameworks.
If your preferred programming language is Java, then the Spring Framework is
a popular choice.

Spring will run in its own context,
different from the main flow of control of the program.
Spring will take care of injecting the required dependencies of a class.
So if you want to instantiate an object of a class, instead of doing it
yourself directly in the code, you ask Spring to give you an object of the
class.

The Spring Framework first looks at all the dependencies required for the
object instantiation, then goes ahead and injects each dependency and
instantiates the object, and gives it back to the main control flow.

Thus the control over dependency injection is completely delegated to the
Spring Framework and does not happen in the main control flow.
This concept is called inversion of control.
And Spring is called an inversion of control container or simply an
IOC container.

Inversion of control in Python:
https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python

Below, Container is a minimal IoC container: the wiring is registered once
(configure_container) and the main flow only asks the container for a
ProductCatalog, without knowing how it is built.
"""

from collections.abc import Callable
from typing import Any, TypeVar, cast

from dependency_inversion.product_catalog_with_dependency_inversion import (
    ProductCatalog,
    ProductRepository,
    SQLProductRepository,
)

T = TypeVar("T")


class Container:
    """Registry of how to build each abstraction."""

    def __init__(self) -> None:
        self._providers: dict[type[Any], Callable[[], Any]] = {}

    def register(
        self, abstraction: type[T], provider: Callable[[], T]
    ) -> None:
        self._providers[abstraction] = provider

    def resolve(self, abstraction: type[T]) -> T:
        return cast(T, self._providers[abstraction]())


def configure_container() -> Container:
    """Wiring: the only place that knows the concrete classes."""
    container = Container()
    container.register(ProductRepository, SQLProductRepository)
    container.register(
        ProductCatalog,
        lambda: ProductCatalog(container.resolve(ProductRepository)),
    )
    return container


def ecommerce_main_application(container: Container) -> None:
    """Run the main control flow without building any dependency."""
    product_catalog = container.resolve(ProductCatalog)
    print(f"All products names: {product_catalog.list_all_products()}")


if __name__ == "__main__":
    ecommerce_main_application(configure_container())
