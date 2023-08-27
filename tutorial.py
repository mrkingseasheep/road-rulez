from constants import *
from level import *

class Tutorial:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.gameStateManager = game_state_manager
        self.pause_rect = pygame.Rect(WIDTH // 10 * 9.5 - 25, HEIGHT // 10 - 25, 50, 50)
        
    def run(self):
        tutorial_rect = TUTORIAL.get_rect()
        tutorial_rect.center = (WIDTH // 2, HEIGHT // 2)
        self.screen.blit(TUTORIAL, tutorial_rect)
        Level.draw_pause(self)