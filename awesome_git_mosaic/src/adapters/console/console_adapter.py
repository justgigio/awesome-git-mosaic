from charmaps.basic.basic_charmap import BasicCharmap

CONSOLE_PIXEL = '▉'
CONSOLE_SPACE = ' '


class ConsoleAdapter:

    def __init__(self, charmap = None):
        self.charmap = charmap or BasicCharmap()

    def output(self, message: str, with_spaces: bool = True) -> str:
        lines = self.charmap.translate(message, with_spaces)

        output = []
        for line in lines:
            output_line = ''
            for char in line:
                output_line += CONSOLE_PIXEL if self.charmap.is_pixel(char) else CONSOLE_SPACE
            output.append(output_line)

        return '\n'.join(output)
