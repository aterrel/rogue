alien = Actor('alien')
alien.pos = 100, 56
alien.topright = 0, 10

class Board:
    BOARD_HEIGHT = 600
    BOARD_WIDTH = 800
    TILE_HEIGHT = 50
    TILE_WIDTH = 50
    BORDERS = (0, 200, 0)

    def draw(self):
        self.draw_board()

    def draw_board(self):
        for i in range(self.TILE_WIDTH, self.BOARD_HEIGHT, self.TILE_WIDTH):
            screen.draw.line((0, i), (self.BOARD_WIDTH, i), self.BORDERS)
        for i in range(self.TILE_HEIGHT, self.BOARD_WIDTH, self.TILE_HEIGHT):
            screen.draw.line((i, 0), (i, self.BOARD_HEIGHT), self.BORDERS)

def draw():
    screen.clear()
    b = Board()
    # alien.draw()
    b.draw()

# def update():
#     alien.left += 2
#     if alien.left > WIDTH:
#         alien.right = 0

# def on_mouse_down(pos):
#     if alien.collidepoint(pos):
#         set_alien_hurt()

# def set_alien_hurt():
#     alien.image = 'alien_hurt'
#     sounds.eep.play()    
#     clock.schedule_unique(set_alien_normal, 1.0)

# def set_alien_normal():
#     alien.image = 'alien'
