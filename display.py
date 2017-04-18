from pygame import display, HWSURFACE, DOUBLEBUF, Color, draw

SCREEN_HEIGHT = 32
SCREEN_WIDTH = 64
'''
Screen depth is the number of bits used to represent color of a pixel
'''
SCREEN_DEPTH = 8 

#The colors of pixels, POM8 has 2 pixel states  - 0 and 1
PIXEL_COLORS = {
    0: Color(0, 0, 0, 255),
    1: Color(250, 250, 250, 255),  
}

class displayScreen(object):

    def __init__(self, scale_factor, height=SCREEN_HEIGHT, width=SCREEN_WIDTH):
        '''
            Initializes display.
            scale_factor is used to adjust the screen size, if 64x32 turns out to be too small
        '''
        self.height = height
        self.width = width
        self.scale_factor = scale_factor
        self.surface = None

    def init_display(self):
        '''
            Attempts to initialize display, the screen by default will have 
            following dimensions:
            SCREEN_HEIGHT = 32
            SCREEN_WIDTH = 64
        '''
        display.init()
        self.surface = display.set_mode(
            ((self.width * self.scale_factor),
             (self.height * self.scale_factor)),
            HWSURFACE | DOUBLEBUF, SCREEN_DEPTH)
        display.set_caption('POM8bit')
        self.clear_screen()
        self.update()

    def draw_pixel(self, x_pos, y_pos, pixel_color):
        '''
            This will attempt to draw a pixel, which will be saved in buffer and drawn 
            after callingt the update() function
        '''
        x_base = x_pos * self.scale_factor
        y_base = y_pos * self.scale_factor
        draw.rect(self.surface, PIXEL_COLORS[pixel_color], (x_base, y_base, self.scale_factor, self.scale_factor))
    
    def get_pixel(self, x_pos, y_pos):
        '''
            Returns whether the pixel is 0 or 1 on specified location
        '''
        x_scale = x_pos * self.scale_factor
        y_scale = y_pos * self.scale_factor
        pixel_color = self.surface.get_at((x_scale, y_scale))
        if pixel_color == PIXEL_COLORS[0]:
            color = 0
        else:
            color = 1

        return color

    def clear_screen(self):
        '''
            Clears screen.
            Writes 0 to all pixel locations
        '''
        self.surface.fill(PIXEL_COLORS[0])
    
    @staticmethod
    def update():
        '''
            Updates display by swapping the screen buffer and back buffer
        '''
        display.flip()

    def get_width():
        return self.width

    def get_height():
        return self.height



