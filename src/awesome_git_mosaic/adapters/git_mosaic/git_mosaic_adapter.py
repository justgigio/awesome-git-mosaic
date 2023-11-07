from datetime import datetime, timedelta
from random import randint
from typing import List, Optional, TYPE_CHECKING

from awesome_git_mosaic.charmaps.basic.basic_charmap import BasicCharmap

if TYPE_CHECKING:
    from awesome_git_mosaic.charmaps.charmap import Charmap


class GitMosaicAdapter:

    def __init__(self, charmap: Optional['Charmap'] = None):
        self.charmap = charmap or BasicCharmap()

    def output(self, message: str, reference_day: Optional[datetime] = None, with_spaces: bool = True, background: bool = False) -> List[datetime]:
        reference_day = reference_day or datetime.today()
        lines = self.charmap.translate(message, with_spaces, background)

        output = []
        y_offset = 0
        for line in lines:
            x_offset = 0
            for char in line:
                if self.charmap.is_pixel(char):
                    output.append(self._timestamp_for_pixel(x_offset, y_offset, reference_day))
                x_offset += 1
            y_offset += 1

        return output

    def _timestamp_for_pixel(self, x_offset: int, y_offset: int, reference_day: datetime) -> datetime:
        last_sunday = reference_day - timedelta(days=reference_day.weekday() + 1)
        top_left_square = last_sunday - timedelta(weeks=51)

        target_date = top_left_square + timedelta(weeks=x_offset) + timedelta(days=y_offset) + timedelta(microseconds=randint(0, 300))
        return target_date
