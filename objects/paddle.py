#objects/paddle.py 

import pygame
from settings import WIDTH, HEIGHT, WHITE

class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 30
        self.speed = 7

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        #Keep paddle within screen boundaries
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))