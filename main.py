import pygame
import sys
import math

pygame.init()

pygame.display.set_caption("NAME | Ignition Hacks")
pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

clock = pygame.time.Clock()

car_original = pygame.image.load('./Graphics/Car.png')
car = car_original

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

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
