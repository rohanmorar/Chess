'''
Class responsible for storing all the info about the current game. It will also be responsible for determining the valid moves and current state.
And will keep a move log. 
'''

import numpy as np


class GameState():
    def __init__(self):
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB","bN","bR" ],
            ["bP", "bN", "bP", "bP", "bP", "bP","bP", "bP"],
            ["--","--", "--", "--", "--", "--","--","--"],
            ["--","--", "--", "--", "--", "--","--","--"],
            ["--","--", "--", "--", "--", "--","--","--"],
            ["--","--", "--", "--", "--", "--","--","--"],
            ["wP", "wP", "wP", "wP", "wP", "wP","wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB","wN","wR" ]

        ])