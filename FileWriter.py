class FileWriter:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
    def write(self, data):
        with open(self.path, self.mode) as f:
            f.write(data)
