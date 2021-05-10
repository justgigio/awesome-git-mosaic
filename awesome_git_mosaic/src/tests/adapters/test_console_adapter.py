from unittest.mock import MagicMock

from charmaps.basic.basic_charmap import BasicCharmap
from adapters.console.console_adapter import ConsoleAdapter, CONSOLE_PIXEL, CONSOLE_SPACE


class TestConsoleAdapter:

    def test_write(self):
        charmap = BasicCharmap()
        charmap.translate = MagicMock(return_value=['o '])

        adapter = ConsoleAdapter(charmap)
        output = adapter.output('test')

        assert output == f'{CONSOLE_PIXEL}{CONSOLE_SPACE}'
