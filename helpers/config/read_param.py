from os import getenv
import logging


def read_param(key: str, default=None):
    """
    Считывает переданный параметр из окружения и возвращает результат.
    Если параметр отсутствует, возвращает значение по умолчанию.
    """
    return getenv(key, default)
