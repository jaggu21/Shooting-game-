import time
import os
import enemy
import main
import pygame
from pygame import mixer

pygame.init()

# Setting a logo for the game.
logo = pygame.image.load(os.path.join('level1', 'L1.png'))
pygame.display.set_icon(logo)

# Setting Resolution of the screen of the game to be Displayed.
Resolution = pygame.display.set_mode((800, 600))

# Setting the Name for the Game.
pygame.display.set_caption("Super Bob")

# Adding a Background for the game.
background = pygame.image.load(os.path.join('level1', "bg.png"))

# Dispalying the gameover background.
gameoverbg = pygame.image.load(os.path.join('level1', 'over.jpg'))

# Displays Trap in the Screen.
Trap = pygame.image.load(os.path.join('level1', 'pipe.png'))

# sound
mixer.music.load(os.path.join('level1', "background.wav"))
mixer.music.play(-1)

fps = pygame.time.Clock()

score = 0

# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)
"""highscore = 0
f = open(r"level1/scores.txt", "r")
highscr = f.read()
f.close()"""

#highscore = int(highscr)


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





def game_over_text():
    scoreCount = 0
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    score_value = over_font.render("Score: " + str(score), True, (255, 255, 255))
    #highscore_value = over_font.render("Score: " + str(highscore), True, (255, 255, 255))
    Resolution.blit(over_text, (200, 100))
    Resolution.blit(score_value, (200, 300))
    #Resolution.blit(highscore_value, (200, 200))

    """if scoreCount == 0:
        f = open(r"level1/scores.txt", "r")
        highscr = f.read()
        f.close()
        f = open(r"level1/scores.txt", "w")
        if int(highscr) < score:
            f.write(str(score))
            highscore = score
        else:
            f.write(str(highscr))
            highscore = highscore
        f.close()
        # print(score)
        scoreCount = 1
    time.sleep(0.5)"""

# We defined a function display_window because this function conatains all the content to Display.Other than this function any other classes or functions just do Internal part of the game.
# But this displpay_window funtion show what we want to show and we need  to call this funtion at last after the mainLoop.
def display_window():
    if hero.gameover == False:
        Resolution.blit(Trap, (200, 550))
        Resolution.blit(Trap, (550, 550))
        text = font.render('Score: ' + str(score), 1, (0, 0, 0))
        Resolution.blit(text, (680, 10))
       # hs = font.render('HighScore: ' + str(highscore), 1, (0, 0, 0))
        #Resolution.blit(hs, (630, 30))
        hero.movement(Resolution)
        enemy1.movement(Resolution)
        for bullet in bullets:
            bullet.draw(Resolution)
    else:
        # Resolution.blit(gameoverbg, (0, 0))
        game_over_text()
        time.sleep(0.5)
    pygame.display.update()

hero = main.main_character(400, 530, 64, 64)
bullets = []
enemy1 = enemy.Enemy(40, 530, 64, 64, 750)
Start = True
shoot_loop = 0
font = pygame.font.SysFont('comicsans', 30, True)
alive = True

# We are going to add a new page. That is Start Menu which contains Rules,and We need to click Enter to start or QUIT the game by using Cross mark in the Top Tab of the Game Window.
# If we click Enter then the game starts.

