import logging
from logging import handlers


_file: str = 'client'
format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
    )

logger = logging.getLogger(f'{_file}')

time_file_handler = logging.FileHandler(f'{_file}.log', encoding='utf-8')
time_file_handler.setLevel(logging.DEBUG)
time_file_handler.setFormatter(format)

logger.addHandler(time_file_handler)
logger.setLevel(logging.DEBUG)