from LogManager import LogMan
LogMan.setFileStream("LogMan.log","a")


import SUB


log=LogMan.getLogger("MAIN",0)
log.info("Calling SUB")

SUB.getLogStream()

log.info("Finished")�/����`����������	� 	��������	��	��	��	� 
� 
�@
�`
��
��