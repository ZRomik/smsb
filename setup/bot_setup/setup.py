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
        super().__init__()
        token = read_param('SMSB_TOKEN')
        self._bot = Bot(token=token, parse_mode=ParseMode.HTML)
        self._disp = Dispatcher(bot=self._bot)

    def instances(self) -> (Bot, Dispatcher):
        """
        Возвращает инстанцированные классы бота и диспетчера.
        """
        return self._bot, self._disp

    @property
    def bot(self) -> Bot:
        """
        Возвращает инстанцированный экземпляр бота.
        """
        return self._bot

    @property
    def disp(self) -> Dispatcher:
        """
        Возвращает инстанцированный экземпляр диспетчера.
        """
        return self._disp