from . import DataParser
class Game:
    def __init__(self, current_player='x'):
        self.board = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        self.current_player = current_player

    @staticmethod
    def natural_language_to_coordinates(location):
        return {
            'topLeft': 0,
            'topCenter': 1,
            'topRight': 2,
            'middleLeft': 3,
            'middleCenter': 4,
            'middleRight': 5,
            'bottomLeft': 6,
            'bottomCenter': 7,
            'bottomRight': 8
        }.get(location, False)

    def new_game(self, starting_player='x'):
        self.board = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        self.current_player = starting_player
        print("Starting new game")

    def can_move(self, position):
        try:
            if self.board[position] == 'b':
                return True
            else:
                return False
        except KeyError:
            return False

    def move(self, position):
        if self.can_move(position):
            self.board[position] = self.current_player
            if self.current_player == 'o':
                self.current_player = 'x'
            else:
                self.current_player = 'o'
            return True, "Moved"
        else:
            return False, "Cant move"

    def is_game_over(self):
        print(DataParser.is_game_end(self.board))
