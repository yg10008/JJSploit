import logging

consoleLogger = logging.getLogger("consoleLogger")
consoleLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
format = logging.Formatter('%(asctime)s / %(levelname)s / %(message)s')
consoleHandler.setFormatter(format)


logfile = logging.FileHandler("consoleLogs.log")
logfile.setLevel(logging.DEBUG)


consoleLogger.addHandler(consoleHandler)
consoleLogger.addHandler(logfile)