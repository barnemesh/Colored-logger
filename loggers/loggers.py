import logging
from logging.config import dictConfig
from pathlib import Path

main_logger = logging.getLogger("main")

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            '()': 'loggers.ColorHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console'],
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


main_logger.info("==== TEST ====")
