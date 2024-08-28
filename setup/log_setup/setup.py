import logging

def setup_logging(level=logging.DEBUG):
    """
    Настройка логирования
    """
    msg_fmt = "[%(asctime)-19s] %(levelname)-8s {%(funcName)-s} [%(module)-s] %(message)-s"
    date_fmt = "%d.%m.%Y %H:%M:%S"
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