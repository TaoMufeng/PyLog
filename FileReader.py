class FileReader:
    def __init__(self):
        pass
    def read_line(self, path):
        with open(path, "r") as f:
            lines = f.readlines()
        return lines
