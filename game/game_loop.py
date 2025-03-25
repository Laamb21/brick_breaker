#game/game_loop.py

import sys
import pygame
from settings import WIDTH, HEIGHT, FPS, BLACK, LAVENDER, PASTEL_PINK, BABY_BLUE, LIGHT_YELLOW, MINT_GREEN, SOFT_PEACH
from objects.paddle import Paddle
from objects.ball import Ball
from objects.brick import Brick
from game.collisions import handle_brick_collisions, handle_paddle_collision, handle_wall_collisions

def create_bricks(rows, cols):
    bricks = []
    padding = 10
    offset_x = 35
    offset_y = 30
    brick_width = 60
    brick_height = 20

    # Define colors for each row of bricks
    row_colors = [
        PASTEL_PINK,
        BABY_BLUE,
        LIGHT_YELLOW,
        MINT_GREEN,
        SOFT_PEACH
    ]

    for row in range(rows):
        color = row_colors[row % len(row_colors)]
        for col in range(cols):
            x = offset_x + col * (brick_width + padding)
            y = offset_y + row * (brick_height + padding)
            bricks.append(Brick(x, y, color, brick_width, brick_height))
    return bricks

def run_game(screen):
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks(5, 10)

    running = True 
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #Handle user input for paddle movement 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move("left")
        if keys[pygame.K_RIGHT]:
            paddle.move("right")

        #Update ball position and check for collisions 
        ball.move()
        handle_wall_collisions(ball)
        handle_paddle_collision(ball, paddle)
        handle_brick_collisions(ball, bricks)

        #Reset ball if it goes off the bottom edge
        if ball.y - ball.radius > HEIGHT:
            ball.reset()

        #Drawing everything on the screen
        screen.fill(LAVENDER)
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
