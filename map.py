from constants import *


class Map:
    def __init__(self, screen):
        self.screen = screen

    def update_map(self, x, y):
        left = x - HALF_X
        top = y - HALF_Y

        free_control = False

        if left < 0:
            left = 0
            free_control = True
        elif left + WIDTH > MAP_X:
            left = MAP_X - WIDTH
            free_control = True
        if top < 0:
            top = 0
            free_control = True
        elif top + HEIGHT > MAP_Y:
            top = MAP_Y - HEIGHT
            free_control = True

        self.screen.blit(MAP, (0, 0), (left, top, WIDTH, HEIGHT))

        return free_control


