import pygame
import math
from minimap import Minimap
from map import Map
from constants import *


class Level:
    def __init__(self, screen, game_state_manager, position=pygame.Vector2(200, 200)):
        self.screen = screen
        self.game_state_manager = game_state_manager

        self.car_pos = position
        self.car = CAR_ORIGINAL
        self.rot_angle = 0
        self.velocity = 0
        self.acceleration = 10
        self.max_vel = 25
        self.ang_vel = 0
        self.ang_accel = 0.5
        self.max_ang_vel = 3
        self.friction = 0.95
        self.rot_friction = 0.9

        self.minimap = Minimap(self.screen)
        self.map = Map(self.screen)

        self.accelerator_image = pygame.image.load(os.path.join("Graphics", "Accelerator.png"))
        self.accelerator_rect = self.accelerator_image.get_rect(center=(WIDTH // 10 * 9, HEIGHT // 10 * 8))

        self.brake_image = pygame.image.load(os.path.join("Graphics", "Brake.png"))
        self.brake_rect = self.brake_image.get_rect(center=(WIDTH // 10 * 8, HEIGHT // 10 * 8.5))
        self.pause_rect = pygame.Rect(WIDTH // 10 * 9.5 - 25, HEIGHT // 10 - 25, 50, 50)
        self.minimap = Minimap(self.screen)  # image dimensions

        self.wheel_image = pygame.image.load(os.path.join("Graphics", "SteeringWheel.png"))
        self.wheel_rect = self.wheel_image.get_rect(bottomleft=(WIDTH // 10, HEIGHT - HEIGHT // 10))

    def run(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity -= self.acceleration
        if keys[pygame.K_s]:
            self.velocity += self.acceleration * 0.2
        if keys[pygame.K_a]:
            self.ang_vel += self.ang_accel
        if keys[pygame.K_d]:
            self.ang_vel -= self.ang_accel

        if self.velocity < -self.max_vel:
            self.velocity = -self.max_vel
        elif self.velocity > self.max_vel:
            self.velocity = self.max_vel

        if self.ang_vel < -self.max_ang_vel:
            self.ang_vel = -self.max_ang_vel
        elif self.ang_vel > self.max_ang_vel:
            self.ang_vel = self.max_ang_vel

        self.rot_angle %= 360

        dist_x = self.velocity * math.sin(math.radians(self.rot_angle))
        dist_y = self.velocity * math.cos(math.radians(self.rot_angle))

        if 0 < self.car_pos.x + dist_x < MAP_X - 67:
            self.car_pos.x += dist_x
        else:
            self.velocity = 0
        if 0 < self.car_pos.y + dist_y < MAP_Y - 67:
            self.car_pos.y += dist_y
        else:
            self.velocity = 0

        self.rot_angle += -1 * self.ang_vel * self.velocity / self.max_vel
        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        car_rect = (WIDTH // 2, HEIGHT // 2)

        self.ang_vel *= self.rot_friction
        self.velocity *= self.friction

        self.map.update_map(self.car_pos.x, self.car_pos.y)
        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        self.screen.blit(self.car, car_rect)

        self.draw_accelerator()
        self.draw_brake()
        self.draw_pause()
        self.draw_wheel()
        self.minimap.update_minimap(self.car_pos.x, self.car_pos.y)

    def draw_accelerator(self):
        self.screen.blit(self.accelerator_image, self.accelerator_rect)

    def draw_brake(self):
        self.screen.blit(self.brake_image, self.brake_rect)

    def draw_pause(self):
        pygame.draw.circle(self.screen, GRAY, self.pause_rect.center, 25)
        pygame.draw.rect(self.screen, WHITE, (self.pause_rect.left + 10, self.pause_rect.top + 10, 10, 30))
        pygame.draw.rect(self.screen, WHITE, (self.pause_rect.right - 20, self.pause_rect.top + 10, 10, 30))

    def draw_wheel(self):
        self.screen.blit(self.wheel_image, self.wheel_rect)

    def rotate_wheel(self, angle):
        self.wheel_image = pygame.transform.rotate(self.wheel_image, angle)

    def accelerate(self):
        self.velocity -= self.acceleration

    def accelerator(self):
        accelerator_rect = pygame.Rect(WIDTH // 10 * 9, HEIGHT // 10 * 8, 45, 115)
        pygame.draw.rect(self.screen, GRAY, accelerator_rect)

    def brake(self):
        self.velocity += self.acceleration * 0.2
