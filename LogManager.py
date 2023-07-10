class LogMan:
    
    stream=None
    streambackup=None
    
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
   