import logging
import coloredlogs

from TicTacToe.AITTTGame import Game as TicTacToeGame
# from TicTacToe.keras.NNet import NNet as nn
from TicTacToe.pytorch.NNet import NNet as nn
from utils import *
from Coach import Coach

log = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

args = dotdict({
    'numIters': 10,
    'numEps': 40,               # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 15,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 25,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})

if __name__ == '__main__':
    game = TicTacToeGame()

    log.info('Loading %s...', nn.__name__)
    nnet = nn(game)

    log.info('Loading the Coach...')
    c = Coach(game, nnet, args)

    log.info('Starting the learning process 🎉')
    c.learn()
