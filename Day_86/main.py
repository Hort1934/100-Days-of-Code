import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the game variables
paddle_width, paddle_height = 100, 10
paddle_x = (window_width - paddle_width) // 2
paddle_y = window_height - paddle_height - 10
paddle_speed = 5

ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_dx = 3
ball_dy = -3

brick_width, brick_height = 75, 20
brick_gap = 10
num_bricks_x = window_width // (brick_width + brick_gap)
num_bricks_y = 4
bricks = []

for i in range(num_bricks_y):
    for j in range(num_bricks_x):
        brick_x = j * (brick_width + brick_gap) + brick_gap
        brick_y = i * (brick_height + brick_gap) + brick_gap
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[K_RIGHT] and paddle_x < window_width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x < 0 or ball_x > window_width:
        ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1
    if ball_y > window_height:
        # Game over, reset the ball and paddle position
        ball_x = window_width // 2
        ball_y = window_height // 2
        paddle_x = (window_width - paddle_width) // 2

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    if ball_rect.colliderect(paddle_rect):
        ball_dy *= -1

    for brick in bricks:
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1

    window.fill(BLACK)

    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(window, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    for brick in bricks:
        pygame.draw.rect(window, WHITE, brick)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
