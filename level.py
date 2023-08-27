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
        self.ang_accel = 10
        self.max_ang_vel = 5
        self.friction = 0.95
        self.rot_friction = 0.95

        self.minimap = Minimap(self.screen)
        self.map = Map(self.screen)

        self.accelerator_image = pygame.image.load(os.path.join("Graphics", "Accelerator.png"))
        self.accelerator_rect = self.accelerator_image.get_rect(center = (WIDTH // 10 * 9, HEIGHT // 10 * 8))

        self.brake_image = pygame.image.load(os.path.join("Graphics", "Brake.png"))
        self.brake_rect = self.brake_image.get_rect(center = (WIDTH // 10 * 8, HEIGHT // 10 * 8.5))
        self.pause_rect = pygame.Rect(WIDTH // 10 * 9.5 - 25, HEIGHT // 10 - 25, 50, 50)
        self.minimap = Minimap(self.screen)

        self.gear_image = pygame.image.load(os.path.join("Graphics", "Drive.png"))
        self.gear_rect = self.gear_image.get_rect(center = (WIDTH // 10 * 9.6, HEIGHT // 10 * 8.2))
        self.current_gear = "Drive"

        self.wheel_clicked = False
        self.wheel_image = pygame.image.load(os.path.join("Graphics", "SteeringWheel.png"))
        self.wheel_rect = self.wheel_image.get_rect(midbottom=(WIDTH // 10 + 10, HEIGHT - HEIGHT // 10 - 10))

    def run(self):
        keys = pygame.key.get_pressed()

        if self.current_gear == "Drive":
            if keys[pygame.K_w]:
                self.velocity -= self.acceleration
            if keys[pygame.K_s]:
                if self.velocity <= 0:
                    self.velocity = 0
                else:
                    self.velocity += self.acceleration * 0.2
            if keys[pygame.K_a]:
                self.ang_vel = self.max_ang_vel
            elif keys[pygame.K_d]:
                self.ang_vel = -self.max_ang_vel
            else:
                self.ang_vel = 0
        elif self.current_gear == "Reverse":
            if keys[pygame.K_w]:
                if self.velocity <= 0:
                    self.velocity = 0
                else:
                    self.velocity -= self.acceleration * 0.2
            if keys[pygame.K_s]:
                self.velocity += self.acceleration * 0.2
            if keys[pygame.K_a]:
                self.ang_vel = -self.max_ang_vel
            elif keys[pygame.K_d]:
                self.ang_vel = self.max_ang_vel
            else:
                self.ang_vel = 0
        elif self.current_gear == "Park":
                self.velocity = 0

        if self.velocity < -self.max_vel:
            self.velocity = -self.max_vel
        elif self.velocity > self.max_vel:
            self.velocity = self.max_vel

        self.rot_angle += -1 * self.ang_vel * self.velocity / self.max_vel
        self.ang_vel *= self.rot_friction

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

        self.wheel_rect.bottomleft = (WIDTH // 10 + 10, HEIGHT - HEIGHT // 10 - 10)

        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        car_rect = self.car.get_rect(center=self.car_pos)

        free_control = self.map.update_map(self.car_pos.x, self.car_pos.y)
        self.map.update_map(self.car_pos.x, self.car_pos.y)
        self.draw_wheel()
        self.rot_angle += -1 * self.ang_vel * self.velocity / self.max_vel
        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        car_rect = (WIDTH // 2, HEIGHT // 2)
        self.ang_vel *= self.rot_friction
        self.velocity *= self.friction
        self.car = pygame.transform.rotate(CAR_ORIGINAL, self.rot_angle)
        self.screen.blit(self.car, car_rect)
        self.draw_accelerator()
        self.draw_brake()
        self.draw_gear()
        self.draw_pause()
        self.minimap.update_minimap(self.car_pos.x, self.car_pos.y)

    def draw_accelerator(self):
        self.screen.blit(self.accelerator_image, self.accelerator_rect)

    def draw_brake(self):
        self.screen.blit(self.brake_image, self.brake_rect)

    def draw_gear(self):
        if self.current_gear == "Drive":
            self.gear_mode_image = pygame.image.load(os.path.join("Graphics", "Drive.png"))
        elif self.current_gear == "Park":
            self.gear_mode_image = pygame.image.load(os.path.join("Graphics", "Park.png"))
        elif self.current_gear == "Reverse":
            self.gear_mode_image = pygame.image.load(os.path.join("Graphics", "Reverse.png"))
        self.screen.blit(self.gear_mode_image, self.gear_rect)

    def draw_pause(self):
        pygame.draw.circle(self.screen, GRAY, self.pause_rect.center, 25)
        pygame.draw.rect(self.screen, WHITE, (self.pause_rect.left + 10, self.pause_rect.top + 10, 10, 30))
        pygame.draw.rect(self.screen, WHITE, (self.pause_rect.right - 20, self.pause_rect.top + 10, 10, 30))

    def draw_wheel(self):
        rotated_wheel = pygame.transform.rotate(self.wheel_image, self.rot_angle)
        self.wheel_rect = rotated_wheel.get_rect(midbottom = (WIDTH // 10 + 10, HEIGHT - HEIGHT // 10 - 10))
    
        if self.wheel_clicked:
            mouse_pos = pygame.mouse.get_pos()
            rel_x = mouse_pos[0] - self.wheel_rect.centerx
            rel_y = mouse_pos[1] - self.wheel_rect.centery
            angle = math.degrees(math.atan2(rel_y, rel_x))
            self.rot_angle = max(min(angle, 45), -45)
    
        self.screen.blit(rotated_wheel, self.wheel_rect)

    def rotate_wheel(self, angle):
        self.rot_angle += angle
        self.wheel_image = pygame.transform.rotate(pygame.image.load(os.path.join("Graphics", "SteeringWheel.png")), self.rot_angle)
        self.wheel_rect = self.wheel_image.get_rect(bottomleft=(WIDTH // 10 + 10, HEIGHT - HEIGHT // 10 - 10))

    def accelerate(self):
        if self.current_gear == "Drive":
                self.velocity -= self.acceleration
        elif self.current_gear == "Park":
            self.velocity = 0
        elif self.current_gear == "Reverse":
            self.velocity += self.acceleration

    def accelerator(self):
        accelerator_rect = pygame.Rect(WIDTH // 10 * 9, HEIGHT // 10 * 8, 45, 115)
        pygame.draw.rect(self.screen, GRAY, accelerator_rect)

    def brake(self):
        if self.current_gear == "Drive":
            if self.velocity <= 0:
                self.velocity = 0
            else:
                self.velocity += self.acceleration * 0.2
        elif self.current_gear == "Park":
                self.velocity = 0
        elif self.current_gear == "Reverse":
            if self.velocity <= 0:
                self.velocity = 0
            else:
                self.velocity -= self.acceleration * 0.2
    
    def gear(self):
        if self.current_gear == "Drive":
            self.current_gear = "Park"
        elif self.current_gear == "Park":
            self.current_gear = "Reverse"
        elif self.current_gear == "Reverse":
            self.current_gear = "Drive"