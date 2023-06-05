import logging

from termcolor import colored

SUCCESS = 25

LEVEL_TO_COLOR = {
    logging.NOTSET: ('grey', None, None),
    logging.DEBUG: ('blue', None, None),
    logging.INFO: ('white', None, None),
    SUCCESS: ('white', 'on_green', ['bold', 'blink']),
    logging.WARNING: ('yellow', None, ['bold']),
    logging.ERROR: ('red', None, ['bold']),
    logging.CRITICAL: ('red', 'on_white', ['bold', 'blink']),
}


def get_colored_params(record):
    return LEVEL_TO_COLOR.get(record.levelno, get_color_for_unknown_level(record))


def get_color_for_unknown_level(record):
    last_key = LEVEL_TO_COLOR[logging.NOTSET]
    for key in LEVEL_TO_COLOR.keys():
        if key <= record.levelno:
            last_key = key
            continue
        return LEVEL_TO_COLOR.get(last_key)
    return LEVEL_TO_COLOR.get(last_key)


class ColorHandler(logging.StreamHandler):

    def emit(self, record: logging.LogRecord) -> None:
        record.msg = colored(record.msg, *get_colored_params(record))
        super().emit(record)
