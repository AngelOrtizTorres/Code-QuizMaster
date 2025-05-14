from __future__ import annotations
from Questions.question import Question
from GameEngine.player import Player
from GameEngine.menu import *
from typeguard import typechecked
import json

@typechecked
class Game:

    def __init__(self, player: Player, questions: Question, difficulty: str):
        self.__player = player
        self.__question = questions
        self.__difficulty = difficulty

    @property
    def player(self):
        return self.__player
    
    @property
    def question(self):
        return self.__question
    
    @property
    def difficulty(self):
         return self.__difficulty


    def evaluate_answer(self, answer, question: dict):
        try:
            user_answer_index = int(answer) - 1  
        except ValueError:
            return "incorrect"  
        
        correct = user_answer_index == question["respuesta"] - 1
        if correct:
            self.__player.score.add_score(5)
            return "correct"
        else:
            self.__player.lives.sub_lives(1)
            self.__apply_difficulty_penalty()
            return "incorrect"
        
    @staticmethod
    def get_top3_players(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                player = json.load(file)

            ordered_player = sorted(player, key=lambda x: (-x["score"], -x["lives"], x["used_hint"]))

            top3 = ordered_player[:3]
            return [f'{j["name"]} - {j["category"]} - {j["score"]} pts - {j["lives"]} vidas - {j["used_hint"]} pistas usadas'
                for j in top3]

        except FileNotFoundError:
            return [f"Archivo no encontrado: {file_path}"]
        except json.JSONDecodeError:
            return [f"No hay registro de partidas"]

    def __apply_difficulty_penalty(self):
        if self.__difficulty == "Difícil":
            self.__player.score.sub_score(3)
        elif self.__difficulty == "Media":
            self.__player.score.sub_score(2)
        else:
            self.__player.score.sub_score(1)

    def get_question_data(self):
        questions = self.__question.get_random_questions()
        return questions
    
    def consume_hint(self, answer: str, player: Player, question: dict):
        if answer == "S":
            if player.hint.has_hint():
                return f"{player.hint.see_hint(question)}"
            else:
                return "No te quedan más pistas\n"
        else:
            return "Decidiste no usar pistas para esta pregunta\n"

    @staticmethod
    def set_difficulty():
        while True:
            difficulty_option = difficulty_menu.choose()
            match difficulty_option:
                case 1:
                    return "Fácil"
                case 2:
                    return "Media"
                case 3:
                    return "Difícil"
                case _:
                    return "Para elegir la dificultad debe ser entre 1 y 3"

    @staticmethod
    def set_category():
        while True:
            category_option = category_menu.choose()
            match category_option:
                case 1:
                    return "Programación"
                case 2:
                    return "Historia"
                case 3:
                    return "Cultura General"
                case 4:
                    return "Geografía"
                case 5:
                    return "Deportes"
                case 6:
                    return "Videojuegos"
                case _:
                    return "Para elegir una categoría debe ser entre 1 y 6"