from unittest.mock import MagicMock, patch

from charmaps.basic.basic_charmap import BasicCharmap
from adapters.console.console_adapter import ConsoleAdapter, CONSOLE_PIXEL, CONSOLE_SPACE
from usecases.write_in_console import WriteInConsole


class TestConsoleAdapter:

    @patch("builtins.print")
    def test_write(self, mock_print):
        charmap = BasicCharmap()
        charmap.translate = MagicMock(return_value=['o ', ' o'])

        adapter = ConsoleAdapter(charmap)
        usecase = WriteInConsole(adapter)

        usecase.write('xxx')

        mock_print.assert_called_with(f'{CONSOLE_PIXEL}{CONSOLE_SPACE}\n{CONSOLE_SPACE}{CONSOLE_PIXEL}')
