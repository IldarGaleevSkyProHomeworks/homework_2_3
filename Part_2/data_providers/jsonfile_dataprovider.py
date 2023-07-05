import data_providers.dataprovider as dp
import json


class JsonFileDataProvider(dp.DataProvider):
    """Адаптер поставщика данных для загрузки данных из файла"""

    def __init__(self, filename):
        """
        Конструктор адаптера
        :param filename: Путь к файлу с данными
        """

        super().__init__()
        self.__filename = filename

    def getdata(self) -> list:
        with open(self.__filename, 'r', encoding='utf-8') as file:
            self._data = json.load(file)

        return super().getdata()

    def __repr__(self):
        return f"JsonFileDataProvider(Filename: '{self.__filename}', Data: {self._data.__repr__()})"
