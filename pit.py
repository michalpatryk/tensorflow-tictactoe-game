import Arena
from MCTS import MCTS
from TicTacToe.AITTTGame import Game
from TicTacToe.TTTPlayer import *
from TicTacToe.pytorch.NNet import NNet
from utils import *

game = Game()

nn = NNet(game)
nn.load_checkpoint('./temp/', 'best.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts1 = MCTS(game, nn, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

arena = Arena.Arena(n1p, HumanTicTacToePlayer(game).play, game, display=Game.display)
arena.playGames(2, verbose=True)
