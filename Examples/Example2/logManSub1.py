from LogManager import LogMan
log=LogMan.getLogger("sub1",LogMan.DEBUG)

import logManSub2

log.info("Sub1 loading")

def Sub1():
    global log
    for l in range(5):
        log.info(f"sub1 Sub1() {l}")
        log.info("going into Sub2")
        logManSub2.Sub2()