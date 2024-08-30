class RequiredParamNotExistsError(Exception):
    """
    Исключение возбуждается, если в файле конфигурации отсутствует обязательный параметр
    """
    def __init__(self, param: str):
        return super().__init__("Отсутствует обяззательный параметр %s. Запуск невозможен." % param)