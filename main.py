import datetime
import logging
import structlog

def example_logging_basic():
    # default simple setup
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('example')

    logger.info("""example_logging_basic:

# default simple setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('example')
""")

    # test logging
    logger.log(logging.NOTSET, 'this is a notset log')
    logger.debug('this is a debug log')
    logger.info('this is an info log')
    logger.warning('this is a warning log')
    logger.error('this is an error log')
    logger.critical('this is a critical log')

    logger.info('end of example_logging_basic')


def example_logging_structured():
    # structlog setup
    logger = structlog.get_logger()
    logger.info("""example_logging_structured:

# structlog setup
structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = structlog.get_logger()
""")

    # test logging
    logger.debug('this is a debug log')
    logger.info('this is an info log')
    logger.warning('this is a warning log')
    logger.error('this is an error log')
    logger.critical('this is a critical log')

    logger.info('end of example_logging_structured')


if __name__ == '__main__':
    example_logging_basic()

    # show the example for structured logging
    example_logging_structured()