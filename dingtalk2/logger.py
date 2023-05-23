import sys

from loguru import logger

LOGGER_FORMAT = '<green>{time:YYYY-MM-DD HH:mm:ss}</green> [ <level>{level: <8}</level> ] <level>{message}</level>'
# LOGGER_FORMAT = '[ <level>{level: <8}</level> ] <level>{message}</level>'

logger.remove(0)
logger.add(sys.stdout, level='INFO', format=LOGGER_FORMAT, filter='dingtalk2')
