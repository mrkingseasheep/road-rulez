import sys
import os
import math
import pygame
from pygame import locals
from pause import Pause
from gameStateManager import GameStateManager
from tutorial import Tutorial
from quiz import Quiz
from level import Level
from menu import Menu
from constants import *

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption(f"{TITLE} | Ignition Hacks")
        pygame.display.set_icon(pygame.image.load(os.path.join("Graphics", "Logo.png")))
        self.SCREEN = SCREEN
        self.CLOCK = pygame.time.Clock()

        self.wheel_clicked = False
        self.acceleration_intensity = 0
        self.brake_intensity = 0
        
        self.gameStateManager = GameStateManager("menu")
        self.menu = Menu(self.SCREEN, self.gameStateManager)
        self.level = Level(self.SCREEN, self.gameStateManager)
        self.pause = Pause(self.SCREEN, self.gameStateManager)
        self.tutorial = Tutorial(self.SCREEN, self.gameStateManager)
        self.quiz = Quiz(self.SCREEN, self.gameStateManager)
        self.states = {"menu": self.menu, "level": self.level, "pause": self.pause, "tutorial": self.tutorial, "quiz": self.quiz}
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
                            elif self.level.accelerator_rect.collidepoint(event.pos):
                                self.level.accelerate()
                            elif self.level.brake_rect.collidepoint(event.pos):
                                self.level.brake()
                            elif self.level.gear_rect.collidepoint(event.pos):
                                self.level.gear()
                            elif self.level.wheel_rect.collidepoint(event.pos):
                                self.wheel_clicked = True
                                dx, dy = event.pos[0] - self.level.wheel_rect.centerx, event.pos[1] - self.level.wheel_rect.centery
                                angle = math.degrees(math.atan2(dy, dx))
                                self.level.rotate_wheel(angle)

                        elif self.gameStateManager.get_state() == "tutorial":
                            if ((WIDTH // 10 * 9.5 - 25 < event.pos[0] < WIDTH // 10 * 9.5 + 25) and (HEIGHT // 10 - 25 < event.pos[1] < HEIGHT // 10 + 25)):
                                self.gameStateManager.set_state("pause")

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

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.wheel_clicked = False

                elif event.type == locals.FINGERDOWN:
                    if self.gameStateManager.get_state() == "level":
                        if hasattr(event, 'touches'):
                            for touch in event.touches:
                                touch_x, touch_y = touch.x, touch.y
                            if self.level.accelerator_rect.collidepoint(touch_x, touch_y):
                                self.level.accelerate()
                                self.acceleration_intensity += 1
                                self.velocity -= self.acceleration * self.acceleration_intensity / 100
                            elif self.level.brake_rect.collidepoint(touch_x, touch_y):
                                self.level.brake()
                                self.brake_intensity += 1
                                self.velocity += self.acceleration * self.brake_intensity
                            elif self.level.gear_rect.collidepoint(event.pos):
                                self.level.gear()
                            elif self.level.wheel_rect.collidepoint(touch_x, touch_y):
                                self.wheel_clicked = True
                                dx, dy = touch_x - self.level.wheel_rect.centerx, touch_y - self.level.wheel_rect.centery
                                angle = math.degrees(math.atan2(dy, dx))
                                self.level.rotate_wheel(angle)
                                self.level.rot_angle = max(min(angle, 45), -45)

                elif event.type == pygame.FINGERUP:
                    self.wheel_clicked = False
                    self.acceleration_intensity = 0
                    self.brake_intensity = 0

                if self.wheel_clicked:
                    if hasattr(event, 'touches'):
                        for touch in event.touches:
                            touch_x, touch_y = touch.x, touch.y
                            rel_x = touch_x - self.level.wheel_rect.centerx
                            rel_y = touch_y - self.level.wheel_rect.centery
                            angle = math.degrees(math.atan2(rel_y, rel_x))
                            self.level.rotate_wheel(angle)
                            self.level.rot_angle = max(min(angle, 45), -45)

            SCREEN.fill(BLACK)
            self.states[self.gameStateManager.get_state()].run()
            self.CLOCK.tick(FPS)
            pygame.display.update()