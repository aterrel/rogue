import pygame.time

class Board:
    BOARD_HEIGHT = 600
    BOARD_WIDTH = 800
    TILE_HEIGHT = 50
    TILE_WIDTH = 50
    MIN_X_TILE = 1
    MAX_X_TILE = BOARD_HEIGHT / TILE_HEIGHT - 2
    MAX_Y_TILE = BOARD_WIDTH / TILE_WIDTH - 2
    MIN_Y_TILE = 1
    BORDERS = (0, 100, 100)

    def draw(self):
        self.draw_board()

    def draw_board(self):
        for i in range(self.TILE_WIDTH, self.BOARD_HEIGHT, self.TILE_WIDTH):
            screen.draw.line((0, i), (self.BOARD_WIDTH, i), self.BORDERS)
        for i in range(self.TILE_HEIGHT, self.BOARD_WIDTH, self.TILE_HEIGHT):
            screen.draw.line((i, 0), (i, self.BOARD_HEIGHT), self.BORDERS)

class Character:
    COLOR_OF_CHARACTER = ( 200, 0, 0)

    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, board,):
        r = Rect((self.y * board.TILE_WIDTH, self.x * board.TILE_HEIGHT), (board.TILE_WIDTH, board.TILE_HEIGHT))
        screen.draw.filled_rect(r, Character.COLOR_OF_CHARACTER)


class World:
    def __init__(self):
        self.c = Character()
        self.b = Board()

    def draw(self):
        self.b.draw()
        self.c.draw(self.b)

    def move_character(self, x, y):
        self.c.x += x
        if self.c.x < self.b.MIN_X_TILE:
            self.c.x = self.b.MIN_X_TILE
        if self.c.x > self.b.MAX_X_TILE:
            self.c.x = self.b.MAX_X_TILE
        self.c.y += y
        if self.c.y < self.b.MIN_Y_TILE:
            self.c.y = self.b.MIN_Y_TILE
        if self.c.y > self.b.MAX_Y_TILE:
            self.c.y = self.b.MAX_Y_TILE

world = World()

def draw():
    global world
    screen.clear()
    world.draw()
    

def move():
    global world
    if keyboard.w:
        world.move_character(-1, 0)
    if keyboard.s:
        world.move_character(1, 0)
    if keyboard.a:
        world.move_character(0, -1)
    if keyboard.d:
        world.move_character(0, 1)

def update():
    move()
    draw()
    pygame.time.delay(100)
