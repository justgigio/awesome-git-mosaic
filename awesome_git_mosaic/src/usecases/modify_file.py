import uuid
from random import random


class ModifyFile:

    def __init__(self, filename: str = '.awesome_file'):
        self.filename = filename

    def modify(self, content: str = None):
        content = content or f"{uuid.uuid4()} {random()}"
        f = open(self.filename, "w+")
        f.write(content)
        f.close()
