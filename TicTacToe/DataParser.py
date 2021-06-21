import csv
import os
import importlib.resources as pkg_resources
from . import dataset


def read_tic_tac_toe_data():
    data = pkg_resources.open_text(dataset, 'tic-tac-toe.data')
    return csv.reader(data, delimiter=',')


def is_game_end(game_state):
    reader = read_tic_tac_toe_data()
    for row in reader:
        if row[:-1] == game_state:
            return True, row[-1]
    return False

def is_game_win(pieces, color):
    reader = read_tic_tac_toe_data()
    flat_transformed_pieces = []
    for subpieces in pieces:
        for piece in subpieces:
            if piece == 0:
                flat_transformed_pieces.append('b')
            if piece == 1:
                flat_transformed_pieces.append('o')
    #for row in reader:
        # if row == pieces