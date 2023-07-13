from LogManager import LogMan
log=LogMan.getLogger("sub2",LogMan.DEBUG)

log.info("Sub2 loading")

def Sub2():
    global log
    for i in range(5):
        log.debug(f"sub2 Sub2() {i}")
    log.info("Sub2 finished")