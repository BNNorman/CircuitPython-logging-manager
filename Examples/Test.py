# logging test
from LogManager import LogMan
LogMan.setFileStream("LogManager.log")
Log0=LogMan.getLogger("MAIN",LogMan.DEBUG)
Log0.info("Starting LogManager test")

class subclass1():
    def __init__(self):
        log1=LogMan.getLogger("subclass1")
        log1.setLevel(LogMan.INFO)
        log1.info("subclass1  starting")
    
class subclass2():
    def __init__(self):
        log2=LogMan.getLogger("subclass2")
        log2.setLevel(LogMan.DEBUG)
        log2.debug("subclass2  starting")

print(f"LogMan.WARNING {LogMan.WARNING}")

Log0.info("testLogging starting")

s1=subclass1()
s2=subclass2()

Log0.info("testLogging finished")
LogMan.close()