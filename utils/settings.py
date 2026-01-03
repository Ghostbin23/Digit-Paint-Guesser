import pygame
pygame.init()
pygame.font.init() # the first two things you do, always initialise fonts and the pygame module

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

FPS = 120

WIDTH, HEIGHT = 600,700

ROWS = COLS = 50 # how many pixels to paint, the size (square pixels for paint)

TOOLBAR_HEIGHT = HEIGHT - WIDTH # difference in height and width is our toolbar

PIXEL_SIZE = WIDTH // ROWS # square, how large to draw pixels

BG_COLOUR = WHITE

DRAW_GRID_LINES = False # whether grid lines of pixels are drawn

def get_font(size): # generate and return a font of passed size
    return pygame.font.SysFont("comicsans", size)