from datetime import datetime

from adapters.git_mosaic.git_mosaic_adapter import GitMosaicAdapter
from gateways.git.git_gateway import GitGateway
from usecases.modify_file import ModifyFile


class WriteMosaic:

    def __init__(self, git_mosaic_adapter: GitMosaicAdapter = None, git_gateway: GitGateway = None,
                 modify_file: ModifyFile = None):

        self.git_mosaic_adapter = git_mosaic_adapter or GitMosaicAdapter()
        self.git_gateway = git_gateway or GitGateway()
        self.modify_file = modify_file or ModifyFile()

    def write(self, message: str, strength: int = 5, multiply: int = 1, background: bool = False):

        timestamps = []
        if background:
            bgstr = '▉' * 100
            timestamps += self.git_mosaic_adapter.output(bgstr, datetime.now(), False)

        for i in range(strength):
            timestamps += self.git_mosaic_adapter.output(f'{message} ' * multiply)

        for timestamp in timestamps:
            print(f"Commit {timestamp}")
            self.modify_file.modify()
            self.git_gateway.add()
            self.git_gateway.commit(timestamp.ctime(), timestamp)

        self.git_gateway.push()

