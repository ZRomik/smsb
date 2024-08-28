from setup import setup_logging
import logging

def main():
    """
    Подготовка и запуск бота.
    """
    logger = logging.getLogger(__name__)
    logger.debug("info сообщение до настройки")
    setup_logging()
    logger.info("info сообщение после настройки")
    logger.debug("debug сообщение после настройки")

if __name__ == "__main__":
    main()