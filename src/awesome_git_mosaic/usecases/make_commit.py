from datetime import datetime, timedelta

from awesome_git_mosaic.gateways.git.git_gateway import GitGateway


class MakeCommit:
    def __init__(self, git_gateway: GitGateway = None):
        self.git_gateway = git_gateway or GitGateway()

    def make_commit(self):
        return NotImplemented
