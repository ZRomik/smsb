from setup import SetupService
import logging
from aiogram import executor
from aiogram.utils.exceptions import *


async def startup(_):
    logging.info(
        "Бот запущен."
    )


async def shutdown(_):
    logging.info(
        "Бот остановлен."
    )


def main():
    """
    Запуск бота.
    """
    bot, dp = SetupService().setup_bot()
    if bot and dp:
        try:
            executor.start_polling(
                dispatcher=dp,
                on_startup=startup,
                on_shutdown=shutdown,
                skip_updates=True
            )
        except Unauthorized as e:
            logging.critical(
                "Во время запуска произошоа ошибка %s."
                " Проверьте усиановленный токен. Аварийное завершение работы!" % repr(e)
            )
            raise SystemExit(-1)
        except Exception as e:
            logging.critical(
                "Во время запуска произошоа ошибка %s."
                " Проверьте параметры запуска. Аварийное завершение работы!" % repr(e)
            )
            raise SystemExit(-1)


if __name__ == "__main__":
    main()
