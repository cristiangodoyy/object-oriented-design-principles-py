"""Smoke test: every example module runs as a script without errors."""

import runpy

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


@pytest.mark.parametrize(
    "example", EXAMPLES, ids=[f"{p.parent.name}/{p.name}" for p in EXAMPLES]
)
def test_example_runs(example: Path) -> None:
    # run_path executes the file as a script without touching sys.modules,
    # so it does not clash with the modules imported by the other tests.
    runpy.run_path(str(example), run_name="__main__")
