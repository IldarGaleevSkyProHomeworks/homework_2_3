import data_providers
import entities
import settings
import random


# ANSI Escape-последовательности для раскрашивания вывода
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
ESC_FG = '\x1B[38;5;{}m'
FG_RED = ESC_FG.format(1)
FG_GREEN = ESC_FG.format(2)
FG_MAGENTA = ESC_FG.format(5)
FG_RESET = '\x1B[0m'


def build_statistic(questions: list[entities.Question]):
    """
    Генерирует текст статистики на основании списка вопросов
    :param questions: Список вопросов
    :return: Строка с текстом-статистикой
    """

    right_answers_points_list = [question.points for question in questions if question.is_correct]
    return f"Вот и всё!\n" \
           f"Отвечено {len(right_answers_points_list)} вопроса из {len(questions)}\n" \
           f"Набрано баллов: {sum(right_answers_points_list)}"


def main(data_provider: data_providers.DataProvider):
    """
    Основной цикл приложения
    :param data_provider: Объект поставщика данных
    """

    # Получаем список вопросов от поставщика данных
    data_list = data_provider.getdata()

    # Создаем список вопросов с локализованной версией объекта Question
    questions_list = [
        entities.QuestionLocalizedRUS(
            item['q'],
            item['a'],
            int(item['d'])
        )
        for item in data_list]

    # Перемешиваем вопросы
    random.shuffle(questions_list)

    print(FG_MAGENTA + "Игра начинается!\n" + FG_RESET)

    for question in questions_list:
        print(question.build_question())

        question.user_answer = input("Ваш ответ: ").strip()
        is_correct = question.is_correct

        print((FG_RED, FG_GREEN)[is_correct] + question.build_feedback() + FG_RESET)
        print("-" * 10)

    print(FG_MAGENTA + build_statistic(questions_list) + FG_RESET)


def app_error(message: str):
    """
    Вывод текста ошибки на консоль
    :param message: Описание ошибки
    :return:
    """
    print(f"{FG_RED}Error: {message}{FG_RESET}")


if __name__ == '__main__':

    # Загрузка указанного в настройках поставщика данных
    match settings.USE_DATA_PROVIDER:
        case 'File':
            if not settings.DATA_FILENAME:
                app_error("Data filename not specified!")
                exit(1)

            app_data_provider = data_providers.JsonFileDataProvider(settings.DATA_FILENAME)

        case 'JsonKeeper':
            if not settings.DATA_JSONKEEPER_TOKEN:
                app_error("JsonKeeper file-id not specified!")
                exit(1)

            app_data_provider = data_providers.JsonKeeperDataProvider(settings.DATA_JSONKEEPER_TOKEN)

        case _:
            app_error("Unknown data provider!")
            exit(1)

    main(app_data_provider)