while Start:
    controls = pygame.key.get_pressed()
    Resolution.fill((234, 234, 234))
    font1 = pygame.font.SysFont('comicsans', 80, True)
    text1 = font1.render("Smashing Bob!!", 30, (150, 80, 90))
    Resolution.blit(text1, (270, 0))

    font2 = pygame.font.SysFont('comicsans', 50, True)
    text2 = font2.render("Rules :For level1 and level2 ", 30, (0, 0, 0))
    Resolution.blit(text2, (10, 60))

    font3 = pygame.font.SysFont('comicsans', 30, True)
    text3 = font3.render("-->If you Shoot the enemy, your score will be incremented by 5", 100, (0, 0, 0))
    Resolution.blit(text3, (10, 100))

    font4 = pygame.font.SysFont('comicsans', 30, True)
    text4 = font4.render("-->If you get contact with the enemy or traps, then you are dead!", 100, (0, 0, 0))
    Resolution.blit(text4, (10, 130))

    font5 = pygame.font.SysFont('comicsans', 50, True)
    text5 = font5.render("Rules for level3:", 1, (0, 0, 0))
    Resolution.blit(text5, (00, 200))

    font6 = pygame.font.SysFont('comicsans', 30, True)
    text6 = font6.render("->Enemies will shoot green bullets and if those green balls hit BOB", 1, (0, 0, 0))
    Resolution.blit(text6, (10, 230))

    font7 = pygame.font.SysFont('comicsans', 30, True)
    text7 = font7.render("then his health will decrease by 2 and that of Enemies will increase", 1, (0, 0, 0))
    Resolution.blit(text7, (10, 260))

    font8 = pygame.font.SysFont('comicsans', 30, True)
    text8 = font8.render("->by 1(each). Your earned score will also decrease by 5.", 1, (0, 0, 0))
    Resolution.blit(text8, (10, 290))

    font9 = pygame.font.SysFont('comicsans', 30, True)
    text9 = font9.render("->Shooting the space ship will give you 20 points", 1, (0, 0, 0))
    Resolution.blit(text9, (10, 320))

    font10 = pygame.font.SysFont('comicsans', 30, True)
    text10 = font10.render("->The Blue Flower on the left side increases Bob's health", 1, (0, 0, 0))
    Resolution.blit(text10, (10, 350))

    font11 = pygame.font.SysFont('comicsans', 30, True)
    text11 = font11.render("Press 's' to start the game!", 1, (0, 255, 255))
    Resolution.blit(text11, (00, 540))

    pygame.display.update()

    if controls[pygame.K_s]:
        Start = False
        alive = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
            alive = False
