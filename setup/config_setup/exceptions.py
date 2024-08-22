class MissedRequiredParam(Exception):
    """
    Исключение возбуждается вслучае отсутствия обязательного параметра в файле конфигурации
    """
class ImproperlyConfigured(Exception):
    """
    Исключение возбуждается в случае неверной кофигурации бота.
    """