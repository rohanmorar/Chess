'''
this is our driver file - responisbilities: user input handling and displays current GameState object
'''

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 400
DIMENSION = 8 # standard 8x8 dimension chess board
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15 # will come to use in animation later
IMAGES = {}

# create a function to load all our piece images one time (as to avoid lag from loading them in each frame)
# helps when implementing option to change piece skins later
def loadImages():
    pieces = ["bB", "bN", "bR", "bK", "bQ", "wB", "wN", "wR", "wK", "wQ", "wP", "bP"]
    for piece in pieces:
         # Access Images with 'IMAGES['bB']'
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

'''
main driver for our code. Handle user input and updating graphics
'''

def main():
    p.init()
    p.display.set_caption('Chess')
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() # do once before while loop for setup
    running = True
    sqSelected = () # no square is selected initially, tuple: (row, col), keeps track of user's last click
    playerClicks = [] # keeps track of the player's clicks as tuples [(6,4), (4,4)]
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                raise SystemExit
                running = False
            #click piece and click end-point to move piece there
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x,y) location of mouse
                # get the row/col cooresponding to mouse click 
                row = location[1] // SQ_SIZE
                col = location[0] // SQ_SIZE
                
                # if our selection has already previously been selected, we want to DESELECT the piece; reset sqSelected and playerClicks
                if sqSelected == (row, col):
                    print("Selection is reset")
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both first and second clicks shown in (rowIndex, colIndex) rowIndex from  top to bottom (0-7). colIndex from left to right (0-7)
                if len(playerClicks) == 2:
                    # check if 2nd move is valid (playerClicks[1])
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print("move to " + str(move.getChessNotation()))
                    gs.makeMove(move)

                    # reset sqSelected and playerClicks after the move
                    sqSelected = ()
                    playerClicks = []

                    # piece moves to location
                    
        drawGameState(screen, gs)
        # for every second at most MAX_FPS frames should pass.
        clock.tick(MAX_FPS)
        # update the full display Surface to the screen
        p.display.flip()

'''
responsible for all the graphics within a current game state
'''

def drawGameState(screen, gs):
    # draw squares on the board
    drawBoard(screen) 
    # add piece highlighting or move suggestions later
    # draw pieces on top of the squares
    drawPieces(screen, gs.board)

'''
draw the squares on the board
'''

def drawBoard(screen):
    #Light square
    LIGHT = (252, 248, 232)
    DARK = (236, 179, 144)
    LIGHT2 = (247, 237, 219)
    DARK2 = (204, 214, 166)

    colors = [p.Color(LIGHT), p.Color(DARK)]

    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
draw the pieces on the board using the current gs.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            # if piece is not empty as represented by '--'
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
