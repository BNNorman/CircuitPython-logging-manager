# CircuitPython-logging-manager

This manager allows imported submodules to share the same logfile and to identify which submodule (Logger name) emitted the log entry. Awfully useful for debugging.

A simple example shows the log message is prepended with the logger name as used with getLogger("NAME").

```
3128.740: MAIN INFO - Calling SUB
3128.842: SUB INFO - SUB getLogStream <FileHandler object at 0x2000b170>
3128.941: MAIN INFO - Finished
```

CAVEAT: The log manager file stream must be setup before any sub modules using it are imported e.g.

```
from LogManager import LogMan
LogMan.setFileStream("LogMan.log","a")

import SUB
```
To get a logger you then call the LogManager method, also called, getLogger(). You can,optionally, set the numeric logging level at the same time.

```
log=LogMan.getLogger("MAIN",<optional level>)
```
The adafruit_logging default level is WARNING so you might not see any log messages till you lower it. By default the LogManager sets the level to zero so all messages are displayed - useful while debugging.

Log levels can be set using LogMan.INFO, LogMan.DEBUG etc.

# Setting all loggers to the same level

In a project where sub-modules use the LogManager and are onverted to MPY files , changing the logging level of submodules would require you to edit the PY files, cross compile them and upload it to the device.

Also when development is complete you probably want to set the level of all loggers to either INFO or WARNING.

The setAllLoggerLevels() method allows you to set all the LogManager users in one command from the main module.

```
LogMan.setAllLoggerLevels(<LEVEL>)
```

# Closing the log

It is necessary to close the log to ensure pending messages are written to the log file.

```
LogMan.close()
```

# Adafruit_logging changes
Get a copy of adafruit_logging.py from the latest bundle then modify line 168 and change it from
```
return f"{record.created:<0.3f}: {record.levelname} - {record.msg}"
```
to
```
return f"{record.created:<0.3f}: {record.name} {record.levelname} - {record.msg}"
```
# Log message types

I have experienced adafruit_logging crashing when trying to log some byte arrays. The trick is to convert the message to a list :-

```
msg=b'....'
log.debug(f"something went wrong {list(msg)}")
```
It's more readable anyway.


