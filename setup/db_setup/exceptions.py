class DatabaseNotSupportedError(Exception):
    """
    Исключение возбуждается, если не поддерживается выбранный тип базы данных
    """
    def __init__(self, db_type: str):
        return super().__init__("Не поддерживается выбранный тип базы данных (%s). Запуск невозможен." % db_type)