#objects/ball.py

import pygame
from settings import WIDTH, HEIGHT, WHITE

class Ball:
    def __init__(self):
        self.radius = 8
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_speed = 4
        self.y_speed = -4

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.x, self.y), self.radius)

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_speed = 4
        self.y_speed = -4