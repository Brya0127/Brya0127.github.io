import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_width = 50
player_height = 50
player_x = 50
player_y = HEIGHT - player_height
player_jump = False
jump_count = 10

# Obstacle variables
obstacle_width = 50
obstacle_height = 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height

# Game variables
score = 0
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not player_jump:
                    player_jump = True

    window.fill(WHITE)

    # Draw player
    pygame.draw.rect(window, BLACK, (player_x, player_y, player_width, player_height))

    # Draw obstacle
    pygame.draw.rect(window, BLACK, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update player position
    if player_jump:
        if jump_count >= -10:
            player_y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
        else:
            player_jump = False
            jump_count = 10

    # Update obstacle position
    obstacle_x -= 5
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        obstacle_y = random.randint(200, HEIGHT - obstacle_height)

    # Collision detection
    if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width:
        if player_y + player_height > obstacle_y:
            running = False

    # Update score
    score += 1

    # Display score on the screen
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Game over message
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, BLACK)
window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

# # Wait for a few seconds before quitting
# pygame.time.wait(3000)

# # Quit the game
# pygame.quit()