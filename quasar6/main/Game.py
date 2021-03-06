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
        Field.__instance = self
        self.SIZE = 3
        self.FIELD = [["_"] * self.SIZE for _ in range(self.SIZE)]

    def set_field_symbol(self, i, j):
        if self.FIELD[i][j] != '_':
            return False

        self.FIELD[i][j] = 'X' if p_turn == "X" else 'O'
        return True

    def print_field(self):
        """
        Prints the game field to the console only used for debugging purposes!
        """
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
        string_col = ""
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] != "_":
                    string_row += self.FIELD[i][j]
                    if len(string_row) == self.SIZE:
                        valid = self.valid(string_row)
                        if valid is not False:
                            return valid
                        string_row = ""
                if self.FIELD[j][i] != "_":
                    string_col += self.FIELD[j][i]
                    if len(string_col) == self.SIZE:
                        valid = self.valid(string_col)
                        if valid is not False:
                            return valid
                        string_col = ""
            string_row = ""
            string_col = ""
        diag_p = ""
        diag_s = ""
        count_ = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.FIELD[i][j] == "_":
                    count_ += 1
                    continue
                if i == j:
                    diag_p += self.FIELD[i][j]
                if i + j == self.SIZE - 1:
                    diag_s += self.FIELD[i][j]

        if len(diag_p) == self.SIZE:
            if diag_p == "X" * self.SIZE:
                return "X"
            elif diag_p == "O" * self.SIZE:
                return "O"
        if len(diag_s) == self.SIZE:
            if diag_s == "X" * self.SIZE:
                return "X"
            elif diag_s == "O" * self.SIZE:
                return "O"
        if count_ == 0:
            return "draw"
        return "No match"

    def reset_field(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.FIELD[i][j] = "_"

    def max(self, alpha, beta):
        max_score = -2
        px, py = (None, None)
        result = self.result()
        if result is not False:
            return result

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
        result = self.result()
        if result is not False:
            return result

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

    def result(self):
        result = self.is_match()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == 'draw':
            return 0, 0, 0
        return False

    def valid(self, chars):
        if chars == "X" * self.SIZE:
            return "X"
        elif chars == "O" * self.SIZE:
            return "O"
        return False
