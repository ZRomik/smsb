import logging
class Singleton:
    """
    Реализация паттерна Одиночка
    """
    def __init__(self, *args, **kwargs):
        super().__init__()
        logging.debug(
            "Инициализация %s" % self.__class__.__name__
        )
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance