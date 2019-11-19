import logging
from logging import handlers


_file: str = 'server'
format = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
    )

logger = logging.getLogger(f'{_file}')

time_file_handler = handlers.TimedRotatingFileHandler(
    f'{_file}.log', when='d', interval=1
    )
time_file_handler.setLevel(logging.DEBUG)
time_file_handler.setFormatter(format)

logger.addHandler(time_file_handler)
logger.setLevel(logging.DEBUG)


class Log():

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f'{inspect.stack()[1][3]} | '
                        f'input args: {args} and kwargs: {kwargs}')

            return func(*args, *kwargs)

        return wrapper