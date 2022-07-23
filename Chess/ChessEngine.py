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
            ["bR", "bN", "bB", "bQ", "bK", "bB","bN","bR" ], #row: 0: "8"
            ["bP", "bN", "bP", "bP", "bP", "bP","bP", "bP"], #row: 1: "7"
            ["--","--", "--", "--", "--", "--","--","--"],   #row: 2: "6"
            ["--","--", "--", "--", "--", "--","--","--"],   #row: 3: "5"
            ["--","--", "--", "--", "--", "--","--","--"],   #row: 4: "4"
            ["--","--", "--", "--", "--", "--","--","--"],   #row: 5: "3"
            ["wP", "wP", "wP", "wP", "wP", "wP","wP", "wP"], #row: 6: "2"
            ["wR", "wN", "wB", "wQ", "wK", "wB","wN","wR" ]  #row: 7: "1"
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

        rowsToRanks = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5:"3", 6:"2", 7:"1"}
        colsToFiles = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

        #decoupling the tuple coordinates (i.e. START: (6,4) -> END: (4, 4))
        self.startRow = startSq[0] # 6
        self.startCol = startSq[1] # 4
        
        self.endRow = endSq[0] # 4
        self.endCol = endSq[1] # 4

        self.pieceMoved = board[self.startRow][self.startCol] # wP
        self.pieceCaptured = board[self.endRow][self.endCol] # --

    def getChessNotation(self):
        return self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, row, col):
        return self.rowsToRanks[row] + self.colsToFiles[col]
