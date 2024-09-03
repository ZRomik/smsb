from peewee import *
from helpers import Singleton
import logging
from setup import read_param
from .exceptions import DatabaseNotSupportedError

logger = logging.getLogger(__name__)

class DbService(Singleton):
    """
    Класс сервис для управления подключением к БД
    """
    def __init__(self):
        """
        Инициализация сервиса и подключение к БД
        """
        super().__init__()
        # logger.debug(
        #     "Инициализация сервиса %s. Создание подключения к БД." % self.__class__.__name__
        # )
        db_type = read_param('SMSB_DB_TYPE')
        db_name = read_param('SMSB_DB_NAME')
        db_user = read_param('SMSB_DB_USER')
        db_pass = read_param('SMSB_DB_PASS')
        db_host = read_param('SMSB_DB_HOST', 'localhost')
        if db_type == "1":
            logger.debug(
                "Выбрана БД PostgreSQL."
            )
            db_port = read_param('SMSB_DB_PORT', 5432)
            self._db = PostgresqlDatabase(
                database=db_name,
                user=db_user,
                password=db_pass,
                port=db_port,
                host='localhost'
            )
            # self._db = PostgresqlDatabase(
            #     database=db_name,
            #     user=db_user,
            #     password=db_pass,
            #     host=db_host,
            #     port=db_port,
            # )
        elif db_type == "2":
            logger.debug(
                "Выбрана БД MySQL."
            )
            db_port = read_param('SMSB_DB_PORT', 3306)
            self._db = MySQLDatabase(
                database=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port=db_port,
            )
        elif db_type == "3":
            logger.debug(
                "Выбрана БД SQLite."
            )
            self._db = SqliteDatabase(database=db_name)
            logger.debug(type(self._db))
        else:
            logger.error(
                "Неверный тип БД (%s)" % db_type,
                exc_info=False
            )
            raise DatabaseNotSupportedError(db_type)

    @property
    def db(self):
        return self._db