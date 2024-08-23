from .utils import read_param
import logging
from .exceptions import MissedRequiredParam, ImproperlyConfigured
import sys

def check_config_file(filenane: str = '.env'):

    logger = logging.getLogger(__name__)

    error_msg = "Отсутствует обязательноый параметр {}. Запуск невозможен."

    logger.info("Проверка конфигурации...")
    try:
        token = read_param(key='SMSB_TOKEN')
        db_type = read_param("SMSB_DB_TYPE")
        db_name = read_param("SMSB_DB_NAME")
        db_user = read_param("SMSB_DB_USER")
        db_pass = read_param('SMSB_DB_PASS')
        adm_cmd = read_param('SMSB_ADM')
        adm_pass = read_param('SMSB_ADM_PASS')
        sys_cmd = read_param('SMSB_SYS')
        sys_pass = read_param('SMSB_SYS_PASS')

        if not token:
            raise MissedRequiredParam(error_msg.format('SMSB_TOKEN'))
        if not db_type:
            raise MissedRequiredParam(error_msg.format('SMSB_DB_TYPE'))
        if db_type != "3":
            if not db_user:
                raise MissedRequiredParam(error_msg.format('SMSB_DB_USER'))
            if not db_pass:
                raise MissedRequiredParam(error_msg.format('SMSB_DB_PASS'))
        if not adm_cmd:
            raise MissedRequiredParam(error_msg.format('SMSB_ADM'))
        if not adm_pass:
            raise MissedRequiredParam(error_msg.format('SMSB_ADM_PASS'))
        if not sys_cmd:
            raise MissedRequiredParam(error_msg.format('SMSB_SYS'))
        if not sys_pass:
            raise MissedRequiredParam(error_msg.format('SMSB_SYS_PASS'))
    except MissedRequiredParam as e:
        logger.critical(e)
        sys.exit(-1)
    logger.info("Запуск бота...")
