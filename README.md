# Python starters

A reference pack provided by the pytemplate-hub maintainer.

Three small, typed starting points for [pytemplate-uv](https://github.com/yuxuzi/pytemplate-uv): a
Python script, a Typer command-line app, and a typed library for PyPI. Each generated project uses
uv, ruff, mypy in strict mode, and pytest, and has an `AGENTS.md` and a `CLAUDE.md` for coding
agents. The pack has no optional components.

## What you get

A `cli` project looks like this (the other profiles follow the same pattern):

```text
my-app/
  .copier-answers.yml
  .gitignore
  .pytemplate.toml
  AGENTS.md
  CLAUDE.md
  README.md
  pyproject.toml
  my_app/
    __init__.py
    cli.py
    core.py
  tests/
    test_cli.py
    test_core.py
  uv.lock
```

The `library` profile adds `py.typed`, `CHANGELOG.md`, and `.github/workflows/ci.yml`.

## Profiles

| Profile | Kind | What you get |
| --- | --- | --- |
| `script` | cli | One package with a `main()` entry point, a `[project.scripts]` command, standard library only (argparse), and one tested function. |
| `cli` | cli | A Typer app (`typer>=0.12`) with two subcommands, `--version`, plain output, and tests with `typer.testing.CliRunner`. |
| `library` | library | A typed package for PyPI: `py.typed`, a small public API in `__init__.py` with `__all__`, docstrings, a test, a `CHANGELOG.md`, and a GitHub Actions workflow that runs on Python 3.11 and 3.13. |

## Create a project

```bash
uvx pytemplate-uv@latest create my-app -p cli -h yuxuzi/pytemplate-starters@v1.1.0 -y
```

`-h` (`--hub`, pytemplate-uv 3.5 or later) reads the commit and digest that
[pytemplate-hub](https://yuxuzi.github.io/pytemplate-hub/) checked for this tag, and refuses the pack if
anything changed. For CI or offline use, copy the fully pinned command from the pack's listing there.

Replace `cli` with `script` or `library`. The hub's listing page also gives `--template-commit` and
`--template-digest` values, which refuse the pack if it has changed.

## What the generated checks run

Each project's lifecycle checks, which pytemplate-uv runs after rendering, are:

```bash
uv sync
uv run ruff check .
uv run ruff format --check .
uv run mypy <package> tests
uv run pytest
```

The tests are offline. The checks do not scan dependencies or code for security problems. The
projects need no secrets or services.

## Make your own pack from this one

1. Fork or copy this repository.
2. Change `id` in `pytemplate-pack.toml` to your own pack name.
3. Edit a profile under `<profile>/template/` and its `profile.toml`. To add a profile, add it to
   the `profile` choices in `questions.yml`.
4. Check it:
   ```bash
   uvx pytemplate-uv@latest list-profiles --template .
   uvx pytemplate-uv@latest create t -p <profile> --template . -y -o <temp-dir>
   ```
   Then run `uv run pytest` in the new project.
5. Tag a release, then list the pack on [pytemplate-hub](https://github.com/yuxuzi/pytemplate-hub)
   by adding it to `docs/authors.md`.

## License

MIT. See [LICENSE](LICENSE).
