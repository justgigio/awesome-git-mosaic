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
        timestamps: list[datetime] = []
        if background:
            bgstr = " " * (len(message) * multiply)
            timestamps += self.git_mosaic_adapter.output(
                bgstr, datetime.today(), with_spaces, True
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
