## Project Context

This is a python project: a reference catalogue of SOLID / object-oriented
design examples (each principle has a "before" and an "after" version).

When creating or modifying classes, follow the rules and templates in
PATTERNS.md. Read README.md for the repository map and each principle's
README.md for the reasoning and the caveats of each example.

The tests in `tests/unit/` are the executable version of the guide: one file
per principle, a smoke test that runs every example, and a test that runs
the snippets of PATTERNS.md.

`tests/unit/test_docs_in_sync.py` checks that every example file and class is
documented. A PostToolUse hook (`.claude/settings.json`) runs it after each
edit: if it reports a failure, update the README of the principle (or
README.md / PATTERNS.md) before finishing.

## Repository assumptions

- Python is the primary implementation language.
- Use `uv` as the package and command runner.
- Use `pytest` for tests.
- Use `ruff` for linting and formatting policy.
- Use `mypy` (strict) for type checking: every example must be fully typed.
- Keep the examples dependency-free: they illustrate design principles,
  not libraries.
- Keep the file naming scheme: `<example>_before_<principle>.py` and
  `<example>_with_<principle>.py`.

## Validation command preference

Prefer commands in this order, depending on the affected code:

```bash
uv run pytest path/to/test_file.py -q
uv run pytest -m unit -q
uv run ruff check .
uv run mypy .
uv run pre-commit run --all-files
```

## AI context map

Before exploring this codebase, read `.codesight/CODESIGHT.md` (file/class/import inventory)
and `.codesight/wiki/index.md`. They're a starting point, not a source of truth - always read
the actual source file before implementing changes; the map doesn't capture full logic.
Re-run `npx codesight && npx codesight --wiki` after structural changes (new/removed files,
new classes) to keep it current.


