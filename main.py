import pygame
import sys

pygame.init()

pygame.display.set_caption("GAME NAME | Ignition Hacks")
pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

clock = pygame.time.Clock()

car_original = pygame.transform.scale(pygame.image.load("./Graphics/Car.png").convert_alpha(), (35, 35))
background = pygame.transform.scale(pygame.image.load("./Graphics/Background.png").convert_alpha(), (WIDTH, HEIGHT))

font = pygame.font.SysFont("./Font/PoetsenOne-Regular.ttf", 30)

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)

player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
car = car_original
rotation_angle = 0

scene = "menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill("black")

    if scene == "menu":
        background_rect = background.get_rect()
        background_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(background, (background_rect))
        
        pygame.draw.rect(screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 2, WIDTH // 10 * 6 + (background_rect.width // 10 * 3) - WIDTH // 10, 50), 0, 10, 10, 10, 10)
        title_text = font.render("GAME NAME", True, BLACK)
        title_rect = title_text.get_rect(center = (WIDTH // 10 + ((WIDTH // 10 * 6 + (background_rect.width // 10 * 3) - WIDTH // 10) // 2), HEIGHT // 10 * 2 + 25))
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 8, background_rect.width // 10 * 3, 50), 0, 10, 10, 10, 10)
        play_text = font.render("G2 Preparation", True, BLACK)
        play_rect = play_text.get_rect(center = (WIDTH // 10 + (background_rect.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 25))
        screen.blit(play_text, play_rect)

        pygame.draw.rect(screen, BROWN, (WIDTH // 10 * 6, HEIGHT // 10 * 8, background_rect.width // 10 * 3, 50), 0, 10, 10, 10, 10)
        exit_text = font.render("Exit", True, BLACK)
        exit_rect = exit_text.get_rect(center = (WIDTH // 10 * 6 + (background_rect.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 25))
        screen.blit(exit_text, exit_rect)

    elif scene == "game": 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            movement = pygame.Vector2(0, -5)
            movement.rotate_ip(-rotation_angle)
            player_pos += movement
        elif keys[pygame.K_s]:
            movement = pygame.Vector2(0, 5)
            movement.rotate_ip(-rotation_angle)
            player_pos += movement
        elif keys[pygame.K_a]:
            rotation_angle += 5
            if rotation_angle >= 360:
                rotation_angle -= 360
        elif keys[pygame.K_d]:
            rotation_angle -= 5
            if rotation_angle < 0:
                rotation_angle += 360
    
        car = pygame.transform.rotate(car_original, rotation_angle)
        car_rect = car.get_rect(center = player_pos)
        screen.blit(car, car_rect)
    
    pygame.display.update()

    clock.tick(60)