import logging
from colorlog import ColoredFormatter

logger = logging.getLogger('filelogger2')
logger.setLevel(logging.INFO)          

handler = logging.FileHandler('info.log')
handler.setLevel(logging.INFO)
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)s: %(message)s",
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
)
handler.setFormatter(formatter)
logger.addHandler(handler)

def logInfo(message):
    logger.info(message)
