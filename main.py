import pygame
import sys

pygame.init()

pygame.display.set_caption("NAME | Ignition Hacks")
pygame.display.set_icon(pygame.image.load("./Graphics/Logo.png"))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()


#test
t = 1          