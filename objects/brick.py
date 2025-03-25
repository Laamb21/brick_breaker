#objects/brick.py

import pygame
from settings import RED

class Brick:
    def __init__(self, x, y, color, width=60, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.color = color

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))