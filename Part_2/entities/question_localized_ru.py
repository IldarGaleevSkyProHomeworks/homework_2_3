import entities.question


class QuestionLocalizedRUS(entities.question.Question):
    """Переопределение класса Question с локализованными строками для методов  build_question и build_feedback"""

    def __init__(self, question: str, right_answer: str, difficulty: int, max_award: float = 50):
        super().__init__(question, right_answer, difficulty, max_award)

    def build_question(self) -> str:
        self._is_asked = True
        return f"Вопрос: {self._question}\n" \
               f"Сложность: {self._difficulty}/{self.MAX_DIFFICULTY}"

    def build_feedback(self) -> str | None:
        if self._is_asked:
            match self.is_correct:
                case True:
                    return f"Ответ верный, {self._award} очков заработано"
                case False:
                    return f"Ответ неверный, правильный ответ: {self._right_answer}"
        return None
