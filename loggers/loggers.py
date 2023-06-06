import logging
from logging.config import dictConfig
from pathlib import Path

from loggers import ColorHandler

main_logger = logging.getLogger("main")

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s.%(msecs)03d] %(levelname)-7s %(message)s [%(name)s.%(module)s:%(lineno)d]'
        },
    },
    'handlers': {
        'color_console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            '()': lambda *args, **kwargs: ColorHandler(*args, **kwargs),
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['color_console'],
            'level': 'DEBUG',
            'propegate': False  # This is if any other package calls logging.basicConfig(), or changes the root
        },
    }
}

dictConfig(LOGGING_CONFIG)


def get_logger(name):
    p = Path(name)
    if p.exists():
        name = p.stem
    logger = main_logger.getChild(name)
    return logger


main_logger.info("==== TEST ====")
