import pygame
import os

pygame.init()
infoObject = pygame.display.Info()

WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
# WIDTH, HEIGHT = 1080, 720
TITLE = "Road Rulez - G1/2 Test Prep"
FPS = 30

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Graphics", "Background.png")).convert_alpha(), (WIDTH, HEIGHT))
BACKGROUND_RECT = BACKGROUND.get_rect()
TUTORIAL = pygame.transform.scale(pygame.image.load(os.path.join("Graphics", "Tutorial.png")).convert_alpha(), (WIDTH, HEIGHT))
TUTORIAL_RECT = TUTORIAL.get_rect()
FONT = pygame.font.SysFont(os.path.join("Graphics", "PoetsenOne-Regular.ttf"), 40)
QUESTION_FONT = pygame.font.SysFont(os.path.join("Graphics", "PoetsenOne-Regular.ttf"), 50)
ANSWER_FONT = pygame.font.SysFont(os.path.join("Graphics", "PoetsenOne-Regular.ttf"), 40)
CAR_ORIGINAL = pygame.image.load(os.path.join("Graphics", "Car.png"))
MAP = pygame.image.load(os.path.join("Graphics", "Map.png"))
MAP_SCALED = pygame.transform.scale(MAP, (MAP.get_width() // 10, MAP.get_height() // 10))

LEFT_MARGIN = WIDTH // 20
TOP_MARGIN = HEIGHT // 15
BOX_WIDTH = WIDTH - 2 * LEFT_MARGIN
QUESTION_THICK = WIDTH // 20
ANSWER_THICK = WIDTH // 30
ANSWER_MARGIN = WIDTH // 30
STAN_ANSWER_THIC = ANSWER_THICK + ANSWER_MARGIN

QUESTION = pygame.Rect(LEFT_MARGIN, TOP_MARGIN, BOX_WIDTH, QUESTION_THICK)
ANS1 = pygame.Rect(LEFT_MARGIN, TOP_MARGIN + QUESTION_THICK + ANSWER_MARGIN, BOX_WIDTH, QUESTION_THICK)
ANS2 = pygame.Rect(LEFT_MARGIN, TOP_MARGIN + QUESTION_THICK + ANSWER_MARGIN + STAN_ANSWER_THIC, BOX_WIDTH,
                   QUESTION_THICK)
ANS3 = pygame.Rect(LEFT_MARGIN, TOP_MARGIN + QUESTION_THICK + ANSWER_MARGIN + 2 * STAN_ANSWER_THIC, BOX_WIDTH,
                   QUESTION_THICK)
ANS4 = pygame.Rect(LEFT_MARGIN, TOP_MARGIN + QUESTION_THICK + ANSWER_MARGIN + 3 * STAN_ANSWER_THIC, BOX_WIDTH,
                   QUESTION_THICK)
ANS_BOX = [ANS1, ANS2, ANS3, ANS4]

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
LIGHT_GRAY = (240, 240, 240)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 100, 0)
RED = (255, 0, 0)
LIGHT_RED = (100, 0, 0)
LIGHT_LIGHT_GREEN = (0, 25, 0)
LIGHT_LIGHT_RED = (25, 0, 0)
DARK_GRAY = (20, 20, 20)
