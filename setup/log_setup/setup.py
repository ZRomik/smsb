import sys
import logging

def configure_logging(level, disable_libs = True):
    """
    Настройка параметров журналирования
    """

    # отключение отладочных сообщений библиотек aiogram и peewee
    if disable_libs:
        logging.getLogger("aiogram").setLevel(logging.ERROR)
        logging.getLogger("peewee").setLevel(logging.ERROR)

    logger = logging.getLogger()

    msg_fmt = "[%(asctime)-20s] %(levelname)-8s %(message)-s"
    date_fmt = "%d.%m.%Y в %H:%M:%S"

    formatter = logging.Formatter(fmt=msg_fmt, datefmt=date_fmt)

    consolehandler = logging.StreamHandler(sys.stdout)
    consolehandler.setLevel(logging.DEBUG)
    consolehandler.setFormatter(formatter)

    filehandler = logging.FileHandler('logs\errors.log', encoding="utf-8", mode='w')
    filehandler.setLevel(logging.WARNING)
    filehandler.setFormatter(formatter)

    logger.addHandler(consolehandler)
    logger.addHandler(filehandler)
    logger.setLevel(level=level)