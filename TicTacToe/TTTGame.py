from . import DataParser


class TTTGame:
    def __init__(self, current_player='x'):
        self.board = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
        self.board_dimensions = 3
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

    def get_board_size(self):
        return self.board_dimensions, self.board_dimensions

    def get_action_size(self):
        return self.board_dimensions * self.board_dimensions + 1

