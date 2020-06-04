import inspect
import logging


def customLogger(logLevel):
    # get class/method name
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode="w")
    fileHandler.setLevel(logLevel)

    formtter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formtter)
    logger.addHandler(fileHandler)

    return logger
