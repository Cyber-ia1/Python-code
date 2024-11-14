import pygame
import random

# Initialize the pygame
pygame.init()

# Define game window dimensions
WIDTH, HEIGHT = 900, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Define colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (170, 51, 106)
BLUE = (0, 0, 255)

# Define some constants
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
PADDLE_SPEED = 7

# Set up the clock for managing frame rate
clock = pygame.time.Clock()

# Define the paddles' positions and ball's starting position
left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS*2, BALL_RADIUS*2)

# Ball movement variables
ball_dx = BALL_SPEED_X * random.choice((-1, 1))  # Randomly start in either left or right direction
ball_dy = BALL_SPEED_Y * random.choice((-1, 1))

# Paddle movement variables
left_paddle_speed = 0
right_paddle_speed = 0

# Scoring
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

def draw():
    """ Function to handle drawing the paddles, ball, and score """
    WINDOW.fill(BLACK)  # Fill the screen with black background

    # Draw paddles and ball
    pygame.draw.rect(WINDOW, PINK, left_paddle)
    pygame.draw.rect(WINDOW, BLUE, right_paddle)
    pygame.draw.ellipse(WINDOW, RED, ball)
    
    # Draw center dividing line
    pygame.draw.aaline(WINDOW, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display score
    left_text = font.render(str(left_score), True, PINK)
    right_text = font.render(str(right_score), True, BLUE)
    WINDOW.blit(left_text, (WIDTH//4, 20))
    WINDOW.blit(right_text, (3*WIDTH//4, 20))

    # Update the display
    pygame.display.flip()

def move_ball():
    """ Function to move the ball and handle collisions """
    global ball_dx, ball_dy, left_score, right_score

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Bounce off the top and bottom of the screen
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1  # Reverse the vertical direction

    # Ball hits left paddle
    if ball.colliderect(left_paddle) and ball_dx < 0:
        ball_dx *= -1  # Reverse horizontal direction

    # Ball hits right paddle
    if ball.colliderect(right_paddle) and ball_dx > 0:
        ball_dx *= -1

    # Ball goes out of bounds on left side (right player scores)
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    # Ball goes out of bounds on right side (left player scores)
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

def move_paddles():
    """ Function to move paddles based on user input """
    left_paddle.y += left_paddle_speed
    right_paddle.y += right_paddle_speed

    # Prevent paddles from going off the screen
    if left_paddle.top <= 0:
        left_paddle.top = 0
    if left_paddle.bottom >= HEIGHT:
        left_paddle.bottom = HEIGHT

    if right_paddle.top <= 0:
        right_paddle.top = 0
    if right_paddle.bottom >= HEIGHT:
        right_paddle.bottom = HEIGHT

def reset_ball():
    """ Function to reset the ball to the center and give it a random direction """
    global ball_dx, ball_dy
    ball.x = WIDTH // 2 - BALL_RADIUS
    ball.y = HEIGHT // 2 - BALL_RADIUS
    ball_dx *= random.choice((-1, 1))  # Randomize the new direction
    ball_dy *= random.choice((-1, 1))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Control paddle movement with keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle_speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right_paddle_speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle_speed = PADDLE_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_speed = 0

    # Move the paddles and the ball
    move_paddles()
    move_ball()

    # Draw everything on the screen
    draw()

    # Limit the frame rate to 120 FPS
    clock.tick(80)

# Quit the game
pygame.quit()
