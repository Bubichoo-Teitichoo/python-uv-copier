# uv copier

A Python project template with sensible defaults for [uv], build using [copier].

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [poe](https://poethepoet.natn.io/installation.html)

## Features

- linting, formatting and import sorting using [ruff]
- static type checking using [mypy]
- tasks with [poe]
- automatic version bumping and changelog generation with [commitizen] and [git-changelog]
- pre-configured [uv], [ruff], [mypy] and more [pre-commit] hooks
- pre-configured [mkdocs] documentation and API references powered by [mkdocstrings]

## Copy

This copier uses a Jinja Extension to read defaults for author name and e-Mail via git.
You can verify that no malicious code is executed by checking
[the extension](./extensions/git.py),
[the config](./copier.yml)
and the [the extension loader](https://github.com/copier-org/copier-templates-extensions).

```shell
uvx --with copier-templates-extensions copier copy --trust https://github.com/Bubichoo-Teitichoo/python-uv-copier <dest>
```

## Tasks

|     Name     |                       Description                          |
|:------------:|:----------------------------------------------------------:|
| `poe setup`  |   Create development environment and install commit hooks  |
|  `poe lint`  |              Execute ruff and mypy linters                 |
| `poe format` |               Format source code with ruff                 |
|  `poe bump`  | Increment the projects version based on convention commits |
|  `poe docs`  |     Build documentation and start a live preview server    |


[commitizen]: <https://commitizen-tools.github.io/commitizen/>
[copier]: <https://copier.readthedocs.io/en/stable/>
[git-changelog]: <https://pawamoy.github.io/git-changelog/>
[mkdocs]: <https://www.mkdocs.org/>
[mkdocstrings]: <https://mkdocstrings.github.io/python/>
[mypy]: <https://mypy.readthedocs.io/en/stable/>
[poe]: <https://poethepoet.natn.io/index.html>
[ruff]: <https://poethepoet.natn.io/index.html>
[pre-commit]: <https://pre-commit.com/>
[uv]: <https://docs.astral.sh/uv/>
