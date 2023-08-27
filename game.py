import sys
import os
import pygame
from pygame import locals
from pause import Pause
from gameStateManager import GameStateManager
from tutorial import Tutorial
from level import Level
from menu import Menu
from constants import *


class Game:
    def __init__(self):
        pygame.init()
        self.FPS = 60

        pygame.display.set_caption("TITLE | Ignition Hacks")
        pygame.display.set_icon(pygame.image.load(os.path.join("Graphics", "Logo.png")))
        self.SCREEN = SCREEN
        self.CLOCK = pygame.time.Clock()

        self.gameStateManager = GameStateManager("menu")
        self.menu = Menu(self.SCREEN, self.gameStateManager)
        self.level = Level(self.SCREEN, self.gameStateManager)
        self.pause = Pause(self.SCREEN, self.gameStateManager)
        self.tutorial = Tutorial(self.SCREEN, self.gameStateManager)
        self.states = {"menu": self.menu, "level": self.level, "pause": self.pause, "tutorial": self.tutorial}

        self.objs = []
        self.obj_rects = []

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.gameStateManager.get_state() == "menu":
                            if (WIDTH // 10 < event.pos[0] < WIDTH // 10 + BACKGROUND_RECT.width // 10 * 3) and (HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
                                self.gameStateManager.set_state("level")
                            elif (WIDTH // 10 * 6 < event.pos[0] < WIDTH // 10 * 6 + BACKGROUND_RECT.width // 10 * 3) and (HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
                                pygame.quit()
                                sys.exit()

                        elif self.gameStateManager.get_state() == "level":
                            if ((WIDTH // 10 * 9.5 - 25 < event.pos[0] < WIDTH // 10 * 9.5 + 25) and (HEIGHT // 10 - 25 < event.pos[1] < HEIGHT // 10 + 25)):
                                self.gameStateManager.set_state("pause")

                            if self.level.accelerator_rect.collidepoint(event.pos):
                                self.level.accelerate()
                            elif self.level.brake_rect.collidepoint(event.pos):
                                self.level.brake()

                        elif self.gameStateManager.get_state() == "pause":
                            tutorial_button = pygame.Rect(WIDTH // 2, HEIGHT // 5, 300, 100)
                            tutorial_button.center = (WIDTH // 2, HEIGHT // 5)
                            menu_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 2, 300, 100)
                            menu_button.center = (WIDTH // 2, HEIGHT // 5 * 2)
                            resume_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 3, 300, 100)
                            resume_button.center = (WIDTH // 2, HEIGHT // 5 * 3)
                            exit_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 4, 300, 100)
                            exit_button.center = (WIDTH // 2, HEIGHT // 5 * 4)

                            mouse_pos = pygame.mouse.get_pos()
                            if tutorial_button.collidepoint(mouse_pos):
                                self.gameStateManager.set_state("tutorial")
                            elif menu_button.collidepoint(mouse_pos):
                                self.gameStateManager.set_state("menu")
                            elif resume_button.collidepoint(mouse_pos):
                                self.gameStateManager.set_state("level")
                            elif exit_button.collidepoint(mouse_pos):
                                pygame.quit()
                                sys.exit()

                elif event.type == locals.FINGERDOWN:
                    if self.gameStateManager.get_state() == "level":
                        if hasattr(event, 'touches'):
                            for touch in event.touches:
                                touch_x, touch_y = touch.x, touch.y
                                if self.level.accelerator_rect.collidepoint(touch_x, touch_y):
                                    self.level.accelerate()
                                elif self.level.brake_rect.collidepoint(touch_x, touch_y):
                                    self.level.brake()

            SCREEN.fill("black")
            self.states[self.gameStateManager.get_state()].run()
            self.CLOCK.tick(self.FPS)
            pygame.display.update()