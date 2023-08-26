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
font = pygame.font.SysFont("./Font/PoetsenOne-Regular.ttf", 40)

BROWN = (194, 114, 77)
BLACK = (0, 0, 0)
GRAY = (217, 217, 217)
WHITE = (255, 255, 255)

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

def menu():
    global scene
    background_rect = background.get_rect()
    background_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(background, (background_rect))
        
    pygame.draw.rect(screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 2, WIDTH // 10 * 6 + (background_rect.width // 10 * 3) - WIDTH // 10, 70), 0, 10, 10, 10, 10)
    title_text = font.render("GAME NAME", True, BLACK)
    title_rect = title_text.get_rect(center = (WIDTH // 10 + ((WIDTH // 10 * 6 + (background_rect.width // 10 * 3) - WIDTH // 10) // 2), HEIGHT // 10 * 2 + 35))
    screen.blit(title_text, title_rect)

    pygame.draw.rect(screen, BROWN, (WIDTH // 10, HEIGHT // 10 * 8, background_rect.width // 10 * 3, 70), 0, 10, 10, 10, 10)
    play_text = font.render("G2 Preparation", True, BLACK)
    play_rect = play_text.get_rect(center = (WIDTH // 10 + (background_rect.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 35))
    screen.blit(play_text, play_rect)

    pygame.draw.rect(screen, BROWN, (WIDTH // 10 * 6, HEIGHT // 10 * 8, background_rect.width // 10 * 3, 70), 0, 10, 10, 10, 10)
    exit_text = font.render("Exit", True, BLACK)
    exit_rect = exit_text.get_rect(center = (WIDTH // 10 * 6 + (background_rect.width // 10 * 3) // 2, HEIGHT // 10 * 8 + 35))
    screen.blit(exit_text, exit_rect)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if (WIDTH // 10 < event.pos[0] < WIDTH // 10 + background_rect.width // 10 * 3) and (HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
            scene = "game"
        elif (WIDTH // 10 * 6 < event.pos[0] < WIDTH // 10 * 6 + background_rect.width // 10 * 3) and (HEIGHT // 10 * 8 < event.pos[1] < HEIGHT // 10 * 8 + 50):
            pygame.quit()
            sys.exit()
    
def game():
    global rot_angle, car_pos, velocity, acceleration, max_vel, ang_vel, ang_accel, max_ang_vel, friction, rot_friction
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

def pause():
    global scene
    pygame.draw.circle(screen, GRAY, (WIDTH // 10 * 9.5, HEIGHT // 10), 25)
    pygame.draw.rect(screen, WHITE, (WIDTH // 10 * 9.5 - 14, HEIGHT // 10 - 15, 10, 30))
    pygame.draw.rect(screen, WHITE, (WIDTH // 10 * 9.5 + 6, HEIGHT // 10 - 15, 10, 30))
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if ((WIDTH // 10 * 9.5 - 25 < event.pos[0] < WIDTH // 10 * 9.5 + 25) and (HEIGHT // 10 - 25 < event.pos[1] < HEIGHT // 10 + 25)):
            scene = "pause"

def pause_scene():
    global scene

    background_rect = background.get_rect()
    background_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(background, (background_rect))

    tutorial_button = pygame.Rect(WIDTH // 2, HEIGHT // 5, 300, 100)
    tutorial_button.center = (WIDTH // 2, HEIGHT // 5)
    menu_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 2, 300, 100)
    menu_button.center = (WIDTH // 2, HEIGHT // 5 * 2)
    resume_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 3, 300, 100)
    resume_button.center = (WIDTH // 2, HEIGHT // 5 * 3)
    exit_button = pygame.Rect(WIDTH // 2, HEIGHT // 5 * 4, 300, 100)
    exit_button.center = (WIDTH // 2, HEIGHT // 5 * 4)

    pygame.draw.rect(screen, BROWN, tutorial_button, 0, 10, 10, 10, 10)
    pygame.draw.rect(screen, BROWN, menu_button, 0, 10, 10, 10, 10)
    pygame.draw.rect(screen, BROWN, resume_button, 0, 10, 10, 10, 10)
    pygame.draw.rect(screen, BROWN, exit_button, 0, 10, 10, 10, 10)
    
    tutorial_text = font.render("Tutorial", True, BLACK)
    tutorial_rect = tutorial_text.get_rect(center = tutorial_button.center)
    screen.blit(tutorial_text, tutorial_rect)
    menu_text = font.render("Main Menu", True, BLACK)
    menu_rect = menu_text.get_rect(center = menu_button.center)
    screen.blit(menu_text, menu_rect)
    resume_text = font.render("Resume", True, BLACK)
    resume_rect = resume_text.get_rect(center = resume_button.center)
    screen.blit(resume_text, resume_rect)
    exit_text = font.render("Exit", True, BLACK)
    exit_rect = exit_text.get_rect(center = exit_button.center)
    screen.blit(exit_text, exit_rect)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if tutorial_button.collidepoint(mouse_pos):
            print("tutorial")
        elif menu_button.collidepoint(mouse_pos):
            scene = "menu"
        elif resume_button.collidepoint(mouse_pos):
            scene = "game"
        elif exit_button.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    if scene == "menu":
        menu()
    elif scene == "game":
        game()
        pause()
    elif scene == "pause":
        pause_scene()

    pygame.display.update()

    clock.tick(60)