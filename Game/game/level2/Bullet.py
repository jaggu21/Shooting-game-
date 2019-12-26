import pygame
from Player import *


class Bullet(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, gameDisplay):
        pygame.draw.circle(gameDisplay, self.color, (self.x,self.y), self.radius)