while alive:
    if (score < 100):
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

        # This for loop is given to make the bullets hit enemies and add score.
        for bullet in bullets:
            if bullet.y_cordinate - bullet.radius < enemy1.box[1] + enemy1.box[
                3] and bullet.y_cordinate + bullet.radius > \
                    enemy1.box[1]:
                if bullet.x_cordinate + bullet.radius > enemy1.box[0] and bullet.x_cordinate - bullet.radius < \
                        enemy1.box[
                            0] + enemy1.box[2]:
                    bullets.pop(bullets.index(bullet))
                    score += 5
            if bullet.x_cordinate < 800 and bullet.x_cordinate > 0:
                bullet.x_cordinate += bullet.speed
            else:
                bullets.pop(bullets.index(bullet))
                # Defining Controls  to set the controls.

        controls = pygame.key.get_pressed()

        if controls[pygame.K_SPACE] and shoot_loop == 0:
            bullet_sound = mixer.Sound("level1/laser.wav")
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

        # Here we are giving x_cordinate less than or greater than beacuase to set the boundaries,so it won't cross the Game screen.
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
        if hero.box[1] < enemy1.box[1] + enemy1.box[3] and hero.box[1] + hero.box[3] > enemy1.box[1]:
            if hero.box[0] + hero.box[2] > enemy1.box[0] and hero.box[0] < enemy1.box[0] + enemy1.box[2]:
                hero.gameover = True
                alive = False
                time.sleep(0.5)

        if hero.x_cordinate > 176 and hero.x_cordinate < 229:
            explosionSound = mixer.Sound("level1/explosion.wav")
            explosionSound.play()
            if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
                hero.gameover = True
                alive = False

        if hero.x_cordinate > 526 and hero.x_cordinate < 579:
            explosionSound = mixer.Sound("level1/explosion.wav")
            explosionSound.play()
            if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
                hero.gameover = True
                alive = False

        display_window()
    else:
        def display_window():
            if hero.gameover == False:
                Resolution.blit(Trap, (50, 550))
                Resolution.blit(Trap, (280, 550))
                Resolution.blit(Trap, (700, 550))
                text = font.render('Score: ' + str(score), 1, (0, 0, 0))
                Resolution.blit(text, (680, 10))
                hero.movement(Resolution)
                enemy1.movement(Resolution)
                enemy2.movement(Resolution)
                for bullet in bullets:
                    bullet.draw(Resolution)
            else:
                # Resolution.blit(gameoverbg, (0, 0))
                game_over_text()
                time.sleep(0.5)
            pygame.display.update()


        hero = main.main_character(400, 530, 64, 64)
        bullets = []
        enemy1 = enemy.Enemy(40, 530, 64, 64, 750)
        enemy2 = enemy.Enemy(100, 530, 64, 64, 750)
        Start = True
        shoot_loop = 0
        font = pygame.font.SysFont('comicsans', 30, True)
        alive = True
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

            # This for loop is given to make the bullets hit enemies and add score.
            for bullet in bullets:
                if (bullet.y_cordinate - bullet.radius < enemy1.box[1] + enemy1.box[
                    3] and bullet.y_cordinate + bullet.radius > \
                        enemy1.box[1]):
                    if (bullet.x_cordinate + bullet.radius > enemy1.box[0] and bullet.x_cordinate - bullet.radius <
                            enemy1.box[
                                0] + enemy1.box[2]):
                        bullets.pop(bullets.index(bullet))
                        score += 5
                if (bullet.y_cordinate - bullet.radius < enemy2.box[1] + enemy2.box[
                    3] and bullet.y_cordinate + bullet.radius > \
                        enemy2.box[1]):
                    if (bullet.x_cordinate + bullet.radius > enemy2.box[0] and bullet.x_cordinate - bullet.radius <
                            enemy2.box[
                                0] + enemy2.box[2]):
                        bullets.pop(bullets.index(bullet))
                        score += 5
                if bullet.x_cordinate < 800 and bullet.x_cordinate > 0:
                    bullet.x_cordinate += bullet.speed
                else:
                    bullets.pop(bullets.index(bullet))
                    # Defining Controls  to set the controls.

            controls = pygame.key.get_pressed()

            if controls[pygame.K_SPACE] and shoot_loop == 0:
                bullet_sound = mixer.Sound("level1/laser.wav")
                bullet_sound.play()
                if hero.leftside:
                    facing = -1
                else:
                    facing = 1

                if len(bullets) < 5:
                    bullets.append(
                        Shooting(round(hero.x_cordinate + hero.width // 2), round(hero.y_cordinate + hero.height // 2),
                                 6,
                                 (255, 0, 0), facing))
                shoot_loop = 1

            # Here we are giving x_cordinate less than or greater than beacuase to set the boundaries,so it won't cross the Game screen.
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
            if hero.box[1] < enemy1.box[1] + enemy1.box[3] and hero.box[1] + hero.box[3] > enemy1.box[1]:
                if hero.box[0] + hero.box[2] > enemy1.box[0] and hero.box[0] < enemy1.box[0] + enemy1.box[2]:
                    hero.gameover = True
                    alive = False
                    time.sleep(0.5)
            if hero.box[1] < enemy2.box[1] + enemy2.box[3] and hero.box[1] + hero.box[3] > enemy2.box[1]:
                if hero.box[0] + hero.box[2] > enemy2.box[0] and hero.box[0] < enemy2.box[0] + enemy2.box[2]:
                    hero.gameover = True
                    alive = False
                    time.sleep(0.5)

            if hero.x_cordinate > 26 and hero.x_cordinate < 79:
                explosionSound = mixer.Sound("level1/explosion.wav")
                explosionSound.play()
                if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
                    hero.gameover = True
                    alive = False

            if hero.x_cordinate > 254 and hero.x_cordinate < 309:
                explosionSound = mixer.Sound("level1/explosion.wav")
                explosionSound.play()
                if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
                    hero.gameover = True
                    alive = False
            if hero.x_cordinate > 676 and hero.x_cordinate < 729:
                explosionSound = mixer.Sound("level1/explosion.wav")
                explosionSound.play()
                if hero.y_cordinate >= 502 and hero.y_cordinate <= 600:
                    hero.gameover = True
                    alive = False

            display_window()

pygame.quit()
