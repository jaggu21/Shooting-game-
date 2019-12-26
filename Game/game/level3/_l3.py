import time

import pygame
from pygame import mixer

import enemy
import space
import main

pygame.init()


# Setting a logo for the game.
logo = pygame.image.load('level3/L1.png')
pygame.display.set_icon(logo)

# Setting Resolution of the screen of the game to be Displayed.
Resolution = pygame.display.set_mode((800, 600))

# Setting the Name for the Game.
pygame.display.set_caption("Smashing Bob!!")

# Adding a Background for the game.
background = pygame.image.load("level3/background1.png")
# adding space ship
space_ship = pygame.image.load("level3/ufo.png")

# Dispalying the gameover background.
gameoverbg = pygame.image.load('level3/over.jpg')

# Displays Trap in the Screen.
Trap = pygame.image.load('level3/pipe.png')
#Display flower
flower = pygame.image.load('level3/flower.png')

# sound
mixer.music.load("level3/background.wav")
mixer.music.play(-1)

fps = pygame.time.Clock()


# This Class is defined to Draw Bullets and give colour Radius and cordinates.
class Shooting(object):
    def __init__(self, x_cordinate, y_cordinate, radius, color, facing):
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, win):
        pygame.draw.circle(Resolution, self.color, (int(self.x_cordinate), int(self.y_cordinate)), self.radius)


# shooting enemies
class Shooting_enemies(object):
    def __init__(self, x_cordinate, y_cordinate, radius, color, facing):
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8 * facing

    def draw(self, win):
        pygame.draw.circle(Resolution, self.color, (int(self.x_cordinate), int(self.y_cordinate)), self.radius)


score = 0
scoreCount=0
health1 = 250
health2 = 250
healths = 500
health_hero = 150
"""highscore = 0
f = open("level3/scores.txt", "r")
highscr = f.read()
f.close()
highscore = int(highscr)"""

# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    score_value = over_font.render("Score: " + str(score), True, (255, 255, 255))
    Resolution.blit(over_text, (200, 100))
    Resolution.blit(score_value, (200, 300))
    time.sleep(0.5)
    """if scoreCount == 0:
        f = open("level3/scores.txt", "r")
        highscr = f.read()
        f.close()
        f = open("level3/scores.txt", "w")
        if int(highscr) < score:
            f.write(str(score))
            highscore = score
        else:
            f.write(str(highscore))
            highscore = highscore
        f.close()
        # print(score)
        scoreCount = 1"""


# We defined a function display_window because this function conatains all the content to Display.Other than this function any other classes or functions just do Internal part of the game.
# But this displpay_window funtion show what we want to show and we need  to call this funtion at last after the mainLoop.
def display_window():
    if hero.gameover == False:
        Resolution.blit(Trap, (200, 550))
        Resolution.blit(Trap, (600, 550))
        Resolution.blit(flower, (100,550))
        text = font.render('Score: ' + str(score), 1, (255, 255, 255))
        Resolution.blit(text, (650, 10))
        #hs = font.render('HighScore: ' + str(highscore), 1, (255, 255, 255))
        #Resolution.blit(hs, (630, 30))
        if health1>0:
            text_h1 = font.render(str(health1), 3, (255, 192, 203))
            Resolution.blit(text_h1, (enemy1.x_cordinate, enemy1.y_cordinate-10))
        if health2>0:
            text_h2 = font.render(str(health2), 3, (255, 192, 203))
            Resolution.blit(text_h2, (enemy2.x_cordinate, enemy2.y_cordinate-10))
        if healths>0:
            text_space = font.render(str(healths), 3, (255, 20, 147))
            Resolution.blit(text_space, (space_ship.x_cordinate, space_ship.y_cordinate-10))
        if 150>=health_hero>100:
            text_heroh_good = font.render(str(health_hero), 3, (255, 105, 180))
            Resolution.blit(text_heroh_good, (hero.x_cordinate, hero.y_cordinate-20))
        if 100>=health_hero>50:
            text_heroh_ok = font.render(str(health_hero), 3, (255, 20, 147))
            Resolution.blit(text_heroh_ok, (hero.x_cordinate, hero.y_cordinate - 20))
        if 50>=health_hero>=0:
            text_heroh_bad = font.render(str(health_hero), 3, (255, 0, 0))
            Resolution.blit(text_heroh_bad, (hero.x_cordinate, hero.y_cordinate - 20))
        hero.movement(Resolution)
        if health1>0:
            enemy1.movement(Resolution)
        if health2>0:
            enemy2.movement(Resolution)
        if healths>0:
            space_ship.movement(Resolution)
        for bullet in bullets:
            bullet.draw(Resolution)
        for bullet in bullets_space:
            bullet.draw(Resolution)
    else:

        # Resolution.blit(gameoverbg, (0, 0))
        game_over_text()
        time.sleep(0.5)
    pygame.display.update()


