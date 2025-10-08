import threading

import LogEnum
from Cache import Cache
from Util import Util
import inspect
from LogEnum import LogType
class Log:
    _instance = None
    _fileNum = 1
    _currentDay = ""
    _loglevel = LogEnum.LogLevel.debug
    _format = "{time} - {level} - {content} - {file}:{line}"
    _logtype = LogEnum.LogType.console
    _logFilePath = ""
    _maxlogsize = 1024
    def __init__(self):
        pass
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def _LogMsg(self, msg, level, thread_id, file, line):
        print(self._loglevel)
        if level < int(self._loglevel):
            return
        if self._currentDay != Util.GetCurrentDay():
            self._currentDay = Util.GetCurrentDay()
            self._fileNum = 1
        logmsg = Util.trim(self._format)
        logmsg = Util.replace(logmsg, "{time}", self._currentDay + " " + Util.GetCurrentTime())
        logmsg = Util.replace(logmsg, "{thread_id}", str(thread_id))
        logmsg = Util.replace(logmsg, "{file}", file)
        logmsg = Util.replace(logmsg, "{line}", str(line))
        logmsg = Util.replace(logmsg, "{content}", msg)
        logmsg = Util.replace(logmsg, "{level}", self._levelMap(level))
        logmsg += "\n"
        cache = Cache(self._logtype, self._maxlogsize, self._fileNum, self._logFilePath)
        self._fileNum = cache.add(logmsg)
    def _levelMap(self, level):
        if level == 1:
            return "debug"
        elif level == 2:
            return "info"
        elif level == 3:
            return "warn"
        elif level == 4:
            return "error"
        elif level == 5:
            return "fatal"
        else:
            return "debug"
    def _SetLogLevel(self, level):
        self._loglevel = level

    def _SetLogType(self, logtype):
        self._logtype = logtype

    def _SetLogPath(self, logpath):
        self._logFilePath = logpath

    def _SetMaxLogSize(self, maxlogsize):
        self._maxlogsize = maxlogsize

    def _SetFormat(self, format):
        self._format = format

    def setLogLevel(self, level):
        self._SetLogLevel(level)

    def setLogType(self, logtype):
        self._SetLogType(logtype)

    def setFormat(self, format):
        self._SetFormat(format)

    def setMaxLogSize(self, maxlogsize):
        self._SetMaxLogSize(maxlogsize)

    def setFilePath(self, logpath):
        self._SetLogPath(logpath)

    def logMsg(self, msg, level):
        self._LogMsg(msg, level, threading.current_thread().ident,
                     inspect.currentframe().f_back.f_code.co_filename, inspect.currentframe().f_back.f_lineno)
    def debug(self, msg):
        self.logMsg(msg, LogEnum.LogLevel.debug)
    def info(self, msg):
        self.logMsg(msg, LogEnum.LogLevel.info)
    def warn(self, msg):
        self.logMsg(msg, LogEnum.LogLevel.warn)
    def error(self, msg):
        self.logMsg(msg, LogEnum.LogLevel.error)
    def fatal(self, msg):
        self.logMsg(msg, LogEnum.LogLevel.fatal)
