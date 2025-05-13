from typeguard import typechecked
import json
import random

@typechecked
class Question:

    def __init__(self, difficulty: str, category: str):
        self.__difficulty = difficulty
        self.__category = category
        self.__questions = self.__load_questions()

    def __load_questions(self):
        
        try:
            with open(self.__check_difficulty(), "rt", encoding = "utf-8") as file:
                data = json.load(file)
                return data[self.__category]
        except FileNotFoundError:
            pass

    def __check_difficulty(self):
        if self.__difficulty == "Difícil":
            return "Questions/hard_questions.json"
        elif self.__difficulty == "Media":
            return "Questions/medium_questions.json"
        else:
            return "Questions/easy_questions.json"

    def get_random_questions(self, num_questions: int = 10):

        random.shuffle(self.__questions)
        return self.__questions[:num_questions]
    