import subprocess
from datetime import datetime
from typing import Optional


class GitGateway:
    def add(self, path: str = "."):
        return self._git("add", path)

    def commit(self, message: str, date: Optional[datetime] = None):
        commit_args = [f'-m"{message}"']
        if date:
            commit_args += ["--date", f'"{date.ctime()}"']
        return self._git("commit", *commit_args)

    def push(self, branch: Optional[str] = None):
        if not branch:
            branch = self._current_branch()

        return self._git("push", "origin", branch)

    def disable_garbage_collector(self):
        return self._git("config", "--local", "gc.auto", "0")

    def enable_garbage_collector(self):
        return self._git("config", "--local", "gc.auto", "1")

    def _current_branch(self):
        return self._git("rev-parse", "--abbrev-ref", "HEAD")

    def _git(self, command: str, *args):
        call_args = ["git", command]
        call_args.extend(args)
        return subprocess.run(
            call_args, stdout=subprocess.PIPE, universal_newlines=True
        ).stdout.rstrip()
