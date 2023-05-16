"""
ball.py
This file defines the Ball class, representing a ball object in the game.

The Ball class inherits from the Drawable class and adds properties and methods
specific to the ball object. It handles the movement of the ball, collision detection,
and interaction with other objects in the game.

"""

import pygame
from drawable import Drawable
import math


class Ball(Drawable):
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 1
        self.__ySpeed = 1

    def isvisible(self):
        return self.__visible

    def setColor(self, color):
        self.__color = color

    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color,
                               self.getLoc(), self.__radius)

    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)

    def move(self):
        currentX, currentY = self.getLoc()
        newY = currentY + self.__ySpeed
        newX = currentX + self.__xSpeed
        self.setX(newX)
        self.setY(newY)
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1
        if newY <= self.__radius or newY + self.__radius >= height:
            self.__ySpeed *= -1

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def isTouchingBall(self, other):
        distance = math.sqrt((self.getX() - other.getX())
                             ** 2 + (self.getY() - other.getY())**2)
        return distance <= self.getRadius() + other.getRadius()

    def setXSpeed(self, speed):
        self.__xSpeed = speed

    def getXSpeed(self):
        return self.__xSpeed

    def setYSpeed(self, speed):
        self.__ySpeed = speed

    def getYSpeed(self):
        return self.__ySpeed
