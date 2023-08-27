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

MAP_SIZE = min(WIDTH, HEIGHT) // 3
HALF_MAP_SIZE = MAP_SIZE // 2
MARGIN_SIZE = min(WIDTH, HEIGHT) // 80
MINI_X, MINI_Y = 394, 677
MAP_X, MAP_Y = 3944, 6775
HALF_X, HALF_Y = MAP_X // 2, MAP_Y // 2

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)
GRAY = (217, 217, 217)
WHITE = (255, 255, 255)

# ur dumb
