import os
import shutil

from awesome_git_mosaic.usecases.modify_file import ModifyFile


class TestModifyFile:

    def test_file_is_modified(self):
        foldername = '.__testing_modify_folder'

        mf = ModifyFile(foldername)
        mf.modify('namespace')
        mf.modify('namespace')
        mf.modify('namespace', 'something')
        mf.modify('namespace2')

        assert len(os.listdir(foldername)) == 2
        assert len(os.listdir(os.path.join(foldername, 'namespace'))) == 3

        shutil.rmtree(foldername)
