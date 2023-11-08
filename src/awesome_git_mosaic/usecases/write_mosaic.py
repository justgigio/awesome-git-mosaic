from datetime import datetime

from awesome_git_mosaic.adapters.git_mosaic.git_mosaic_adapter import GitMosaicAdapter
from awesome_git_mosaic.gateways.git.git_gateway import GitGateway
from awesome_git_mosaic.usecases.modify_file import ModifyFile


class WriteMosaic:
    def __init__(
        self,
        git_mosaic_adapter: GitMosaicAdapter = None,
        git_gateway: GitGateway = None,
        modify_file: ModifyFile = None,
    ):
        """
        Class wich will get calculated timestamps, make commits and pushes

        :param git_mosaic_adapter: The adapater wich convert pixels to timestamp, defaults to GitMosaicAdapter
        :type git_mosaic_adapter: GitMosaicAdapter, optional
        :param git_gateway: The gateway wich will perform git actions, defaults to GitGateway
        :type git_gateway: GitGateway, optional
        :param modify_file: The usecase wich make files modifications to commit, defaults to ModifyFile
        :type modify_file: ModifyFile, optional
        """
        self.git_mosaic_adapter = git_mosaic_adapter or GitMosaicAdapter()
        self.git_gateway = git_gateway or GitGateway()
        self.modify_file = modify_file or ModifyFile()

    def write(
        self,
        message: str,
        strength: int = 15,
        multiply: int = 1,
        with_spaces: bool = True,
        background: bool = False,
        inverted: bool = False,
    ):
        """
        Perform commits and pushes, writing the message on mosaic

        :param message: The massage that will be written
        :type message: str
        :param strength: How many commits each pixel will have, defaults to 15
        :type strength: int, optional
        :param multiply: How many times the message will be written consecutively, defaults to 1
        :type multiply: int, optional
        :param with_spaces: if it will be spaces between the characters, defaults to True
        :type with_spaces: bool, optional
        :param background: if it will have bacjaground or not, defaults to False
        :type background: bool, optional
        :param inverted: if it will be inverted or not, defaults to False
        :type inverted: bool, optional
        """
        timestamps: list[datetime] = []
        if background:
            bgstr = " " * (len(message) * multiply)
            timestamps += self.git_mosaic_adapter.output(
                bgstr, None, with_spaces, True
            )

        for _ in range(strength):
            timestamps += self.git_mosaic_adapter.output(
                f"{message} " * multiply, None, with_spaces, inverted
            )

        timestamps.sort()

        total = len(timestamps)
        count = 0.0
        last_pct = 0

        print(f"Disabling git Garbage Collector...")
        self.git_gateway.disable_garbage_collector()

        print(f"Creating {total} commits...")
        for timestamp in timestamps:
            self.modify_file.modify(timestamp.ctime())
            self.git_gateway.add()
            self.git_gateway.commit(f"{timestamp.ctime()} {count}", timestamp)

            count += 1
            pct = round(count * 100 / total)

            if pct % 5 == 0 and pct != last_pct:
                print(f"{pct}%")
                last_pct = pct

            if count % 500 == 0:
                print(f"{count} commits created, pushing")
                self.git_gateway.push()

        print("All commits created. Last push...")
        self.git_gateway.push()

        print(f"Re-enabling git Garbage Collector...")
        self.git_gateway.enable_garbage_collector()

        print("That's all, folks! Bye!")
