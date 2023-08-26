import pygame
import math
from constants import *


class Level:
    def __init__(self, screen, game_state_manager, position=pygame.Vector2(WIDTH // 2, HEIGHT // 2)):
        self.screen = screen
        self.game_state_manager = game_state_manager

        self.car_pos = position
        self.car = CAR_ORIGINAL
        self.rot_angle = 0
        self.velocity = 0
        self.acceleration = 0.6
        self.max_vel = 7
        self.ang_vel = 0
        self.ang_accel = 1
        self.max_ang_vel = 3
        self.friction = 0.9
        self.rot_friction = 0.9

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

        # keeps velocity and ang_vel in bounds
        if self.velocity < -self.max_vel:
            self.velocity = -self.max_vel
        elif self.velocity > self.max_vel:
            self.velocity = self.max_vel

        if self.ang_vel < -self.max_ang_vel:
            self.ang_vel = -self.max_ang_vel
        elif self.ang_vel > self.max_ang_vel:
            self.ang_vel = self.max_ang_vel

        self.rot_angle %= 360

        self.car_pos.x += self.velocity * math.sin(math.radians(self.rot_angle))
        self.car_pos.y += self.velocity * math.cos(math.radians(self.rot_angle))
        self.velocity *= self.friction

        self.rot_angle += -1 * self.ang_vel * self.velocity / self.max_vel  # relates turning to velocity
        self.ang_vel *= self.rot_friction

        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        car_rect = self.car.get_rect(center=self.car_pos)

        self.screen.blit(self.car, car_rect)
