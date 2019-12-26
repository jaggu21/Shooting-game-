import pygame
import random


class Enemy(object):
    moveRight = [pygame.image.load('level2/R1E.png'), pygame.image.load('level2/R2E.png'), pygame.image.load('level2/R3E.png'), pygame.image.load('level2/R4E.png'), pygame.image.load('level2/R5E.png'), pygame.image.load('level2/R6E.png'), pygame.image.load('level2/R7E.png'), pygame.image.load('level2/R8E.png'), pygame.image.load('level2/R9E.png'), pygame.image.load('level2/R10E.png'), pygame.image.load('level2/R11E.png')]
    moveLeft = [pygame.image.load('level2/L1E.png'), pygame.image.load('level2/L2E.png'), pygame.image.load('level2/L3E.png'), pygame.image.load('level2/L4E.png'), pygame.image.load('level2/L5E.png'), pygame.image.load('level2/L6E.png'), pygame.image.load('level2/L7E.png'), pygame.image.load('level2/L8E.png'), pygame.image.load('level2/L9E.png'), pygame.image.load('level2/L10E.png'), pygame.image.load('level2/L11E.png')]


    def __init__(self, y, width, height):
        self.x = random.randint(0, 1) * 788
        self.y = y
        self.width = width
        self.height = height
         
        self.moveCount = 0
        self.speed = 3
        self.hitbox = (self.x, self.y, 50, 65)
        self.health = 10
        self.visible = True

    def draw(self, gameDisplay, hero):
        self.move(hero)
        if self.visible == True:
            if self.moveCount + 1 >= 33:
                self.moveCount = 0
            if self.speed > 0:
                gameDisplay.blit(self.moveRight[self.moveCount//3], (self.x, self.y))
                self.moveCount += 1
            else:
                gameDisplay.blit(self.moveLeft[self.moveCount//3], (self.x, self.y))
                self.moveCount += 1
            if self.speed > 0:
                self.hitbox = (self.x + 10, self.y, 40, 65)
            else:
                self.hitbox = (self.x + 20, self.y, 40, 65)

            pygame.draw.rect(gameDisplay, (255,0,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(gameDisplay, (0,128,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 2)
        else:
            self.visible = True
            self.health = 10
            self.x = random.randint(0, 1) * 788
            
            pygame.draw.rect(gameDisplay, (255,0,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(gameDisplay, (0,128,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.draw(gameDisplay, hero)

        

    def move(self, hero):
        
        if hero.x_player - self.x > 0:
            self.speed = abs(self.speed)
            self.x += self.speed
        else:
            self.speed = abs(self.speed) * -1
            self.x += self.speed
        
        

     #   if self.speed > 0:
     #      if self.x + self.speed< self.path[1]:
     #         self.x += self.speed
     #    else:
     #       self.speed = self.speed * -1
     #      self.moveCount = 0
     # else:
     #    if self.x - self.speed > self.path[0]:
     #        self.x += self.speed
     #   else:
     #      self.speed = self.speed * -1
     #     self.moveCount = 0
        
        

    def hit(self):
         #print("KILL")
         if self.health > 0:
             self.health -= 1
         else:
             self.visible = False
             


