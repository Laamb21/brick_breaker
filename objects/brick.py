#objects/brick.py

import pygame
from settings import BRICK_COLOR

class Brick:
    def __init__(self, x, y, width=60, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, BRICK_COLOR, (self.x, self.y, self.width, self.height))