import os
import time


class Util:
    @staticmethod
    def GetCurrentDay():
        return time.strftime("%Y%m%d", time.localtime())
    @staticmethod
    def trim(str):
        return str.strip()
    @staticmethod
    def replace(str, old, new):
        return str.replace(old, new)
    @staticmethod
    def filesize(path):
        return os.path.getsize(path)

    @staticmethod
    def GetCurrentTime():
        return time.strftime("%H:%M:%S", time.localtime())
