from shutil import which
import subprocess

from jinja2.ext import Extension


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        self._git = which("git")

        self.environment.globals["git_name"] = lambda: self._read_git_config(
            "user.name"
        )
        self.environment.globals["git_mail"] = lambda: self._read_git_config(
            "user.email"
        )

    def _read_git_config(self, key: str) -> str:
        if self._git is None:
            return ""

        result = subprocess.run(
            [self._git, "config", "--global", key],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if result.returncode:
            return ""
        return result.stdout.strip()
