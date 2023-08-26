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

player_pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
car_original = pygame.image.load('./Graphics/Car.png')
car = car_original
rotation_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill("black")

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