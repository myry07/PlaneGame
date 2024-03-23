import pygame
from Games.PlaneGame.util.Constant import *

class Shot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.image1 = pygame.image.load(Constant.absolutePath + "shot.png")
        self.image2 = pygame.image.load(Constant.absolutePath + "enemyShot.png")
        self.isLive = True

    def moveUp(self):
        if self.y > 0:
            self.y -= self.speed
        else:
            self.isLive = False

        print(self.y)

    def moveDown(self):
        if self.y + Constant.Shot_Height < Constant.Screen_Height:
            self.y += self.speed
        else:
            self.isLive = False

        print(self.y)

    def hitEnemy(self, enemyPlanes):
        for e in enemyPlanes:
            if self.x + Constant.Shot_Width >= e.x and self.x <= e.x + Constant.Plane_Width and self.y <= e.y + Constant.Plane_Height and self.y >= e.y and e.isLive:

                # set sound
                sound = pygame.mixer.Sound(Constant.absolutePath + "exp.wav")
                sound.play()

                Constant.Score += 1

                e.isLive = False
                enemyPlanes.remove(e)
                self.isLive = False

    def hitHero(self, myPlane):
        if self.x + Constant.Shot_Width >= myPlane.x and self.x <= myPlane.x + Constant.Plane_Width and self.y <= myPlane.y + Constant.Plane_Height and self.y >= myPlane.y and myPlane.isLive:
            # set sound
            sound = pygame.mixer.Sound(Constant.absolutePath + "exp.wav")
            sound.play()

            myPlane.isLive = False
            self.isLive = False
