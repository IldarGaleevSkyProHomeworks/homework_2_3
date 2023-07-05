import data_providers.dataprovider as dp
import requests


class JsonKeeperDataProvider(dp.DataProvider):
    """Адаптер поставщика данных для загрузки данных из web-ресурса JsonKeeper"""

    JSON_KEEPER_URL = "https://www.jsonkeeper.com/b/"

    def __init__(self, json_file_id):
        """
        Конструктор адаптера
        :param json_file_id: Идентификатор Json-файла
        """
        super().__init__()
        self.__json_file_id = json_file_id

    def getdata(self):
        request = requests.get(self.JSON_KEEPER_URL + self.__json_file_id)
        self._data = request.json()

        return super().getdata()

    def __repr__(self):
        return f"JsonFileDataProvider(Token: '{self.__json_file_id}', Data: {self._data.__repr__()})"
