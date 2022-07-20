'''
Class responsible for storing all the info about the current game. It will also be responsible for determining the valid moves and current state.
And will keep a move log. 
'''

import numpy as np

class GameState():
    def __init__(self):
        # 8x8 chess board represented by a 2D list. 
        # Each element in the list is represented by a 2 char string
        # -- represents empty space, b/w represent black/white, and R/N/B/Q/K represent Rook/Knight/Bishop/Queen/King
        # created using np array for ease of use down the line
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

        self.whiteToMove = True;

        self.move_log = []

        self.wKCastleK = False;

        self.wKCastleQ = False;
        
        self.bKCastleK = False;

        self.bKCastleQ = False;