import logging

def setup_logging(level=logging.DEBUG):
    """
    Настройка логирования
    """
    # отключение отладочных сообщений библиотек peewee и aiogram
    logging.getLogger("peewee").setLevel(logging.ERROR)
    logging.getLogger("aiogram").setLevel(logging.ERROR)
    msg_fmt = "[%(asctime)-19s:%(msecs)-03d] %(levelname)-8s {%(filename)s %(funcName)s:%(lineno)d} > %(message)-s"
    date_fmt = "%d.%m.%Y в %H:%M:%S"
    formatter = logging.Formatter(fmt=msg_fmt, datefmt=date_fmt)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("errors.log", encoding='utf-8', mode='w')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.WARNING)

    logging.basicConfig(
        level=level,
        handlers=[
            console_handler,
            file_handler
        ]
    )