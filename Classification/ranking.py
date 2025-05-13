from __future__ import annotations
from GameEngine.player import Player
import json
import os

class Ranking:

    def __init__(self, player: Player, difficulty: str, category: str):
        self.__player = player
        self.__difficulty = difficulty
        self.__category = category

    @property
    def player(self):
        return self.__player

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def category(self):
        return self.__category
        
    def append_to_leaderboard(self):
        file_path = self.get_leaderboard_file_path()

        new_entry = {
            "name": self.player.name,
            "category": self.category,
            "score": self.player.score.score,
            "lives": self.player.lives.lives,
            "used_hint": self.player.hint.used_hint
        }

        self.update_leaderboard(file_path, new_entry)
        
    def get_leaderboard_file_path(self):
        if self.__difficulty == "Difícil":
            return "Classification/HardMode.json"
        if self.__difficulty == "Media":
            return "Classification/MediumMode.json"
        else:
            return "Classification/EasyMode.json"
        
    def load_leaderboard(self, file_location):
        if os.path.exists(file_location) and os.path.getsize(file_location) > 0:
            with open(file_location, "rt", encoding="utf-8") as file:
                try:
                    leaderboard = json.load(file)
                except json.JSONDecodeError:
                    leaderboard = []
        else:
            leaderboard = []
        
        return leaderboard

    def update_leaderboard(self, file_location, score_data):
        leaderboard = self.load_leaderboard(file_location)
        leaderboard.append(score_data)

        with open(file_location, "wt", encoding="utf-8") as file:
            json.dump(leaderboard, file, ensure_ascii = False, indent = 4)