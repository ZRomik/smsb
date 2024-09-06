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
    SetupService()
    bot, dp = SetupService().setup_bot()
    db = SetupService().setup_connection()
    if db.is_closed():
        db.connect()
    if bot and dp:
        try:
            executor.start_polling(
                dispatcher=dp,
                on_startup=startup,
                on_shutdown=shutdown,
                skip_updates=True
            )
        except Unauthorized:
            logging.critical(
                "Во время запуска произошоа ошибка. Проверьте усnановленный токен. Аварийное завершение работы!"
            )
            raise SystemExit(-1)
        except Exception as e:
            logging.critical(
                "Во время запуска произошоа ошибка %s."
                " Проверьте параметры запуска. Аварийное завершение работы!" % str(e)
            )
            raise SystemExit(-1)
    else:
        logging.critical(
            "Не удалось инициализировать бот. Проверьте параметры в файле конфигурации."
        )


if __name__ == "__main__":
    main()
