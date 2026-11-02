"""The documentation stays in sync with the example classes.

If one of these tests fails after changing an example, update the README of
the principle (or the main README.md / PATTERNS.md) as the message says.
"""

import ast
import re

from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

ROOT = Path(__file__).resolve().parents[2]
PRINCIPLES = (
    "single_responsibility",
    "open_close",
    "substitution",
    "interface_segregation",
    "dependency_inversion",
)
EXAMPLES = sorted(
    path
    for principle in PRINCIPLES
    for path in (ROOT / principle).glob("*.py")
    if path.stem != "__init__"
)
EXAMPLE_IDS = [f"{p.parent.name}/{p.name}" for p in EXAMPLES]
# Names that shadow Python built-ins: the templates must not use them.
FORBIDDEN_NAMES = {"id", "type"}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _public_classes(example: Path) -> list[str]:
    tree = ast.parse(_read(example))
    return [
        node.name
        for node in tree.body
        if isinstance(node, ast.ClassDef) and not node.name.startswith("_")
    ]


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_example_is_linked_in_its_readme(example: Path) -> None:
    readme = example.parent / "README.md"

    assert f"({example.name})" in _read(readme), (
        f"{example.name} is not linked in the 'Archivos' table of "
        f"{example.parent.name}/README.md"
    )


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_example_is_linked_in_the_main_readme(example: Path) -> None:
    link = f"({example.parent.name}/{example.name})"

    assert link in _read(ROOT / "README.md"), (
        f"{example.parent.name}/{example.name} is not linked in the "
        "repository map of README.md"
    )


@pytest.mark.parametrize("example", EXAMPLES, ids=EXAMPLE_IDS)
def test_example_classes_are_documented(example: Path) -> None:
    readme_path = example.parent / "README.md"
    readme = _read(readme_path)

    missing = [
        name
        for name in _public_classes(example)
        if not re.search(rf"\b{name}\b", readme)
    ]

    assert not missing, (
        f"Classes of {example.name} not mentioned in "
        f"{example.parent.name}/README.md: {', '.join(missing)}"
    )


def test_patterns_templates_do_not_shadow_builtins() -> None:
    snippets = re.findall(
        r"```python\n(.*?)```", _read(ROOT / "PATTERNS.md"), re.DOTALL
    )
    offending: set[str] = set()
    for snippet in snippets:
        for node in ast.walk(ast.parse(snippet)):
            if isinstance(node, ast.AnnAssign) and isinstance(
                node.target, ast.Name
            ):
                offending.add(node.target.id)
            elif isinstance(node, ast.arg):
                offending.add(node.arg)
            elif isinstance(node, ast.Attribute):
                offending.add(node.attr)

    assert not offending & FORBIDDEN_NAMES, (
        "PATTERNS.md templates use names that shadow built-ins: "
        f"{', '.join(sorted(offending & FORBIDDEN_NAMES))}"
    )
