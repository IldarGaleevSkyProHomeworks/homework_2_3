# Описание объектов

- `data_providers` - Поставщики данных
    - `DataProvider` - Базовый клас поставщика данных
    - `JsonFileDataProvider` - Адаптер загружает данные из Json-файла
    - `JsonKeeperDataProvider` - Адаптер загружает данные с ресурса [JsonKeeper](https://www.jsonkeeper.com/)

- `entities` - Объекты приложения
    - `Question` - Объект вопроса
    - `QuestionLocalizedRUS` - Объект-обертка: русифицирует вывод объекта `Question`

# Файл настроек

Приложение хранит настройки в файле [settings.py](/Part_2/settings.py)

- `DATA_FILENAME` - Путь к файлу с данными. По умолчанию [Data/questions.json](/Part_2/Data/questions.json)
- `DATA_JSONKEEPER_TOKEN` = Идентификатор Json-файла, выданный [JsonKeeper](https://www.jsonkeeper.com/). По умолчанию: `ZLRH`
- `USE_DATA_PROVIDER` - Указание поставщика данных. Одно из значений:

|  Значение  | Поставщик данных       |
|:----------:|:-----------------------|
|   `File`   |`JsonFileDataProvider`  |
|`JsonKeeper`|`JsonKeeperDataProvider`|