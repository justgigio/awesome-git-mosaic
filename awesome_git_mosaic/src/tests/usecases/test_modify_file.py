import os

from usecases.modify_file import ModifyFile


class TestModifyFile:

    def test_file_is_modified(self):
        filename = '.__testing_modify_file'
        initial_content = 'initial content'

        f = open(filename, 'w+')
        f.write(initial_content)
        f.close()

        mf = ModifyFile(filename)
        mf.modify()

        f = open(filename, 'r')
        actual_content = f.read()
        f.close()

        os.remove(filename)

        assert initial_content != actual_content
