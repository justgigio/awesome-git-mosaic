from typing import TYPE_CHECKING, Optional

from awesome_git_mosaic.charmaps.basic.basic_charmap import BasicCharmap

if TYPE_CHECKING:
    from awesome_git_mosaic.charmaps.charmap import Charmap


CONSOLE_PIXEL = "▉"
CONSOLE_SPACE = " "


class ConsoleAdapter:
    def __init__(self, charmap: Optional["Charmap"] = None):
        self.charmap = charmap or BasicCharmap()

    def output(self, message: str, with_spaces: bool = True) -> str:
        lines = self.charmap.translate(message, with_spaces)

        output = []
        for line in lines:
            output_line = ""
            for char in line:
                output_line += (
                    CONSOLE_PIXEL if self.charmap.is_pixel(char) else CONSOLE_SPACE
                )
            output.append(output_line)

        return "\n".join(output)
