import pygame

# Loading Images for Moving Right and Moving Left are given in a List.
moveright = [pygame.image.load('level3/R1.png'), pygame.image.load('level3/R2.png'), pygame.image.load('level3/R3.png'),
             pygame.image.load('level3/R4.png')]
moveleft = [pygame.image.load('level3/L1.png'), pygame.image.load('level3/L2.png'), pygame.image.load('level3/L3.png'),
            pygame.image.load('level3/L4.png')]

Resolution = pygame.display.set_mode((1200, 600))


# We defined class for all the Operayion of main character that is our Hero.
class main_character(object):
    def __init__(self, x_cordinate, y_cordinate, width, height):
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.width = width
        self.height = height
        self.speed = 5
        self.jumping = False
        self.jump = 10
        self.leftside = False
        self.rightside = False
        self.movecount = 0
        self.still = True
        self.gameover = False
        self.box = (self.x_cordinate + 7, self.y_cordinate + 11, 16, 52)

    # This function defines the movement of main character(HERO).
    def movement(self, Resolution):
        if self.movecount + 1 >= 12:
            self.movecount = 0

        if not (self.still):
            if self.leftside:
                Resolution.blit(moveleft[self.movecount // 3], (self.x_cordinate, self.y_cordinate))
                self.movecount += 1
            elif self.rightside:
                Resolution.blit(moveright[self.movecount // 3], (self.x_cordinate, self.y_cordinate))
                self.movecount += 1
        else:
            if self.rightside:
                Resolution.blit(moveright[0], (self.x_cordinate, self.y_cordinate))
            else:
                Resolution.blit(moveleft[0], (self.x_cordinate, self.y_cordinate))
        self.box = (self.x_cordinate + 7, self.y_cordinate + 11, 16, 52)
        # pygame.draw.rect(Resolution, (255,0,0), self.box,2)
