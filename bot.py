from setup import setup_logging
import logging
from setup import load_config, check_required_params, BotService
from aiogram import executor
from setup import DbService

logger = logging.getLogger(__name__)


async def startup(_):
    logger.info(
        "Бот запущен."
    )


async def shutdown(_):
    logger.info(
        "Бот остановлен."
    )


def main():
    """
    Запуск бота.
    """
    setup_logging()
    load_config()
    check_required_params()
    db = DbService().db
    try:
        db.connect()
    except Exception as e:
        logging.error(
            "Не удалось подключиться к базе данных. Запуск невозможен.",
            exc_info=True
        )
        raise SystemExit(-1)
    logger.info(
        "Подготовка к запуску..."
    )
    bot, disp = BotService().instances()
    executor.start_polling(
        dispatcher=disp,
        on_startup=startup,
        on_shutdown=shutdown
    )


if __name__ == "__main__":
    main()
