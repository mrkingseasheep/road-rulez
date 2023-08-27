from constants import *

MAP_SIZE = min(WIDTH, HEIGHT) // 3
MARGIN_SIZE = min(WIDTH, HEIGHT) // 80
MINI_X = 394
MINI_Y = 677


class Minimap:
    def __init__(self, screen):
        self.screen = screen

    def update_minimap(self, x, y):
        left = x // 10 - MAP_SIZE // 2
        top = y // 10 - MAP_SIZE // 2

        if left < 0:
            left = 0
        elif left + MAP_SIZE > MINI_X:
            left = MINI_X - MAP_SIZE
        if top < 0:
            top = 0
        elif top + MAP_SIZE > MINI_Y:
            top = MINI_Y - MAP_SIZE

        self.screen.blit(MAP_SCALED, (MARGIN_SIZE, MARGIN_SIZE), (left, top, MAP_SIZE, MAP_SIZE))
