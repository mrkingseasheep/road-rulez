from constants import *


class Pause:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.gameStateManager = game_state_manager
        
    def run(self):
        background_rect = BACKGROUND.get_rect()
        background_rect.center = (WIDTH // 2, HEIGHT // 2)
        self.screen.blit(BACKGROUND, background_rect)

        tutorial_button = pygame.Rect(WIDTH // 2, HEIGHT // 5, 300, 100)
        tutorial_button.center = (WIDTH // 2, HEIGHT // 5)
        menu_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 2, 300, 100)
        menu_button.center = (WIDTH // 2, HEIGHT // 5 * 2)
        resume_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 3, 300, 100)
        resume_button.center = (WIDTH // 2, HEIGHT // 5 * 3)
        exit_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 4, 300, 100)
        exit_button.center = (WIDTH // 2, HEIGHT // 5 * 4)

        pygame.draw.rect(self.screen, BROWN, tutorial_button, 0, 10, 10, 10, 10)
        pygame.draw.rect(self.screen, BROWN, menu_button, 0, 10, 10, 10, 10)
        pygame.draw.rect(self.screen, BROWN, resume_button, 0, 10, 10, 10, 10)
        pygame.draw.rect(self.screen, BROWN, exit_button, 0, 10, 10, 10, 10)

        tutorial_text = FONT.render("Tutorial", True, BLACK)
        tutorial_rect = tutorial_text.get_rect(center=tutorial_button.center)
        self.screen.blit(tutorial_text, tutorial_rect)
        menu_text = FONT.render("Main Menu", True, BLACK)
        menu_rect = menu_text.get_rect(center=menu_button.center)
        self.screen.blit(menu_text, menu_rect)
        resume_text = FONT.render("Resume", True, BLACK)
        resume_rect = resume_text.get_rect(center=resume_button.center)
        self.screen.blit(resume_text, resume_rect)
        exit_text = FONT.render("Exit", True, BLACK)
        exit_rect = exit_text.get_rect(center=exit_button.center)
        self.screen.blit(exit_text, exit_rect)