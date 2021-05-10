import uuid


class ModifyFile:

    def __init__(self, filename: str = '.awesome_file'):
        self.filename = filename

    def modify(self, content: str = None):
        content = content or str(uuid.uuid4())
        f = open(self.filename, "w+")
        f.write(content)
        f.close()
