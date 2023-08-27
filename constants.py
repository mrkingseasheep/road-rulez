import pygame
import os

pygame.init()
infoObject = pygame.display.Info()

WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
TITLE = "Driving Test Game CHANGE"

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Graphics", "Background.png")).convert_alpha(), (WIDTH, HEIGHT))
BACKGROUND_RECT = BACKGROUND.get_rect()
TUTORIAL = pygame.transform.scale(pygame.image.load(os.path.join("Graphics", "Tutorial.png")).convert_alpha(), (WIDTH, HEIGHT))
TUTORIAL_RECT = TUTORIAL.get_rect()
FONT = pygame.font.SysFont(os.path.join("Graphics", "PoetsenOne-Regular.ttf"), 40)
CAR_ORIGINAL = pygame.image.load(os.path.join("Graphics", "Car.png"))
MAP = pygame.image.load(os.path.join("Graphics", "Map.png"))
MAP_SCALED = pygame.transform.scale(MAP, (MAP.get_width() // 10, MAP.get_height() // 10))

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)
GRAY = (217, 217, 217)
WHITE = (255, 255, 255)