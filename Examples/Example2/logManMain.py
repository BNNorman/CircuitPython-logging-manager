from LogManager import LogMan
LogMan.setFileStream("logMan.log","w")
Log=LogMan.getLogger("Main",LogMan.DEBUG)

Log.info("This is main")

import logManSub1


logManSub1.Sub1()

Log.info("This is main finishing")

LogMan.close()