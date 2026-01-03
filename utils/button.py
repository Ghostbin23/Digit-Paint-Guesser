from .settings import *

class Button:
    def __init__(self, x, y, width, height, colour, text = None, text_colour = BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text
        self.text_colour = text_colour

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 2) # the two means that it's just an outline
        if self.text:
            button_font = get_font(16)
            text_surface = button_font.render(self.text, 1, self.text_colour) # using font object to render the text
            win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, # we subtract text surface width so it happens in middle
                                    self.y + self.height / 2 - text_surface.get_height() / 2)) # putting it on the screen

    def clicked(self, pos):
        x,y = pos
        if not (x >= self.x and x<= self.x + self.width): # xheck if the position is within bounds of button
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False
        
        return True