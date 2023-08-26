import pygame
import sys
import math

pygame.init()

pygame.display.set_caption("GAME NAME | Ignition Hacks")
pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

clock = pygame.time.Clock()

car_original = pygame.image.load('./Graphics/Car.png')
background = pygame.transform.scale(pygame.image.load("./Graphics/Background.png").convert_alpha(), (WIDTH, HEIGHT))
car = car_original
font = pygame.font.SysFont("./Font/PoetsenOne-Regular.ttf", 30)

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)

rot_angle = 0
car_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
velocity = 0
acceleration = 0.6
max_vel = 7
ang_vel = 0
ang_accel = 1
max_ang_vel = 3
friction = 0.9
rot_friction = 0.9

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
            velocity -= acceleration
        if keys[pygame.K_s]:
            velocity += acceleration * 0.2
        if keys[pygame.K_a]:
            ang_vel += ang_accel
        if keys[pygame.K_d]:
            ang_vel -= ang_accel

        # keeps velocity and ang_vel in bounds
        if velocity < -max_vel:
            velocity = -max_vel
        elif velocity > max_vel:
            velocity = max_vel

        if ang_vel < -max_ang_vel:
            ang_vel = -max_ang_vel
        elif ang_vel > max_ang_vel:
            ang_vel = max_ang_vel

        rot_angle %= 360

        car_pos.x += velocity * math.sin(math.radians(rot_angle))
        car_pos.y += velocity * math.cos(math.radians(rot_angle))
        velocity *= friction

        rot_angle += -1 * ang_vel * velocity / max_vel  # relates turning to velocity
        ang_vel *= rot_friction

        car = pygame.transform.rotate(car_original, rot_angle)
        car_rect = car.get_rect(center=car_pos)
        screen.blit(car, car_rect)

    pygame.display.update()

    clock.tick(60)
