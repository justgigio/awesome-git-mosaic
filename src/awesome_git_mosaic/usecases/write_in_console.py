from awesome_git_mosaic.adapters.console.console_adapter import ConsoleAdapter


class WriteInConsole:

    def __init__(self, console_adapter: ConsoleAdapter = None):
        self.console_adapter = console_adapter or ConsoleAdapter()

    def write(self, text: str, with_spaces: bool = True):
        output = self.console_adapter.output(text, with_spaces)
        print(output)
