from TicTacToe import DataParser
from TicTacToe.Game import Game

if __name__ == '__main__':
    DataParser.read_tic_tac_toe_data()
    game_state = ['x', 'x', 'x', 'x', 'o', 'o', 'b', 'o', 'b']
    print(DataParser.is_game_end(game_state))
    game = Game('o')
    game.new_game()
    print(game.board)
    print(game.move(game.natural_language_to_coordinates('topLeft')))
    print(game.move(game.natural_language_to_coordinates('topLeft')))
    game.board = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    game.is_game_over()
    print(game.natural_language_to_coordinates('topRight'))
