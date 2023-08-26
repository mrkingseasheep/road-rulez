import pygame

pygame.init()
infoObject = pygame.display.Info()

WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
TITLE = "Driving Test Game CHANGE"

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

BACKGROUND = pygame.transform.scale(pygame.image.load("./Graphics/Background.png").convert_alpha(), (WIDTH, HEIGHT))
BACKGROUND_RECT = BACKGROUND.get_rect()
FONT = pygame.font.SysFont("./Font/PoetsenOne-Regular.ttf", 30)
CAR_ORIGINAL = pygame.image.load('./Graphics/Car.png')

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)
