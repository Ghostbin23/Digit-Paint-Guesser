from utils import * # import everything from the utils folder

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) # defining a window to draw on
pygame.display.set_caption("Drawing Program") # setting the header of the window

def init_grid(rows,cols,colour):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols): # not using variable here
            grid[i].append(colour)
    return grid

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * 
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) # draw onto window, with pixel colour, and x and y and width and height
    
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, RED, (0, i * PIXEL_SIZE), 
                             (WIDTH, i * PIXEL_SIZE))
        
        for j in range(COLS + 1):
            pygame.draw.line(win, RED, (j * PIXEL_SIZE, 0), 
                             (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw(win, grid,buttons):
    win.fill(BG_COLOUR) # fill window with background
    draw_grid(win,grid)
    for button in buttons:
        button.draw(win)

    pygame.display.update() # updating display 

def get_row_col_from_pos(pos):
    x, y= pos # decompose tuple
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS: # if the row being clicked is not in the drawable area (in toolbar)
        raise IndexError

    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS,COLS,BG_COLOUR)
drawing_colour = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, BLUE),
    Button(130, button_y, 50, 50, WHITE, "Clear", BLACK),
]

## EVENT LOOP: continually runs until program ends, listening for events
while run: 
    clock.tick(FPS) # sticking to the FPS of the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]: # checking for LEFT click, which is [0]
            pos = pygame.mouse.get_pos() # gets x/y of where mouse is
            try:
                row,col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_colour
                grid[row+1][col] = drawing_colour
                grid[row-1][col] = drawing_colour
                grid[row][col+1] = drawing_colour
                grid[row][col-1] = drawing_colour
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_colour = button.colour
                    if button.text == "Clear":
                        grid = init_grid(ROWS,COLS,BG_COLOUR)
                        drawing_colour = BLACK

    draw(WIN,grid,buttons)

pygame.quit()
