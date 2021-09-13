from loguru import logger

logger.add('debug.log', level='DEBUG')


def getLogger():
    return logger
