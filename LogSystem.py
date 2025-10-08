from FileWriter import FileWriter
from ConfigReader import ConfigReader
class LogSystem:
    def __init__(self):
        pass

    def _SetLogConfig(self,path, config):
        fw = FileWriter(path, "w")
        fw.write("logtype=" + str(config.getlogtype()) + "\n" +
        "format=" + str(config.getformat()) + "\n" +
        "loglevel=" + str(config.getloglevel()) + "\n" +
        "logfilepath=" + str(config.getlogfilepath()) + "\n" +
        "maxlogsize=" + str(config.getmaxlogsize()))

    def _LoadLogConfig(self,path):
        cr = ConfigReader()
        config = cr.read_config(path)
        return config


    def setLogConfig(self, path, config):
        self._SetLogConfig(path, config)

    def loadLogConfig(self, path):
        config = self._LoadLogConfig(path)
        return config
