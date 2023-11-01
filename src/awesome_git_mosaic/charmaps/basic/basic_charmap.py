from os import path

from unidecode import unidecode

CHARMAP_PIXEL = 'o'


class BasicCharmap:

    def __init__(self, model_file: str = None, char_width: int = 5, char_height: int = 7,
                 char_list: str = ' abcdefghijklmnopqrstuvwxyz0123456789#'):
        if not model_file:
            current_dir = path.dirname(path.abspath(__file__))
            model_file = path.join(current_dir, 'char_model.txt')
        self.chars = self._load_char_model(model_file, char_width, char_height, char_list)

    def translate(self, string: str, with_spaces: bool = True, background: bool = False):
        string = unidecode(string).lower()
        mapped_chars = [self.chars[c] for c in string]

        if with_spaces:
            space = '#' if background else ' '
        else:
            space = ''
        output = []

        for line in range(len(mapped_chars[0])):
            output.append(space.join([''.join(char[line]) for char in mapped_chars]))

        return output

    def is_pixel(self, char: str):
        return char == CHARMAP_PIXEL

    def _load_char_model(self, model_file: str, char_width: int, char_height: int, char_list: int):

        f = open(model_file, 'r')
        lines = f.read().splitlines(keepends=False)
        f.close()

        char_map = {c: [] for c in char_list}

        line_number = 0
        for line in lines:
            if line == '':
                continue

            char_line = line_number % char_height
            char_index = line_number // char_height

            char = char_list[char_index]
            char_map[char].append(list(line))

            line_number += 1

        return char_map
