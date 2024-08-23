import logging
from setup import configure_logging, check_config_file, dp
from aiogram import executor

configure_logging(logging.INFO)
check_config_file()

logger = logging.getLogger(__name__)

async def startup(_):
    logger.info("Бот запущен.")

async def shutdown(_):
    logger.info("Бот остановлен.")

def main():
    executor.start_polling(
        dispatcher=dp,
        on_startup=startup,
        on_shutdown=shutdown,
        skip_updates=True,
    )

if __name__ == "__main__":
    main()