hero = main.main_character(400, 530, 64, 64)
bullets = []
bullets_space = []
if health1>0:
    enemy1 = enemy.Enemy(40, 530, 64, 64, 750)
if health2>0:
    enemy2 = enemy.Enemy(750, 530, 64, 64, 750)
if healths>0:
    space_ship = space.Enemys(450, 500, 64, 64, 750)
Start = True
shoot_loop = 0
if health1>0:
    shoot_loop_enemies = 0
if health2>0:
    shoot_loop_enemies2 = 0

font = pygame.font.SysFont('comicsans', 30, True)
alive = True

# We are going to add a new page. That is Start Menu which contains Rules,and We need to click Enter to start or QUIT the game by using Cross mark in the Top Tab of the Game Window.
# If we click Enter then the game starts.


while Start:
    controls = pygame.key.get_pressed()
    #Resolution.fill((234, 234, 234))
    Resolution.blit(background, (0, 0))
    font1 = pygame.font.SysFont('comicsans', 80, True)
    text1 = font1.render("Smashing Bob!!", 30, (150, 80, 90))
    Resolution.blit(text1, (270, 0))
    font2 = pygame.font.SysFont('comicsans', 50, True)
    text2 = font2.render("Rules : ", 100, (41, 36, 33))
    Resolution.blit(text2, (10, 60))
    font3 = pygame.font.SysFont('comicsans', 30, True)
    text3 = font3.render("->If you Shoot the enemy, your score will be incremented by 5.", 100, (70, 0, 130))
    Resolution.blit(text3, (10, 100))
    font4 = pygame.font.SysFont('comicsans', 30, True)
    text4 = font4.render("->If you get contact with the enemy or traps, then you are dead!!!", 100, (70, 0, 130))
    Resolution.blit(text4, (10, 130))
    font5 = pygame.font.SysFont('comicsans', 60, True)
    text5 = font5.render("Press ENTER to start the game!!", 1, (0, 255, 255))
    Resolution.blit(text5, (00, 540))
    font6 = pygame.font.SysFont('comicsans', 50, True)
    text6 = font6.render("Level 3", 100, (41, 36, 33))
    Resolution.blit(text6, (150, 60))
    font7 = pygame.font.SysFont('comicsans', 30, True)
    text7 = font7.render("->Enemies will shoot green bullets and if those green balls hit BOB, ",100, (70, 0, 130))
    Resolution.blit(text7, (10, 160))
    font8 = pygame.font.SysFont('comicsans', 30, True)
    text8 = font8.render(
        "then his health will decrease by 2 and that of Enemies will increase",
        100, (70, 0, 130))
    Resolution.blit(text8, (10, 190))
    font9 = pygame.font.SysFont('comicsans', 30, True)
    text9 = font8.render(
        "by 1(each). Your earned score will also decrease by 5.",
        100, (70, 0, 130))
    Resolution.blit(text9, (10, 220))
    font10 = pygame.font.SysFont('comicsans', 30, True)
    text10 = font10.render("->Shooting the space ship will give you 20 points", 100, (70, 0, 130))
    Resolution.blit(text10, (10, 250))
    font11 = pygame.font.SysFont('comicsans', 30, True)
    text11 = font10.render("->The Blue Flower on the left side increases Bob's health", 100, (70, 0, 130))
    Resolution.blit(text11, (10, 280))

    pygame.display.update()
    if controls[pygame.K_RETURN]:
        Start = False
        alive = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
            alive = False
