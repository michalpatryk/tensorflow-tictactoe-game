from .TTTGameLogic import Board
import numpy as np
class Game():

    def __init__(self):
        self.n = 3  # dimensions

    def getInitBoard(self):
        b = Board()
        return np.array(b.pieces)

    def getBoardSize(self):
        return self.n, self.n

    def getActionSize(self):
        return self.n * self.n + 1

    def getNextState(self, board, player, action):
        if action == self.n * self.n:
            return board, -player
        b = Board()
        b.pieces = np.copy(board)
        move = (int(action / self.n), action % self.n)
        b.move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        valids = [0] * self.getActionSize()
        b = Board()
        b.pieces = np.copy(board)
        legalMoves = b.get_all_legal_moves(player)
        if len(legalMoves) == 0:
            valids[-1] = 1
            return np.array(valids)
        for x, y in legalMoves:
            valids[self.n * x + y] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        b = Board()
        b.pieces = np.copy(board)
        if b.is_win(player):
            return 1
        if b.is_win(-player):
            return -1
        if b.are_any_moves_possible() > 0:  # game didnt end
            return 0
        return 0.0001   # draw

    def getCanonicalForm(self, board, player):
        return board * player

    def getSymmetries(self, board, pi):
        assert (len(pi) == self.n ** 2 + 1)  # 1 for pass
        pi_board = np.reshape(pi[:-1], (self.n, self.n))
        l = []

        for i in range(1, 5):
            for j in [True, False]:
                newB = np.rot90(board, i)
                newPi = np.rot90(pi_board, i)
                if j:
                    newB = np.fliplr(newB)
                    newPi = np.fliplr(newPi)
                l += [(newB, list(newPi.ravel()) + [pi[-1]])]
        return l

    def stringRepresentation(self, board):
        return np.array_str(board)

    @staticmethod
    def display(board):
        n = board.shape[0]
        print(" |", end='')
        for i in range(n):
            print('-' + str(i), end='')
        print("-|")
        for i in range(n):
            print(str(i) + '| ', end='')
            for j in range(n):
                piece = board[i][j]
                piece = 'X' * piece + 'O' * -piece + ' ' * (piece == 0)
                print(piece + ' ', end='')
            print('|')

