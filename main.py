import logging

from loggers import SUCCESS, get_logger

logger = get_logger(__file__)

if __name__ == '__main__':
    logger.log(logging.NOTSET, "NOSET")
    logger.log(5, "5")
    logger.debug("debug")
    logger.info("Info")
    logger.log(SUCCESS, "Success")
    logger.warning("warn")
    logger.log(35, "35")
    logger.error("error")
    logger.critical("critical")