while alive:
    # Setting Frames per second.
    Resolution.blit(background, (0, 0))
    fps.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
    # This Conditions are given so that bullets will fire with some gap similar like Time Delay .
    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0
    if shoot_loop_enemies > 0:
        shoot_loop_enemies += 1
    if shoot_loop_enemies > 2:
        shoot_loop_enemies = 0
    if shoot_loop_enemies2 > 0:
        shoot_loop_enemies2 += 1
    if shoot_loop_enemies2 > 2:
        shoot_loop_enemies2 = 0

    # This for loop is given to make the bullets hit enemies and add score.
    if hero.x_cordinate>70 and hero.x_cordinate<120:
            health_hero+=1
    for bullet in bullets:
        if health1>0:
            if bullet.y_cordinate - bullet.radius < enemy1.box[1] + enemy1.box[3] and bullet.y_cordinate + bullet.radius > \
                    enemy1.box[1]:
                if bullet.x_cordinate + bullet.radius > enemy1.box[0] and bullet.x_cordinate - bullet.radius < enemy1.box[
                    0] + enemy1.box[2]:
                    bullets.pop(bullets.index(bullet))
                    score += 5
                    health1 -= 5
        if health2>0:
            if bullet.y_cordinate - bullet.radius < enemy2.box[1] + enemy2.box[3] and bullet.y_cordinate + bullet.radius > \
                    enemy2.box[1]:
                if bullet.x_cordinate + bullet.radius > enemy2.box[0] and bullet.x_cordinate - bullet.radius < enemy2.box[
                    0] + enemy2.box[2]:
                    bullets.pop(bullets.index(bullet))
                    score += 5
                    health2 -= 5
        if healths>0:
            if bullet.y_cordinate - bullet.radius < space_ship.box[1] + space_ship.box[
                3] and bullet.y_cordinate + bullet.radius > \
                    space_ship.box[1]:
                if bullet.x_cordinate + bullet.radius > space_ship.box[0] and bullet.x_cordinate - bullet.radius < \
                        space_ship.box[
                            0] + space_ship.box[2]:
                    bullets.pop(bullets.index(bullet))
                    score += 10
                    healths -= 10
        if 800 > bullet.x_cordinate > 0:
            bullet.x_cordinate += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

            # Defining Controls  to set the controls.
    # enemies bullets hitting hero
    for bullet in bullets_space:
        if bullet.y_cordinate - bullet.radius < hero.box[1] + hero.box[3] and bullet.y_cordinate + bullet.radius > \
                hero.box[1]:
            if bullet.x_cordinate + bullet.radius > hero.box[0] and bullet.x_cordinate - bullet.radius < hero.box[
                0] + hero.box[2]:
                bullets_space.pop(bullets_space.index(bullet))
                score -= 5
                health_hero -=2
                if health1>0:
                    health1 += 1
                if health2>0:
                    health2 += 1
        if 800 > bullet.x_cordinate > 0:
            bullet.x_cordinate += bullet.speed
        else:
            bullets_space.pop(bullets_space.index(bullet))
    # enemies shooting
    if health1>10:
        if shoot_loop == 0:
            if enemy1.leftside:
                facing = -1
            else:
                facing = 1

            if len(bullets_space) < 5:
                bullets_space.append(
                    Shooting(round(enemy1.x_cordinate + enemy1.width // 2), round(enemy1.y_cordinate + enemy1.height // 2),
                             6,
                             (124, 252, 0), facing))
            shoot_loop_space = 1

    if health2>10:
        if shoot_loop == 0:
            if enemy2.leftside:
                facing = -1
            else:
                facing = 1

            if len(bullets_space) < 5:
                bullets_space.append(
                    Shooting(round(enemy2.x_cordinate + enemy2.width // 2), round(enemy2.y_cordinate + enemy2.height // 2),
                             6,
                             (124, 252, 0), facing))
            shoot_loop_space2 = 1

    controls = pygame.key.get_pressed()
    if controls[pygame.K_SPACE] and shoot_loop == 0:
        bullet_sound = mixer.Sound("level3/laser.wav")
        bullet_sound.play()
        if hero.leftside:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                Shooting(round(hero.x_cordinate + hero.width // 2), round(hero.y_cordinate + hero.height // 2), 6,
                         (255, 0, 0), facing))
        shoot_loop = 1

    # Here we are giving x_coordinate less than or greater than because to set the boundaries,so it won't cross the
    # Game screen.
    if controls[pygame.K_LEFT] and hero.x_cordinate > hero.speed:
        hero.x_cordinate = hero.x_cordinate - hero.speed
        hero.leftside = True
        hero.rightside = False
        hero.still = False

    elif controls[pygame.K_RIGHT] and hero.x_cordinate < 830 - hero.speed - hero.width:
        hero.x_cordinate = hero.x_cordinate + hero.speed
        hero.leftside = False
        hero.rightside = True
        hero.still = False
    else:
        hero.still = True
        hero.movecount = 0
    # These Conditions are given for jumping.
    if not (hero.jumping):
        if controls[pygame.K_UP]:
            hero.jumping = True
            hero.rightside = False
            hero.leftside = False
            hero.movecount = 0
    else:
        if hero.jump >= -10:
            val = 1
            if hero.jump < 0:
                val = -1
            hero.y_cordinate -= (hero.jump ** 2) * 0.5 * val
            hero.jump -= 1
        else:
            hero.jumping = False
            hero.jump = 10

            # These Condtions are given because when Hero touches ENEMY or TRAPS ,the game should be completed.If the hero does any of these condition then Game will be Over.
    if health1>0:
        if hero.box[1] < enemy1.box[1] + enemy1.box[3] and hero.box[1] + hero.box[3] > enemy1.box[1]:
            if hero.box[0] + hero.box[2] > enemy1.box[0] and hero.box[0] < enemy1.box[0] + enemy1.box[2]:
                hero.gameover = True
                alive = False
                time.sleep(0.5)
    if health2>0:
        if hero.box[1] < enemy2.box[1] + enemy2.box[3] and hero.box[1] + hero.box[3] > enemy2.box[1]:
            if hero.box[0] + hero.box[2] > enemy2.box[0] and hero.box[0] < enemy2.box[0] + enemy2.box[2]:
                hero.gameover = True
                alive = False
                time.sleep(0.5)
    if healths>0:
        if hero.box[1] < space_ship.box[1] + space_ship.box[3] and hero.box[1] + hero.box[3] > space_ship.box[1]:
            if hero.box[0] + hero.box[2] > space_ship.box[0] and hero.box[0] < space_ship.box[0] + space_ship.box[2]:
                hero.gameover = True
                alive = False
                time.sleep(0.5)

    if hero.x_cordinate > 176 and hero.x_cordinate < 229:
        explosionSound = mixer.Sound("level3/explosion.wav")
        explosionSound.play()
        if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
            hero.gameover = True
            alive = False

    if hero.x_cordinate > 575 and hero.x_cordinate < 625:
        explosionSound = mixer.Sound("level3/explosion.wav")
        explosionSound.play()
        if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
            hero.gameover = True
            alive = False


    if health_hero<=0:
        hero.gameover = True
        alive = False
    if health1==health2==healths==0:
        hero.gameover = True
    """if scoreCount == 0:
        f = open("level3/scores.txt", "r")
        highscr = f.read()
        f.close()
        f = open("level3/scores.txt", "w")
        if int(highscr) < score:
            f.write(str(score))
            highscore = score
        else:
            f.write(str(highscr))
            highscore = highscore
        f.close()
        # print(score)
        scoreCount = 1"""


    display_window()

pygame.quit()






