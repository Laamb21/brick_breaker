#game/collisions.py

from settings import WIDTH, HEIGHT

def handle_wall_collisions(ball):
    #Reverse x direction if ball hits left or right walls
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= WIDTH:
        ball.x_speed *= -1
    #Reverse y direction if ball hits the top wall
    if ball.y - ball.radius <= 0:
        ball.y_speed *= -1

def handle_paddle_collision(ball, paddle):
    if(paddle.y <= ball.y + ball.radius <= paddle.y + paddle.height) and \
      (paddle.x <= ball.x <= paddle.x + paddle.width):
        ball.y_speed *= -1

def handle_brick_collisions(ball, bricks):
    for brick in bricks:
        if brick.visible:
            if (brick.x < ball.x < brick.x + brick.width) and (brick.y < ball.y < brick.y + brick.height):
                ball.y_speed *= -1
                brick.visible = False
                break