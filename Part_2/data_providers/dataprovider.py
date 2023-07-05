class DataProvider:
    """Базовый класс поставщика данных"""

    def __init__(self):
        self._data = []

    def getdata(self) -> list:
        """Получить данные"""

        return self._data

    def __str__(self):
        return '\n'.join([str(item) for item in self._data])

    def __repr__(self):
        return f"DataProvider (data: {self._data.__repr__()})"
