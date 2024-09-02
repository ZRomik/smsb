from aiogram import Bot, Dispatcher
import logging
from aiogram.types import ParseMode
from ..config_setup import read_param
from helpers import Singleton

logger = logging.getLogger(__name__)


class BotService(Singleton):
    """
    Сервисный класс для ринициализации бота
    """

    def __init__(self):
        """
        Конструктор сервиса
        """
        super().__init__()
        logger.debug(
            "Инициализация сервисного класса."
        )
        # инициализация переменных для инстанцинации бота и диспетчера.
        self._bot = None
        self._disp = None

    def initialize(self) -> (Bot, Dispatcher):
        """
        Инициализация бота
        :param token: токен бота
        """
        if not self._bot and not self._disp:
            logger.debug(
                "Инициализация бота и деспетчера."
            )
            token = read_param("SMSB_TOKEN")
            try:
                self._bot = Bot(token=token, parse_mode=ParseMode.HTML)
                self._disp = Dispatcher(bot=self._bot)
            except Exception as e:
                logger.error(
                    "При инициализации бота произошла ошибка %s" % e,
                    exc_info=e
                )
                raise e
        return self._bot, self._disp

    @property
    def bot(self) -> Bot:
        """
        Возвращает инстанцированный экземпляр бота
        :return: Bot
        """
        return self._bot

    @property
    def dispatcher(self) -> Dispatcher:
        """
        Возвращает инстанцированный экземпляр диспетчера
        :return: Dispatcher
        """
        return self._disp

    @property
    def initialized(self) -> bool:
        """
        Возвращает True если бот и диспетчер инициализированы, иначе False
        """
        return self._bot is not None and self._disp is not None
