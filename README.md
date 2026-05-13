# uv copier

An opinionated Python project template with sensible defaults, build using [copier].

## Prerequisites

- [mise](https://docs.astral.sh/uv/getting-started/installation/)

## Features

- linting, formatting and import sorting using [ruff]
- static type checking with [pyrefly]
- automation [tasks](#tasks) powered by [mise]
- automatic version bumping and changelog generation with [commitizen] and [git-changelog]
- pre-configured [uv], [ruff], [pyrefly] and more [prek] hooks
- pre-configured [mkdocs] documentation and API references powered by [mkdocstrings]

## Copy

This copier uses a Jinja Extension to read defaults for author name and e-Mail via git.
You can verify that no malicious code is executed by checking
[the extension](./extensions/git.py),
[the config](./copier.yml)
and the [the extension loader](https://github.com/copier-org/copier-templates-extensions).

```shell
mise x uv -- uvx --with copier-templates-extensions copier copy --trust https://github.com/Bubichoo-Teitichoo/python-uv-copier <dest>
```

## Tasks

|      Name     |                        Description                           |
|:-------------:|:------------------------------------------------------------:|
| `mise setup`  |    Create development environment and install commit hooks   |
|  `mise lint`  |             Execute ruff and pyrefly linters                 |
| `mise format` |                Format source code with ruff                  |
|  `mise bump`  | Increment the projects version based on conventional commits |
|  `mise docs`  |      Build documentation and start a live preview server     |


[commitizen]: <https://commitizen-tools.github.io/commitizen/>
[copier]: <https://copier.readthedocs.io/en/stable/>
[git-changelog]: <https://pawamoy.github.io/git-changelog/>
[mkdocs]: <https://www.mkdocs.org/>
[mkdocstrings]: <https://mkdocstrings.github.io/python/>
[pyrefly]: <https://pyrefly.org/>
[poe]: <https://mise.jdx.dev/>
[ruff]: <https://poethepoet.natn.io/index.html>
[prek]: <https://prek.j178.dev/>
[uv]: <https://docs.astral.sh/uv/>
