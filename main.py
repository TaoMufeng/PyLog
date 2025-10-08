import Cache
from Config import Config
from LogEnum import LogLevel, LogType
from LogSystem import LogSystem
from Log import Log


def main():
    # config = Config(LogLevel.debug, LogType.console, "log.txt",
    #                 1024, "{level} - {content} - {file}:{line}")
    ls = LogSystem()
    # ls.setLogConfig(path="D:/Project/PythonProject/Log/config.txt", config=config)
    reconfig = ls.loadLogConfig(path="D:/Project/PythonProject/Log/config.txt")

    l = Log()
    l.setLogType(reconfig["logtype"])
    l.setLogLevel(reconfig["loglevel"])
    l.setFormat(reconfig["format"])
    l.setFilePath(reconfig["logfilepath"])
    l.setMaxLogSize(int(reconfig["maxlogsize"]))
    l.info("hello world")
if __name__ == "__main__":
    main()
