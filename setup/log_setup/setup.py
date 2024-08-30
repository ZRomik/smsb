import logging

def setup_logging(level=logging.DEBUG):
    """
    Настройка логирования
    """
    # отключение отладочных сообщений библиотек peewee и aiogram
    logging.getLogger("peewee").setLevel(logging.ERROR)
    logging.getLogger("aiogram").setLevel(logging.ERROR)
    detailed_fmt = "[%(asctime)-19s.%(msecs)-03d] %(levelname)-8s {%(module)-s.%(funcName)-s:%(lineno)-02d (%(pathname)-s)} : %(message)s"
    brief_fmt = "[%(asctime)-19s.%(msecs)-03d] %(levelname)-8s : %(message)s"
    date_fmt = "%d.%m.%Y в %H:%M:%S"
    detailed_formatter = logging.Formatter(fmt=detailed_fmt, datefmt=date_fmt)
    brief_formatter = logging.Formatter(fmt=brief_fmt, datefmt=date_fmt)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(brief_formatter)
    console_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("errors.log", encoding='utf-8', mode='w')
    file_handler.setFormatter(detailed_formatter)
    file_handler.setLevel(logging.WARNING)

    logging.basicConfig(
        level=level,
        handlers=[
            console_handler,
            file_handler
        ]
    )