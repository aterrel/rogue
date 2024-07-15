import random
import pygame.time


class Board:
    BOARD_HEIGHT = 600
    BOARD_WIDTH = 800
    TILE_HEIGHT = 50
    TILE_WIDTH = 50
    MIN_X_TILE = 1
    MAX_Y_TILE = BOARD_HEIGHT // TILE_HEIGHT - 2
    MAX_X_TILE = BOARD_WIDTH // TILE_WIDTH - 2
    MIN_Y_TILE = 1
    SCORE = 0
    BORDERS = (0, 100, 100)

    def __init__(self):
        self.obstacles = [(random.randint(2, self.MAX_X_TILE - 1), random.randint(2, self.MAX_Y_TILE - 1))
                          for i in range(10)]
        self.coins = self.generate_coins()
    
    def generate_coins(self):
        num_coins = 10
        coins = []
        for _ in range(num_coins):
            while True:
                coin = (random.randint(1, self.MAX_X_TILE - 1), random.randint(1, self.MAX_Y_TILE - 1))
                if coin not in self.obstacles:
                    break
            coins.append(coin)
        return coins

    def draw(self):
        self.draw_board()
        self.draw_obstacles()
        self.draw_coins()

    def draw_board(self):
        for i in range(self.TILE_WIDTH, self.BOARD_HEIGHT, self.TILE_WIDTH):
            screen.draw.line((0, i), (self.BOARD_WIDTH, i), self.BORDERS)
        for i in range(self.TILE_HEIGHT, self.BOARD_WIDTH, self.TILE_HEIGHT):
            screen.draw.line((i, 0), (i, self.BOARD_HEIGHT), self.BORDERS)

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            m = Rect((obstacle[0] * self.TILE_WIDTH, 
                      obstacle[1] * self.TILE_HEIGHT), 
                     (self.TILE_WIDTH, self.TILE_HEIGHT))
            screen.draw.filled_rect(m, (0, 200, 0))

    def draw_coins(self):
        for coin in self.coins:
            n = Rect((coin[0] * self.TILE_WIDTH, 
                      coin[1] * self.TILE_HEIGHT), 
                     (self.TILE_WIDTH, self.TILE_HEIGHT))
            screen.draw.filled_rect(n, (255, 255, 0))

    def has_obstacle(self, x, y):
        """Given tile x and y, checks to see if there is an obstacle"""
        for obstacle in self.obstacles:
            if obstacle[0] == x and obstacle[1] == y:
                return True
        return False
    
    def hit_coin(self, x, y):
        c_idx = -1
        for i, coin in enumerate(self.coins):
            if coin[0] == x and coin[1] == y:
                self.score += 1
                c_idx = i
        if c_idx != -1:
            self.coins.pop(c_idx)
        return
        

class Character:
    COLOR = ( 200, 0, 0)

    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, board,):
        r = Rect((self.x * board.TILE_WIDTH, self.y * board.TILE_HEIGHT), 
                 (board.TILE_WIDTH, board.TILE_HEIGHT))
        screen.draw.filled_rect(r, Character.COLOR)


class World:
    def __init__(self):
        self.c = Character()
        self.b = Board()

    def draw(self):
        self.b.draw()
        self.c.draw(self.b)

    def move_character(self, x, y):
        if self.b.has_obstacle(self.c.x + x, self.c.y + y):
            return None

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
        world.move_character(0, -1)
    if keyboard.s:
        world.move_character(0, 1)
    if keyboard.a:
        world.move_character(-1, 0)
    if keyboard.d:
        world.move_character(1, 0)
    if keyboard.up:
        world.move_character(0, -1)
    if keyboard.down:
        world.move_character(0, 1)
    if keyboard.left:
        world.move_character(-1, 0)
    if keyboard.right:
        world.move_character(1, 0)

def update():
    move()
    draw()
    pygame.time.delay(100)
