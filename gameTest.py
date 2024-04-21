import pygame
import sys
import random

import neat
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shlooby Vs Gooby: A Game To Get Money")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Character properties
character_width = 75
character_height = 75
DEFAULT_IMAGE_SIZE = (character_width, character_height)
character_x = (WIDTH - character_width) // 2 - 50
character_y = (HEIGHT - character_height) // 2
character_speed = 15
character_direction = 'STOP'  # Initial direction

shlooby = pygame.image.load('shlooby.png')
shlooby = pygame.transform.scale(shlooby, DEFAULT_IMAGE_SIZE)
money = pygame.image.load('money.png')
money = pygame.transform.scale(money, DEFAULT_IMAGE_SIZE)

# Yellow square properties
yellow_square_width = 50
yellow_square_height = 50
yellow_square_x = (WIDTH - yellow_square_width) // 2
yellow_square_y = (HEIGHT - yellow_square_height) // 2

# Score
score = 0

def spawn_yellow_square():
    return random.randint(0, WIDTH - yellow_square_width), random.randint(0, HEIGHT - yellow_square_height)

def check_hit():
    global character_x, character_y, character_direction, score
     # Check if the character hits an edge
    if character_x < 0 or character_x + character_width > WIDTH or \
            character_y < 0 or character_y + character_height > HEIGHT:
        # Reset character position to center
        character_x = (WIDTH - character_width) // 2
        character_y = (HEIGHT - character_height) // 2
        character_direction = 'STOP'
        score = 0

def handle_input():
    global character_x, character_y, character_direction, score

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Change character direction
    if keys[pygame.K_LEFT]:
        character_direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        character_direction = 'RIGHT'
    elif keys[pygame.K_UP]:
        character_direction = 'UP'
    elif keys[pygame.K_DOWN]:
        character_direction = 'DOWN'

    # Update character position based on direction
    if character_direction == 'LEFT':
        character_x -= character_speed
    elif character_direction == 'RIGHT':
        character_x += character_speed
    elif character_direction == 'UP':
        character_y -= character_speed
    elif character_direction == 'DOWN':
        character_y += character_speed

    check_hit()

def draw_game():
    # Fill the screen with background color
    screen.fill(WHITE)

    # Draw the character
    screen.blit(shlooby, (character_x, character_y))

    # Draw the yellow square
    screen.blit(money, (yellow_square_x, yellow_square_y))

    # Render the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render("Shlooby score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input and update character position
    handle_input()

    # Check if the character collects the yellow square
    if character_x < yellow_square_x + yellow_square_width and character_x + character_width > yellow_square_x \
            and character_y < yellow_square_y + yellow_square_height and character_y + character_height > yellow_square_y:
        # Respawn yellow square at a different spot
        yellow_square_x, yellow_square_y = spawn_yellow_square()
        # Increase score
        score += 1

    # Draw game elements
    draw_game()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
