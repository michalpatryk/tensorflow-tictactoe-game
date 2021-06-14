from TicTacToe import DataParser
from TicTacToe.Game import Game

if __name__ == '__main__':
    DataParser.read_tic_tac_toe_data()
    game_state = ['x', 'x', 'x', 'x', 'o', 'o', 'b', 'o', 'b']
    print(DataParser.is_game_end(game_state))
    game = Game('o')
    game.new_game()
    print(game.board)
    print(game.move('topLeft'))
    print(game.move('topLeft'))
    game.board = {'topLeft': 'x', 'topCenter': 'x', 'topRight': 'x',
                  'middleLeft': 'x', 'middleCenter': 'o', 'middleRight': 'o',
                  'bottomLeft': 'b', 'bottomCenter': 'o', 'bottomRight': 'b'}
    game.is_game_over()
