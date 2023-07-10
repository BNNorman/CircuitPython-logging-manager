from LogManager import LogMan

assert LogMan.stream is not None,"Log stream has not been setup"

log=LogMan.getLogger("SUB",0)

def getL