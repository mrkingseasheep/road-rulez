from constants import *


class Map:
    def __init__(self, screen):
        self.screen = screen

    def update_map(self, x, y):
        left = x - WIDTH // 2
        top = y - HEIGHT // 2

        # if left <= 0:
        #     left = 0
        #     car_should_move = True
        # elif left + WIDTH >= MAP_X:
        #     left = MAP_X - WIDTH
        #     car_should_move = True
        # if top <= 0:
        #     top = 0
        #     car_should_move = True
        # elif top + HEIGHT >= MAP_Y:
        #     top = MAP_Y - HEIGHT
        #     car_should_move = True

        self.screen.blit(MAP, (0, 0), (left, top, WIDTH, HEIGHT))
