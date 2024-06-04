from pygame import display, time, event, Rect, draw, QUIT, quit

class Game:
    def __init__(self, width, height, title, bgcolor, fps):
        # initialize parameter variables
        self.width = width
        self.height = height
        self.title = title
        self.bgcolor = bgcolor
        self.clock_tick = fps

        #initialize pygame stuff
        self.screen = display.set_mode((self.width, self.height))
        display.set_caption(self.title)
        self.clock = time.Clock()

        # initialize game stuff like players
        self.player = Player(0,0,30,30,"red")
    
    def draw_everything(self):
        # draw background
        self.screen.fill(self.bgcolor)

        # draw player
        draw.rect(self.screen, self.player.color, self.player.get_rect)

        # update screen
        display.update()

    def run(self):
        running = True
        while running:
            for e in event.get():
                if e.type == QUIT:
                    running = False 
                    quit()
                    return
            
            self.draw_everything()

            self.clock.tick(self.clock_tick)
                    
class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def get_pos(self):
        return (self.x, self.y)
    
    def get_rect(self):
        return rect(self.x, self.y, self.width, self.height)
    
    def move(self, d_x, d_y):
        self.x += d_x
        self.y += d_y

game = Game(500,500, "sigma", "white", 60)
game.run()