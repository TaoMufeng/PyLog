# Cache.py
from LogEnum import LogType
from Util import Util
import atexit


class Cache:
    _datalist = []
    _instance = None
    def __new__(cls, logtype=LogType.console, maxlogsize=1024 * 1024, filenum=1, path="log.txt"):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, logtype=LogType.console, maxlogsize=1024 * 1024, filenum=1, path="log.txt"):
        # 防止重复初始化
        if hasattr(self, "_initialized"):
            return
        atexit.register(lambda: self._flash())
        self._logtype = logtype
        self._logFilePath = path
        self._maxlogsize = maxlogsize
        self._number = filenum
        self._initialized = True

    def add(self, data):
        self._datalist.append(data)
        if len(self._datalist) >= 100:
            self._number = self._flash()
        return self._number

    def _get_current_path(self):
        return f"{Util.GetCurrentDay()}_{self._number}_{self._logFilePath}"

    def _flash(self):
        if not self._datalist:
            return self._number
        if self._logtype == "1":
            for data in self._datalist:
                print(data)
        elif self._logtype == "2":
            full_path = self._get_current_path()
            with open(full_path, "a", encoding="utf-8") as f:
                for data in self._datalist:
                    f.write(data)

            if Util.filesize(full_path) > self._maxlogsize:
                self._number += 1

        self._datalist.clear()
        return self._number