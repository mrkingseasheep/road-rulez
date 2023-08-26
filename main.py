import pygame
import sys

pygame.init()

pygame.display.set_caption("NAME | Ignition Hacks")
pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
car = pygame.image.load('car.png')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
            pygame.quit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(car,(player_pos))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()