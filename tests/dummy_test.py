from loggers import get_logger


def test():
    logger = get_logger(__file__)
    logger.info("TEST")