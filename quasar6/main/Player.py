class Player:
    """
    Basic class for player objects.
    The program does not handle more then 2 players!
    """
    def_name_1 = "Player"
    def_name_2 = "AI"

    def __init__(self, name):
        self.score = 0
        self.name = name
