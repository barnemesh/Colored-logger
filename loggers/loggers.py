import logging
from logging.config import dictConfig
from pathlib import Path

from loggers import ColorHandler, CustomLevels

main_logger = logging.getLogger("main")
logging.basicConfig()

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
            '()': ColorHandler,
        },
    },
    'loggers': {
        'main': {
            'handlers': ['color_console'],
            'level': 'DEBUG',
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


main_logger.log(CustomLevels.SUCCESS, "==== TEST ====")
