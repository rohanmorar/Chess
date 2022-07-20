'''
this is our driver file - responisbilities: user input handling and displays current GameState object
'''

import pygame as p
import ChessEngine

p.init()

WIDTH = HEIGHT = 400
DIMENSION = 8 # standard 8x8 dimension chess board

SQ_SIZE = WIDTH // DIMENSION

MAX_FPS = 15 # will come to use in animation later

IMAGES = {}

PATH = "/Users/rohanmorar/Desktop/Chess/Chess/images"

# create a function to load all our piece images one time (as to avoid lag from loading them in each frame)
# helps when implementing option to change piece skins later
def loadImages():
    pieces = ["bB", "bN", "bR", "bK", "bQ", "wB", "wN", "wR", "wK", "wQ", "wP", "bP"]
    for piece in pieces:
         # Access Images with 'IMAGES['bB']'
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

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
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                raise SystemExit
                running = False
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
            color = colors[(row + col) % 2]
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
