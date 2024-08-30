from aiogram import Bot, Dispatcher
import logging
from ..config_setup import read_param, load_config


def setup_bot(token: str = None) -> (Bot, Dispatcher):
    """
    Инстанцинация бота и диспетчера
    :param token: (string) токен бота
    :return: инстанцинированные экземпляры бота и диспетчера
    """
    logger = logging.getLogger(__name__)
    if token is None:
        load_config()
        token = read_param('SMSB_TOKEN')
    try:
        logger.debug(
            "Инстанцинация бота."
        )
        bot = Bot(token=token)
        logger.debug(
            "Инстанцинация диспетчера."
        )
        disp = Dispatcher(bot=bot)
    except Exception as e:
        logger.error(
            "Ошибка при инициализации бота: %s" % e,
            exc_info=e
        )
        raise SystemExit(-1)
    return bot, disp