import adafruit_logging as logging

class LogMan:
    
    stream=None
    streambackup=None

    # logging levels
    NOTSET=logging.NOTSET
    DEBUG=logging.DEBUG
    INFO=logging.INFO
    WARNING=logging.WARNING
    ERROR=logging.ERROR
    CRITICAL=logging.CRITICAL

    
    @staticmethod
    def setNullHandler():
        if LogMan.streambackup is None:
            LogMan.streambackup=LogMan.stream
        LogMan.stream=logging.NullHandler()
        
    @staticmethod
    def restoreLastHandler():
        if LogMan.streambackup is not None:
            LogMan.stream=logMan.streambackup
            logMan.streambackup=None
        
        
    @staticmethod
    def setFileStream(filename,mode="a"):
        """Must be called first immediately after importing LogManager and before importing other modules which use LogManager"""
        assert type(filename) is str,"Expected a string for the filename"
        
        try:
            LogMan.stream=open(filename,mode)
			LogMan.handler=logging.StreamHandler(stream)
        except Exception as e:
            print(f"Unable to create a file stream {e}")
            raise
            
    @staticmethod
    def getLogger(name,level=None):
		assert LogMan.stream is not None,"LogManager stream must be created first with LogMan.setFileStream(<log file name>)"
        assert level is int and level>=0,"getLogger optional level parameter must be an int>=0"
        log=logging.getLogger(name)
        log.addHandler(LogMan.handler)
        log.setLevel(level)
        return log

    @staticmethod
    def close():
        LogMan.stream.close() # flushes the stream