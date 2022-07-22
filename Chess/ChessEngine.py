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

        def updateMoveLog():
            self.move_log.append(self.board)

class Move():
    def __init__(self, startSq, endSq, board):

        rowsToRanks = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
        rowsToRanks = {v:k for k, v in rowsToRanks.items()}
        colsToFiles = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
        colsToFiles = {v:k for k, v in colsToFiles.items()}



        #decoupling tuples for our start and end squares
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol)
        # if self.pieceMoved == "wP" or self.pieceMoved == "bP":
        #     self.move_log.append()

    def getRankFile(self, row, col):
        return self.rowsToRanks[row] + self.colsToFiles[col]