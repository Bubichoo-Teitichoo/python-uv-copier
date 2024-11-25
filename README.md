# UV Copier

A Python project template with sensible defaults for UV, build using copier.

## Usage

This copier uses a Jinja Extension to read defaults for author name and e-Mail via git.
You can verify that no malicious code is executed by checking
[the extension](./extensions/git.py), [the config](./copier.yml) and the [the extension loader](https://github.com/copier-org/copier-templates-extensions).

```shell
uvx --with copier-templates-extensions copier copy --trust https://github.com/Bubichoo-Teitichoo/python-uv-copier <dest>
```
