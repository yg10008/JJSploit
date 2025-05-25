import logging
from logging.handlers import RotatingFileHandler

ygLogs = logging.getLogger("fileLogger")
ygLogs.setLevel(logging.DEBUG)

logFile = RotatingFileHandler("ygLogs.log", maxBytes=5*1024*1024, backupCount=5)
logFile.setLevel(logging.DEBUG)

format = logging.Formatter('%(asctime)s / %(levelname)s / %(message)s')
logFile.setFormatter(format)

ygLogs.addHandler(logFile)
