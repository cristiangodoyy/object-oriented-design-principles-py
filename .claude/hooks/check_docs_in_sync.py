"""Claude Code PostToolUse hook: keep the docs in sync with the examples.

After Claude edits an example (.py inside a principle folder) or a Markdown
doc, run tests/unit/test_docs_in_sync.py. On failure, exit with code 2 so the
test output is sent back to Claude, which then updates the README or
PATTERNS.md in the same turn.
"""

import json
import subprocess
import sys

from pathlib import PurePath

PRINCIPLES = {
    "single_responsibility",
    "open_close",
    "substitution",
    "interface_segregation",
    "dependency_inversion",
}


def _is_watched(file_path: str) -> bool:
    path = PurePath(file_path.replace("\\", "/"))
    if path.suffix == ".md":
        return True
    return path.suffix == ".py" and path.parent.name in PRINCIPLES


def main() -> int:
    payload = json.load(sys.stdin)
    tool_input = payload.get("tool_input", {})
    file_path = str(tool_input.get("file_path", ""))
    if not _is_watched(file_path):
        return 0

    result = subprocess.run(  # noqa: S603
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "tests/unit/test_docs_in_sync.py",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return 0

    failures = [
        line
        for line in result.stdout.splitlines()
        if line.startswith("E ") or "AssertionError" in line
    ]
    # stderr + exit code 2 is how a hook sends its message back to Claude.
    sys.stderr.write(
        "The documentation is out of sync with the examples. Update the "
        "README of the principle (or README.md / PATTERNS.md):\n"
        + "\n".join(failures or result.stdout.splitlines()[-20:])
        + "\n"
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
