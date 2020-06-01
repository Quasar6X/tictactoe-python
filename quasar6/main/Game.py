p_turn = "X"


class Field:
    """
    Singleton class for the N*N tic-tac-toe field
    """
    __instance = None

    @staticmethod
    def get_instance():
        if Field.__instance is None:
            Field()
        return Field.__instance

    def __init__(self):
        if Field.__instance is not None:
            raise Exception("Do not instantiate!")
        else:
            Field.__instance = self
        self.SIZE = 3
        self.FIELD = [["_"] * self.SIZE for _ in range(self.SIZE)]

    def set_field_symbol(self, i, j):
        if self.FIELD[i][j] != '_':
            return False

        self.FIELD[i][j] = 'X' if p_turn == "X" else 'O'
        return True

    def print_field(self):
        print(" " * (74 - int(self.SIZE / 2 + int((self.SIZE + 1) / 2))), end="")
        print("-" * (self.SIZE * 2 + 3))
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if j == 0:
                    print(" " * (74 - int(self.SIZE / 2 + int((self.SIZE + 1) / 2))), end="")
                    print("| " + self.FIELD[i][j], end=" ")
                elif j == self.SIZE - 1:
                    print(self.FIELD[i][j], end=" |")
                else:
                    print(self.FIELD[i][j], end=" ")
            print()
        print(" " * (74 - int(self.SIZE / 2 + int((self.SIZE + 1) / 2))), end="")
        print("-" * (self.SIZE * 2 + 3))

    def is_match(self):
        string_row = ""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] == "_":
                    continue
                string_row += self.FIELD[i][j]
                if len(string_row) == self.SIZE:
                    if string_row == "XXX":
                        return "X"
                    elif string_row == "OOO":
                        return "O"
                    else:
                        string_row = ""
            string_row = ""
        string_col = ""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[j][i] == "_":
                    continue
                string_col += self.FIELD[j][i]
                if len(string_col) == self.SIZE:
                    if string_col == "XXX":
                        return "X"
                    elif string_col == "OOO":
                        return "O"
                    else:
                        string_col = ""
            string_col = ""
        diag_p = []
        diag_s = []
        count_ = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] == "_":
                    count_ += 1
                    continue
                if i == j:
                    diag_p.append(self.FIELD[i][j])
                if i + j == self.SIZE - 1:
                    diag_s.append(self.FIELD[i][j])

        if len(diag_p) == self.SIZE:
            if diag_p.count(diag_p[0]) == len(diag_p):
                return diag_p[0]
        if len(diag_s) == self.SIZE:
            if diag_s.count(diag_s[0]) == len(diag_s):
                return diag_s[0]
        if count_ == 0:
            return "draw"
        return "Invalid game state!"

    def reset_field(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.FIELD[i][j] = "_"

    def get_size(self):
        return self.SIZE

    def get_symbol_at(self, i, j):
        return self.FIELD[i][j]

    def max(self, alpha, beta):
        max_score = -2
        px, py = (None, None)
        result = self.is_match()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == 'draw':
            return 0, 0, 0

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] == "_":
                    self.FIELD[i][j] = "O"
                    (m, min_i, min_j) = self.min(alpha, beta)

                    if m > max_score:
                        max_score = m
                        px = i
                        py = j
                    self.FIELD[i][j] = "_"

                    if max_score >= beta:
                        return max_score, px, py
                    alpha = max(max_score, alpha)
        return max_score, px, py

    def min(self, alpha, beta):
        min_score = 2
        qx, qy = (None, None)
        result = self.is_match()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == 'draw':
            return 0, 0, 0

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] == "_":
                    self.FIELD[i][j] = "X"
                    (m, max_i, max_j) = self.max(alpha, beta)

                    if m < min_score:
                        min_score = m
                        qx = i
                        qy = j
                    self.FIELD[i][j] = "_"

                    if min_score <= alpha:
                        return min_score, qx, qy
                    min_score = min(min_score, beta)
        return min_score, qx, qy
