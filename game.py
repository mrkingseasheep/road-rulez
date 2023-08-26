import sys

import pygame

from gameStateManager import GameStateManager
from level import Level
from menu import Menu
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.FPS = 60

        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.CLOCK = pygame.time.Clock()

        self.gameStateManager = GameStateManager("menu")
        self.menu = Menu(self.SCREEN, self.gameStateManager)
        self.level = Level(self.SCREEN, self.gameStateManager)

        self.states = {"menu": self.menu, "level": self.level}

        self.objs = []
        self.obj_rects = []

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (WIDTH // 10 < event.pos[0] < WIDTH // 10 + BACKGROUND_RECT.width // 10 * 3) and (
                            HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
                        self.gameStateManager.set_state("level")
                    elif (WIDTH // 10 * 6 < event.pos[0] < WIDTH // 10 * 6 + BACKGROUND_RECT.width // 10 * 3) and (
                            HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
                        pygame.quit()
                        sys.exit()
            SCREEN.fill("black")
            self.states[self.gameStateManager.get_state()].run()
            self.CLOCK.tick(self.FPS)
            pygame.display.update()
