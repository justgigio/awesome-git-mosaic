from datetime import datetime, timedelta
from unittest.mock import MagicMock, ANY, call

from pytest import fixture

from awesome_git_mosaic.charmaps.basic.basic_charmap import BasicCharmap
from awesome_git_mosaic.adapters.git_mosaic.git_mosaic_adapter import GitMosaicAdapter
from awesome_git_mosaic.usecases.write_mosaic import WriteMosaic


class MessageStartsWith(str):
    def __eq__(self, other):
        return other.startswith(self)


class TimestampNextTo(datetime):
    def __eq__(self, other):
        return other > self and other < (self + timedelta(seconds=2))


class TestWriteInConsole:

    @fixture
    def gateway(self):
        gg = MagicMock()
        gg.commit = MagicMock()
        gg.disable_garbage_collector = MagicMock()
        gg.add = MagicMock()
        gg.push = MagicMock()
        gg.enable_garbage_collector = MagicMock()
        return gg
    
    @fixture
    def modify_file(self):
        mf = MagicMock()
        mf.modify = MagicMock()
        return mf

    def test_write(self, gateway: MagicMock, modify_file: MagicMock):
        charmap = BasicCharmap()
        charmap.translate = MagicMock(return_value=['o ', ' o'])

        adapter = GitMosaicAdapter(charmap)
        usecase = WriteMosaic(adapter, gateway, modify_file)

        reference_day = datetime.today()
        last_sunday = reference_day - timedelta(days=reference_day.weekday() + 1)
        top_left_square = last_sunday - timedelta(weeks=51)
        second_square = top_left_square + timedelta(days=8)

        usecase.write('x', 2)

        gateway.disable_garbage_collector.assert_called_once()
        assert modify_file.modify.call_count == 4
        assert gateway.add.call_count == 4

        calls = [
            call(MessageStartsWith(top_left_square.ctime()), TimestampNextTo.fromtimestamp(top_left_square.timestamp())),
            call(MessageStartsWith(top_left_square.ctime()), TimestampNextTo.fromtimestamp(top_left_square.timestamp())),
            call(MessageStartsWith(second_square.ctime()), TimestampNextTo.fromtimestamp(second_square.timestamp())),
            call(MessageStartsWith(second_square.ctime()), TimestampNextTo.fromtimestamp(second_square.timestamp())),
        ]

        gateway.commit.assert_has_calls(calls)

        assert gateway.commit.call_count == 4
        gateway.push.assert_called_once()
        gateway.enable_garbage_collector.assert_called_once()
