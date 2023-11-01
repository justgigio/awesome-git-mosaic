import subprocess

from datetime import datetime
from pytest import fixture
from unittest.mock import MagicMock

from awesome_git_mosaic.gateways.git.git_gateway import GitGateway


class TestGitGateway:

    @fixture
    def gateway(self):
        gg = GitGateway()
        gg._git = MagicMock()
        return gg

    def test_add(self, gateway):
        gateway.add('some_file')

        gateway._git.assert_called_with('add', 'some_file')

    def test_commit(self, gateway):
        gateway.commit('some message', datetime(1990, 8, 28, 10, 23, 37))
        gateway._git.assert_called_with('commit', '-m"some message"', '--date', '"Tue Aug 28 10:23:37 1990"')

    def test_push(self, gateway):
        gateway.push('branch')
        gateway._git.assert_called_with('push', 'origin', 'branch')

    def test__git(self):
        subprocess.run = MagicMock()
        gateway = GitGateway()

        gateway._git('status')

        subprocess.run.assert_called_with(['git', 'status'], stdout=subprocess.PIPE, universal_newlines=True)
