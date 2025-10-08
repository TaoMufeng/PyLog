from LogEnum import LogLevel, LogType
class Config:
    def __init__(self, loglevel, logtype, logfilepath, maxlogsize, format):
        self._loglevel = loglevel
        self._logtype = logtype
        self._logfilepath = logfilepath
        self._maxlogsize = maxlogsize
        self._format = format
    # getters 不用@property
    #_Getters 写内部实现
    #getter写外部接口
    def _Getloglevel(self):
        return self._loglevel
    def _Getlogtype(self):
        return self._logtype
    def _Getlogfilepath(self):
        return self._logfilepath
    def _Getmaxlogsize(self):
        return self._maxlogsize
    def _Getformat(self):
        return self._format
    def getloglevel(self):
        return self._Getloglevel()
    def getlogtype(self):
        return self._Getlogtype()
    def getlogfilepath(self):
        return self._Getlogfilepath()
    def getmaxlogsize(self):
        return self._Getmaxlogsize()
    def getformat(self):
        return self._Getformat()
    def _Setloglevel(self, loglevel):
        self._loglevel = loglevel
    def _Setlogtype(self, logtype):
        self._logtype = logtype
    def _Setlogfilepath(self, logfilepath):
        self._logfilepath = logfilepath
    def _Setmaxlogsize(self, maxlogsize):
        self._maxlogsize = maxlogsize
    def _Setformat(self, format):
        self._format = format
    def setloglevel(self, loglevel):
        self._Setloglevel(loglevel)
    def setlogtype(self, logtype):
        self._Setlogtype(logtype)
    def setlogfilepath(self, logfilepath):
        self._Setlogfilepath(logfilepath)
    def setmaxlogsize(self, maxlogsize):
        self._Setmaxlogsize(maxlogsize)
    def setformat(self, format):
        self._Setformat(format)
