import pygame
from Games.PlaneGame.main.Plane import *
from Games.PlaneGame.util.Constant import *
import random

# initialize
pygame.init()
pygame.display.set_caption(Constant.Screen_Title)
pygame.display.set_icon(pygame.image.load(Constant.absolutePath + "ufo.png"))
screen = pygame.display.set_mode((Constant.Screen_Width, Constant.Screen_Height))

# set framerate
clock = pygame.time.Clock()
FPS = 120 

# set music
pygame.mixer.music.load(Constant.absolutePath + "bg.wav")
pygame.mixer.music.play(-1)  # -1 表示单曲循环

# background picture
background = pygame.image.load(Constant.absolutePath + "bg.png")

# my Plane picture
myPlane_png = pygame.image.load(Constant.absolutePath + "plane.png")

# enemy Plane picture
enemyPlane_png = pygame.image.load(Constant.absolutePath + "enemy.png")
enemyPlane_png2 = pygame.image.load(Constant.absolutePath + "enemy2.png")

# game over picture
gameover = pygame.image.load(Constant.absolutePath + "gameover.png")

# set myPlane
myPlane = myPlane(400, 400, 15, myPlane_png)

# set enemyPlanes
speed = 3
num = 10
enemyPlanes = []

# create EnemyPlanes
def create():
    for e in range(num):
        type = random.randint(0, 2)
        enemyX = random.randint(0, Constant.Screen_Width - Constant.Plane_Width)
        enemyY = random.randint(0, 200)
        if type == 0:
            e = enemyPlane(enemyX, enemyY, speed, enemyPlane_png)
            enemyPlanes.append(e)
        else:
            e = enemyPlane(enemyX, enemyY, speed, enemyPlane_png2)
            enemyPlanes.append(e)


# draw Background
def drawBg(self, background):
    screen.blit(background, (0, 0))


# draw myPlane
def drawMyPlane(self, myPlane):
    if myPlane.isLive:
        screen.blit(myPlane.image, (myPlane.x, myPlane.y))


# draw enemyPlane
def drawEnemyPlane(self, enemyPlanes):
    for e in enemyPlanes:
        if e.isLive:
            screen.blit(e.image, (e.x, e.y))
            e.move()
            e.fire()


# draw enemyShot
def drawEnemyShot(self, myPlane):
    for e in enemyPlanes:
        for s in e.shots:
            if s.isLive:
                screen.blit(s.image2, (s.x, s.y))
                s.moveDown()
                s.hitHero(myPlane)


# draw myShot
def drawMyPlaneShot(self, myPlane):
    for s in myPlane.shots:
        if s.isLive:
            screen.blit(s.image1, (s.x, s.y))
            s.moveUp()
            s.hitEnemy(enemyPlanes)


def drawGameOver(self):
    screen.blit(gameover, (Constant.Screen_Width / 2 - 100, Constant.Screen_Height / 2 - 21))


# draw Score
def drawScore(self):
    myfont = pygame.font.Font(None, 30)
    white = 255, 255, 255
    text = myfont.render("Score: " + str(Constant.Score), True, white)
    screen.blit(text, (Constant.Screen_Width - 100, 10))


# loop
run = True
while run:
    clock.tick(FPS)

    if len(enemyPlanes) == 0:
        create()
        num += 2

    if myPlane.isLive:
        drawBg(screen, background)
        drawMyPlane(screen, myPlane)
        drawEnemyPlane(screen, enemyPlanes)
        drawMyPlaneShot(screen, myPlane)
        drawEnemyShot(screen, myPlane)

    else:
        drawGameOver(screen)

    drawScore(screen)

    # event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                # set sound
                sound = pygame.mixer.Sound(Constant.absolutePath + "laser.wav")
                sound.play()
                myPlane.fire()

        key = pygame.key.get_pressed()
        # up
        if key[pygame.K_w] and myPlane.y > 0:
            myPlane.moveUp()

        # right
        if key[pygame.K_d] and myPlane.x + Constant.Plane_Width < Constant.Screen_Width:
            myPlane.moveRight()

        # down
        if key[pygame.K_s] and myPlane.y + Constant.Plane_Height < Constant.Screen_Height:
            myPlane.moveDown()

        # left
        if key[pygame.K_a] and myPlane.x > 0:
            myPlane.moveLeft()

    pygame.display.update()

#游戏结束时 写入数据
path = "/Users/myry/Documents/MyPythonProject/Games/PlaneGame/record/scores.txt"
with open(path, 'a') as file:
    # 写入新数据
    file.write(str(Constant.Score) + "\n")
file.close()
