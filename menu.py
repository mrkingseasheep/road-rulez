from constants import *


class Menu:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.gameStateManager = game_state_manager

    def run(self):
        BACKGROUND_RECT.center = (WIDTH // 2, HEIGHT // 2)
        self.screen.blit(BACKGROUND, BACKGROUND_RECT)

        pygame.draw.rect(self.screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 2, WIDTH // 10 * 6 + (BACKGROUND_RECT.width // 10 * 3) - WIDTH // 10, 50), 0, 10, 10, 10, 10)
        title_text = FONT.render(TITLE, True, BLACK)
        title_rect = title_text.get_rect(center = (WIDTH // 10 + ((WIDTH // 10 * 6 + (BACKGROUND_RECT.width // 10 * 3) - WIDTH // 10) // 2), HEIGHT // 10 * 2 + 25))
        self.screen.blit(title_text, title_rect)

        pygame.draw.rect(self.screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 8, BACKGROUND_RECT.width // 10 * 3, 50), 0, 10, 10, 10, 10)
        play_text = FONT.render("Start Preparation", True, BLACK)
        play_rect = play_text.get_rect(center = (WIDTH // 10 + (BACKGROUND_RECT.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 25))
        self.screen.blit(play_text, play_rect)

        pygame.draw.rect(self.screen, BROWN, (WIDTH // 10 * 6, HEIGHT // 10 * 8, BACKGROUND_RECT.width // 10 * 3, 50), 0, 10, 10, 10, 10)
        exit_text = FONT.render("Exit", True, BLACK)
        exit_rect = exit_text.get_rect(center = (WIDTH // 10 * 6 + (BACKGROUND_RECT.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 25))
        self.screen.blit(exit_text, exit_rect)
