from os import path
from typing import Optional

from unidecode import unidecode

from awesome_git_mosaic.charmaps.charmap import Charmap

CHARMAP_PIXEL = 'o'


class BasicCharmap(Charmap):

    def __init__(self, model_file: Optional[str] = None, char_width: int = 5, char_height: int = 7,
                 char_list: str = ' abcdefghijklmnopqrstuvwxyz0123456789#') -> None:
        if not model_file:
            current_dir = path.dirname(path.abspath(__file__))
            model_file = path.join(current_dir, 'char_model.txt')
        self.chars = self._load_char_model(model_file, char_width, char_height, char_list)

    def translate(self, string: str, with_spaces: bool = True, background: bool = False) -> list:
        string = unidecode(string).lower()
        mapped_chars = [self.chars[c] for c in string]

        if with_spaces:
            space = CHARMAP_PIXEL if background else ' '
        else:
            space = ''
        output = []

        for line in range(len(mapped_chars[0])):
            output.append(space.join([''.join(char[line]) for char in mapped_chars]))

        return output

    def is_pixel(self, char: str) -> bool:
        return char == CHARMAP_PIXEL

    def _load_char_model(self, model_file: str, char_width: int, char_height: int, char_list: str) -> dict[str, list[list]]:

        f = open(model_file, 'r')
        lines = f.read().splitlines(keepends=False)
        f.close()

        char_map: dict[str, list[list]] = {}

        for char_index, char in enumerate(char_list):
            char_map[char] = []

            for i in range(char_height):
                char_line = i + char_index + (char_height * char_index)

                char_map[char].append(list(lines[char_line][:char_width]))

        return char_map
