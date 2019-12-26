import pygame
import os

class Enemy(object):
    moveright = [pygame.image.load(os.path.join('level1', 'R1E.png')), pygame.image.load(os.path.join('level1', 'R2E.png')), pygame.image.load(os.path.join('level1', 'R3E.png')),
                 pygame.image.load(os.path.join('level1', 'R4E.png')), pygame.image.load(os.path.join('level1', 'R5E.png')), pygame.image.load(os.path.join('level1', 'R6E.png')),
                 pygame.image.load(os.path.join('level1', 'R7E.png')), pygame.image.load(os.path.join('level1', 'R8E.png')), pygame.image.load(os.path.join('level1', 'R9E.png')),
                 pygame.image.load(os.path.join('level1', 'R10E.png')), pygame.image.load(os.path.join('level1', 'R11E.png'))]
    moveleft = [pygame.image.load(os.path.join('level1', 'L1E.png')), pygame.image.load(os.path.join('level1', 'L2E.png')), pygame.image.load(os.path.join('level1', 'L3E.png')),
                pygame.image.load(os.path.join('level1', 'L4E.png')), pygame.image.load(os.path.join('level1', 'L5E.png')), pygame.image.load(os.path.join('level1', 'L6E.png')),
                pygame.image.load(os.path.join('level1', 'L7E.png')), pygame.image.load(os.path.join('level1', 'L8E.png')), pygame.image.load(os.path.join('level1', 'L9E.png')),
                pygame.image.load(os.path.join('level1', 'L10E.png')), pygame.image.load(os.path.join('level1', 'L11E.png'))]

    def __init__(self, x_cordinate, y_cordinate, width, height, boundary):
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.width = width
        self.height = height
        self.boundary = boundary
        # We are giving path to make to move enemy in the limits.
        self.path = [x_cordinate, boundary]
        self.movecount = 0
        # We are giving enemy speed.
        self.speed = 5
        # We are declaring a Rectangle Box to frame the position of Enemy. Because we can't get the Perfect Cordinates of Enemy character.
        self.box = (self.x_cordinate + 17, self.y_cordinate + 2, 31, 57)
        self.seen = True

    # This function defines the movement of Enemy character according to SPRITES we loaded.
    def movement(self, Resolution):
        self.move()
        if self.movecount + 1 >= 33:
            self.movecount = 0

        if self.speed > 0:
            Resolution.blit(self.moveright[self.movecount // 3], (self.x_cordinate, self.y_cordinate))
            self.movecount += 1
        else:
            Resolution.blit(self.moveleft[self.movecount // 3], (self.x_cordinate, self.y_cordinate))
            self.movecount += 1
        # We are declaring a Rectangle Box to frame the position of Enemy. Because we can't get the Perfect Cordinates of Enemy character.
        self.box = (self.x_cordinate + 17, self.y_cordinate + 2, 31, 57)

    # This function defines the automatic movement of enemy character in the Display Resolution.   
    def move(self):
        if self.speed > 0:
            if self.x_cordinate < self.path[1] + self.speed:
                self.x_cordinate += self.speed
            else:
                self.speed = self.speed * -1
                self.x_cordinate += self.speed
                self.movecount = 0
        else:
            if self.x_cordinate > self.path[0] - self.speed:
                self.x_cordinate += self.speed
            else:
                self.speed = self.speed * -1
                self.x_cordinate += self.speed
                self.movecount = 0
