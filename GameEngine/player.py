from typeguard import typechecked

@typechecked
class Player:

    def __init__(self, name: str, difficulty: str, category: str):
        self.__name = name
        self.__difficulty = difficulty
        self.__category = category
        self.__lives = Lives()
        self.__score = Score()
        self.__hint = Hint()

    @property
    def name(self):
        return self.__name

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def category(self):
        return self.__category
    
    @property
    def lives(self):
        return self.__lives
    
    @property
    def score(self):
        return self.__score
    
    @property
    def hint(self):
        return self.__hint

class Lives:

    def __init__(self):
        self.__lives = 3

    @property
    def lives(self):
        return self.__lives

    def sub_lives(self, lives: int):
        self.__lives -= lives
        
    def __str__(self):
        return f"{self.__lives}"

class Score:

    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        return self.__score

    def add_score(self, score: int):
        self.__score += score

    def sub_score(self, score: int):
        self.__score = max(0, self.__score - score)

    def __str__(self):
        return f"{self.__score}"
    
class Hint:

    def __init__(self):
        self.__hint = 3
        self.__used_hint = 0

    @property
    def used_hint(self):
        return self.__used_hint

    def see_hint(self, question):
        self.__used_hint += 1
        self.__hint -= 1
        return f"Pista: {question['pista']}\n"
    
    def has_hint(self):
        return self.__hint > 0