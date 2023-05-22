import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger = logging.getLogger('dingtalk2')
logger.addHandler(console)
logger.setLevel(logging.INFO)
