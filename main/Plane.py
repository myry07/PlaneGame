import pygame
import random
from Games.PlaneGame.main.Shot import *


class Plane():
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.isLive = True
        self.shots = []

    def move(self):
        pass


class myPlane(Plane):
    def moveUp(self):
        self.y -= self.speed

    def moveRight(self):
        self.x += self.speed

    def moveDown(self):
        self.y += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def fire(self):
        s = Shot(self.x + 16, self.y + 16)
        if self.isLive:
            self.shots.append(s)

            if s.y < 0:
                self.shots.isLive = False
                self.shots.remove(s)


class enemyPlane(Plane):
    def move(self):
        num1 = random.randint(Constant.Screen_Width - 70, Constant.Screen_Width)
        num2 = random.randint(0, 70)
        self.x += self.speed
        if self.x + Constant.Plane_Width > num1 or self.x < num2:
            self.speed *= -1

    def fire(self):
        num = random.randint(0, 400)
        s = Shot(self.x + 16, self.y + 16)
        if self.isLive and num == 7:
            self.shots.append(s)
            if s.y < 0:
                self.shots.isLive = False
                self.shots.remove(s)
