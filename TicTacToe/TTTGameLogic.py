class Board():
    def __init__(self):
        self.n = 3
        # 1 for white, 0 for empty, -1 for black
        # we store all our pieces in two dimensional array
        self.pieces = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]

    def __getitem__(self, item):
        return self.pieces[item]

    def can_move(self, x, y):
        if self.pieces[x][y] == 0:
            return True
        else:
            return False

    def get_all_legal_moves(self, color):
        moves = set()
        for x in range(self.n):
            for y in range(self.n):
                if self[x][y] == 0:
                    moves.add((x, y))
        return list(moves)

    def are_any_moves_possible(self):
        for x in range(self.n):
            for y in range(self.n):
                if self[x][y] == 0:
                    return True
        return False

    def is_win(self, color):
        for y in range(self.n):
            count = 0
            for x in range(self.n):
                if self[x][y] == color:
                    count += 1
            if count == 3:
                return True

        for x in range(self.n):
            count = 0
            for y in range(self.n):
                if self[x][y] == color:
                    count += 1
            if count == 3:
                return True

        count = 0
        for diagonal in range(self.n):
            if self[diagonal][diagonal] == color:
                count += 1
        if count == 3:
            return True
        count = 0
        for diagonal in range(self.n):
            if self[diagonal][self.n - diagonal-1] == color:
                count += 1
        if count == 3:
            return True
        return False

    def move(self, move, color):
        x, y = move
        assert self[x][y] == 0
        self[x][y] = color
