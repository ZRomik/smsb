from setup import setup_logging
import logging
from setup import load_config, check_required_params, BotService
from aiogram import executor

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
