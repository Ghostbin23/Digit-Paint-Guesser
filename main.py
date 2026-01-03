from utils import * # import everything from the utils folder
import cv2
import numpy as np
import tensorflow as tf

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

def submit_drawing():
    pygame.image.save(WIN, "digit.png")
    img = cv2.imread(f"digit.png")[:,:,0] # no shape, no colour, just pixels
    img = cv2.bitwise_not(img) # invert, black on white now but needs white on black
    img = img[0:HEIGHT-TOOLBAR_HEIGHT,0:WIDTH]
    img = cv2.resize(img, (28,28), interpolation = cv2.INTER_AREA)
    cv2.imwrite("changed.png",img)
    img = img.reshape(1,28,28) # need to add batch dimension
    print(img.shape)
    pred = np.argmax(model.predict(img))
    print(pred)

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS,COLS,BG_COLOUR)
drawing_colour = BLACK
model  = tf.keras.models.load_model('digit_model.keras')
predict_text = f'That number is {pred}'

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, BLUE),
    Button(130, button_y, 50, 50, WHITE, "Clear", BLACK),
    Button(190, button_y, 50, 50, WHITE, "Submit", BLACK),
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
                    if button.text == "Submit":
                        submit_drawing()

    draw(WIN,grid,buttons)

pygame.quit()
