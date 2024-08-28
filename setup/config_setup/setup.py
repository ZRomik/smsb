from os import getenv
from dotenv import load_dotenv
import logging
from .exceptions import RequiredParamNotExistsError

logger = logging.getLogger(__name__)

def load_config(filename: str = '.env'):
    """
    Загружает из файла конфигурации параметры для запуска бота
    """
    load_dotenv(filename)

def read_param(key: str, default: str = None) -> str | None:
    """
    Возвращает прочитанное значение параметра или None, если параметра не существует
    :param key: (str) имя параметра
    :param default: (str) возвращаемое значение по умолчанию
    :return: (str) прочитанное значение или None
    """
    logger.debug(
        "Чтение параметра %s." % repr(key)
    )
    return getenv(key, default)

def check_required_params(filename: str = None):
    logger.info(
        "Проверка параметров для запуска."
    )

    if filename:
        load_config(filename)

    bot_token = read_param('SMSB_TOKEN')
    db_type = read_param('SMSB_DB_TYPE')
    adm_cmd = read_param('SMSB_ADM')
    adm_pass = read_param('SMSB_ADM_PASS')
    sys_cmd = read_param('SMSB_SYS')
    sys_pass = read_param('SMSB_SYS_PASS')
    db_name = read_param('SMSB_DB_NAME')
    db_user = read_param('SMSB_DB_USER')
    db_pass = read_param('SMSB_DB_PASS')

    if not bot_token:
        raise RequiredParamNotExistsError("SMSB_TOKEN")
    if not db_type:
        raise RequiredParamNotExistsError("SMSB_DB_TYPE")
    if not db_name:
        raise RequiredParamNotExistsError("SMSB_DB_NAME")
    if db_type != "3":
        if not db_user:
            raise RequiredParamNotExistsError("SMSB_DB_USER")
        if not db_pass:
            raise RequiredParamNotExistsError("SMSB_DB_PASS")
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

    logger.info(
        "Проверка параметров успешно завершена."
    )