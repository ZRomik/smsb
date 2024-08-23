from aiogram import Bot, Dispatcher
from ..config_setup import read_param
import logging

logger = logging.getLogger(__name__)

logger.debug(
    "Подготовка к запуску."
)

bot = Bot(
    token=read_param("SMSB_TOKEN")
)

dp = Dispatcher(
    bot=bot
)

logger.debug(
    "Подготовка завершено. Запуск."
)