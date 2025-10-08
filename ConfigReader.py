from Util import Util
from LogEnum import LogType, LogLevel
from FileReader import FileReader
from Log import Log

class ConfigReader:
    def __init__(self):
        pass
    @staticmethod
    def read_config(path):
        reader = FileReader()
        lines = reader.read_line(path)
        config = {}
        for line in lines:
            line = Util.trim(line)
            if line.startswith("#") or line == "":
                continue
            key, value = line.split("=")
            config[key.strip()] = value.strip()
        return config
