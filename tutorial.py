from constants import *


class Tutorial:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.gameStateManager = game_state_manager
        
    def run(self):
        background_rect = BACKGROUND.get_rect()
        background_rect.center = (WIDTH // 2, HEIGHT // 2)
        self.screen.blit(BACKGROUND, background_rect)