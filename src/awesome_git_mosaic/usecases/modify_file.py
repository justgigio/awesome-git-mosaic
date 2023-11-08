import os
import uuid
from typing import Optional

FOLDER_NAME = ".awesome_folder"


class ModifyFile:
    def __init__(self, folder_name: str = FOLDER_NAME):
        self.folder_name = folder_name
        self._mkdir()

    def modify(self, namespace: str = "default", content: Optional[str] = None):
        path = self._mkdir(namespace)
        filename = str(uuid.uuid4())
        content = content or filename

        self._write(path, filename, content)

    def _mkdir(self, name: str = "") -> str:
        path = os.path.join(self.folder_name, name)
        if not os.path.exists(path):
            os.mkdir(path)

        return path

    def _write(self, path: str, filename: str, content: str):
        f = open(os.path.join(path, filename), "w+")
        f.write(content)
        f.close()
