import numpy as np
import os
from .TicTacToeNNet import TicTacToeNNet as tttnn
from utils import *

args = dotdict({
    'lr': 0.001,
    'dropout': 0.3,
    'epochs': 10,
    'batch_size': 64,
    'cuda': True,  # only half of the team has cuda
    'num_channels': 512,
})


class NNet():
    def __init__(self, game):
        self.nnet = tttnn(game, args)
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()

    def train(self, examples):
        input_boards, target_pis, target_vs = list(zip(*examples))
        input_boards = np.asarray(input_boards)
        target_pis = np.asarray(target_pis)
        target_vs = np.asarray(target_vs)
        self.nnet.model.fit(x=input_boards, y=[target_pis, target_vs], batch_size=args.batch_size, epochs=args.epochs)

    def predict(self, board):
        board = board[np.newaxis, :, :]
        pi, v = self.nnet.model.predict(board)
        return pi[0], v[0]

    def save_checkpoint(self, folder, filename):
        filepath = os.path.join(folder, filename)
        if not os.path.exists(folder):
            print("Directory does not exist, making directory {path}".format(path=folder))
        else:
            print("Directory already exists!")
        self.nnet.model.save_weights(filepath)

    def load_checkpoint(self, folder, filename):
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError("No model in path {path}".format(path=filepath))
        self.nnet.model.load_weights(filepath)
