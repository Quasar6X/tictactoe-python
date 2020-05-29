class Player:
    """
    Basic class for player objects.
    The program does not handle more then 2 players!
    """
    def_name_1 = "Player 1"
    def_name_2 = "AI"

    def __init__(self, name):
        self.score = 0
        self.name = name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
