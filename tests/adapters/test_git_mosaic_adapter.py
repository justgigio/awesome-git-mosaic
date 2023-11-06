from datetime import datetime, timedelta
from unittest.mock import MagicMock

from awesome_git_mosaic.charmaps.basic.basic_charmap import BasicCharmap
from awesome_git_mosaic.adapters.git_mosaic.git_mosaic_adapter import GitMosaicAdapter


class TestGitMosaicAdapter:

    def test_output(self):
        charmap = BasicCharmap()
        charmap.translate = MagicMock(return_value=['o'])

        adapter = GitMosaicAdapter(charmap)

        reference_day = datetime.today()
        last_sunday = reference_day - timedelta(days=reference_day.weekday() + 1)
        top_left_square = last_sunday - timedelta(weeks=51)

        output = adapter.output('x', reference_day)

        assert len(output) == 1
        assert output[0] > top_left_square
        assert output[0] < top_left_square + timedelta(microseconds=301)
