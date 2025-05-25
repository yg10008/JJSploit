import logging
from colorlog import ColoredFormatter

logger = logging.getLogger('fileLogger')
logger.setLevel(logging.ERROR)

handler = logging.FileHandler('error.log')
handler.setLevel(logging.ERROR)
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

def logError(message):
    logger.error(message)
