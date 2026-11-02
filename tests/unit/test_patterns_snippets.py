"""The Python snippets of PATTERNS.md run, so the guide does not go stale."""

import re

from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

PATTERNS = Path(__file__).resolve().parents[2] / "PATTERNS.md"
SNIPPETS = re.findall(
    r"```python\n(.*?)```", PATTERNS.read_text(encoding="utf-8"), re.DOTALL
)


def test_patterns_has_snippets() -> None:
    assert SNIPPETS


@pytest.mark.parametrize("index", range(len(SNIPPETS)))
def test_snippet_runs(index: int) -> None:
    # A snippet may build on the previous one (e.g. the DIP test double
    # reuses ProductCatalog), so each one runs on top of the previous one.
    namespace: dict[str, object] = {}
    for snippet in SNIPPETS[: index + 1]:
        exec(snippet, namespace)  # noqa: S102

    for name, value in list(namespace.items()):
        if name.startswith("test_") and callable(value):
            value()
