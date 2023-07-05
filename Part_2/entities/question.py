class Question:
    """Объект, представляющий вопрос"""

    MAX_DIFFICULTY = 5

    def __init__(self, question: str, right_answer: str, difficulty: int, max_award: float = 50):
        """
        Конструктор вопроса
        :param question: Текст вопроса
        :param right_answer: Текст верного ответа
        :param difficulty: Сложность вопроса
        :param max_award: Максимальное вознаграждение
        """
        self._question = question
        self._right_answer = right_answer
        self._difficulty = min(difficulty, self.MAX_DIFFICULTY)
        self._award = round((self._difficulty / self.MAX_DIFFICULTY) * max_award)

        self._is_asked = False
        self._user_answer = None

    @property
    def user_answer(self):
        """Ответ пользователя"""

        return self._user_answer

    @user_answer.setter
    def user_answer(self, value):
        self._user_answer = value

    @property
    def is_correct(self) -> bool | None:
        """
        Возвращает результат проверки ответа на правильность
        :return: Результат проверки, либо None - если на вопрос не отвечали
        """
        if self._is_asked:
            return self._right_answer.lower() == self._user_answer.lower()

        return None

    @property
    def points(self) -> int:
        """
        Возвращает количество начисляемых очков за правильный ответ
        :return:
        """
        return self._award

    def build_question(self) -> str:
        """Возвращает текст вопроса, помечает вопрос как "Заданный" """

        self._is_asked = True
        return f"Question: {self._question}\n" \
               f"Difficulty: {self._difficulty}/{self.MAX_DIFFICULTY}"

    def build_feedback(self) -> str | None:
        """Возвращает текст с результатом проверки, либо None - если на вопрос не отвечали"""

        if self._is_asked:
            match self.is_correct:
                case True:
                    return f"Right, {self._award} points earned"
                case False:
                    return f"Wrong, right answer: {self._right_answer}"
        return None

    def __str__(self):
        return self._question

    def __repr__(self):
        return f"Question(Text: '{self._question}', " \
               f"Right answer: '{self._right_answer}', " \
               f"Difficulty: {self._difficulty}, " \
               f"Award: {self._award}, " \
               f"User answer: {self._user_answer}, " \
               f"Is asked: {self._is_asked})"
