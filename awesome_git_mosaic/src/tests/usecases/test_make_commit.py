from usecases.make_commit import MakeCommit


class TestMakeCommit:

    def test_make_commit(self):
        mc = MakeCommit()

        result = mc.make_commit()

        assert result == NotImplemented
