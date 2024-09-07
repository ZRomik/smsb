from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from helpers import Singleton
import logging
import sys
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .exceptions import RequiredParamNotExistsError
from peewee import *


class SetupService(Singleton):
    """
    Класс сервис для настройки приложения
    """

    def __init__(self, level=logging.DEBUG):
        self.__setup_logging(level=level)

    def __read_param(self, key: str, default=None):
        """
        Читает переданный параметр в файле конфигурации и возвращает прочитанное значение.
        Если параметр отсутствует возвращается значение по умолчанию
        """
        logging.debug(
            "Чтение параметра %s." % repr(key)
        )
        return os.getenv(key, default)

    def __check_config(self):

        logging.debug(
            "Проверка файла конфигурации."
        )

        bot_token = self.__read_param('SMSB_TOKEN')
        db_type = self.__read_param('SMSB_DB_TYPE')
        adm_cmd = self.__read_param('SMSB_ADM')
        adm_pass = self.__read_param('SMSB_ADM_PASS')
        sys_cmd = self.__read_param('SMSB_SYS')
        sys_pass = self.__read_param('SMSB_SYS_PASS')
        db_name = self.__read_param('SMSB_DB_NAME')
        db_user = self.__read_param('SMSB_DB_USER')
        db_pass = self.__read_param('SMSB_DB_PASS')

        try:
            if not bot_token:
                raise RequiredParamNotExistsError("SMSB_TOKEN")
            if not db_type:
                raise RequiredParamNotExistsError("SMSB_DB_TYPE")
            if not db_name:
                raise RequiredParamNotExistsError("SMSB_DB_NAME")
            if not adm_cmd:
                raise RequiredParamNotExistsError("SMSB_ADM")
            if not adm_pass:
                raise RequiredParamNotExistsError("SMSB_ADM_PASS")
            if not sys_cmd:
                raise RequiredParamNotExistsError("SMSB_SYS")
            if not sys_pass:
                raise RequiredParamNotExistsError("SMSB_SYS_PASS")
            if db_type != "3":
                if not db_user:
                    raise RequiredParamNotExistsError("SMSB_DB_USER")
                if not db_pass:
                    raise RequiredParamNotExistsError("SMSB_DB_PASS")
        except RequiredParamNotExistsError as e:
            logging.critical(msg=e, exc_info=False)
            raise SystemExit(-1)

        logging.debug(
            "Завершена."
        )

    def __load_config(self, filename=".env") -> bool:
        """
        Возвращает истину, если файл конфигурации найден и загружен, иначе возвращает ложь
        :param filename: (str) - имя файл конфигурации (по умрлчанию .env)
        :return: (bool) - результат выполнения
        """
        logging.debug(
            "Загрузка конфигурации."
        )
        return load_dotenv(filename)

    def setup_bot(self) -> (Bot, Dispatcher):
        logging.info("Подготовка к запуску.")
        self.__load_config()
        self.__check_config()
        bot_token = self.__read_param('SMSB_TOKEN')
        logging.debug(
            "Подготовка к запуску бота."
        )
        try:
            self._bot = Bot(
                token=bot_token,
                parse_mode=ParseMode.HTML
            )
            self._dp = Dispatcher(
                bot=self._bot
            )
        except Exception as e:
            logging.critical(
                "При инициализации бота произоша ошибка %s! Запск невозможен!" % e
            )
            raise SystemExit(-1)
        return self._bot, self._dp

    def __setup_logging(self, level=logging.DEBUG):
        """
        Настройка журналирования
        """
        # отключение отладочных сообщений библиотек peewee и aiogram
        logging.getLogger("aiogram").setLevel(logging.ERROR)
        logging.getLogger("peewee").setLevel(logging.ERROR)

        # настройка формата сообщения
        detailed_fmt = "[%(asctime)s.%(msecs)-03d] %(levelname)-8s {%(module)s (%(funcName)s):[%(lineno)d]} : %(message)s"
        brief_fmt = "[%(asctime)s.%(msecs)-03d] %(levelname)-8s %(message)s"
        date_fmt = "%d.%m.%Y в %H:%M:%S"
        detailed_formatter = logging.Formatter(fmt=detailed_fmt, datefmt=date_fmt)
        brief_formatter = logging.Formatter(fmt=brief_fmt, datefmt=date_fmt)

        # настройка обработчиков
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(brief_formatter)

        file_handler = RotatingFileHandler(
            os.path.join('logs', 'errors.log'),
            encoding="utf-8",
            mode="w",
            maxBytes=5 * 1024 * 1024
        )
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(detailed_formatter)

        # настройка журнала
        logging.basicConfig(
            level=level,
            handlers=[
                console_handler,
                file_handler
            ]
        )

    def setup_connection(self):
        """
        Настройка соединения с БД
        """
        logging.debug(
            'Настройка соединения с БД.'
        )
        db_type = self.__read_param('SMSB_DB_TYPE')
        db_host = self.__read_param('SMSB_DB_HOST', 'localhost')
        db_user = self.__read_param('SMSB_DB_USER')
        db_pass = self.__read_param('SMSB_DB_PASS')
        db_name = self.__read_param('SMSB_DB_NAME')
        if db_type == "1":  # postgres
            db_port = self.__read_param('SMSB_DB_PORT', 5432)
            self._db = PostgresqlDatabase(
                database=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port=db_port
            )
        elif db_type == "2":  # mysql
            db_port = self.__read_param('SMSB_DB_PORT', 3306)
            self._db = MySQLDatabase(
                database=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
            )
        elif db_type == "3":  # sqlite
            self._db = SqliteDatabase(
                database=db_name,
                pragmas={'foreign_keys': 1})  # применение ограничений внешнего ключа
        logging.info(
            "Попытка подключения к БД."
        )
        self._db.connect()
        logging.info(
            "Соединение с БД установлено."
        )
        return self._db
