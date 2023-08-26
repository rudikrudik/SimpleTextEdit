class DataFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding="utf8") as file:
            return file.read()

    def write(self, data):
        with open(self.path, 'w', encoding="utf8") as file:
            file.write(data)
