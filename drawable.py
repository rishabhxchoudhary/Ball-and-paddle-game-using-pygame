"""
This file defines the Drawable class, serving as a base class for drawable objects in the game.

The Drawable class is an abstract base class that provides a common interface and
basic functionality for objects that can be drawn on the game surface.
Other drawable objects in the game, such as Ball and Paddle, inherit from this class
and implement their specific drawing and interaction logic.
"""

import pygame
from abc import ABC, abstractmethod


class Drawable(ABC):
    def __init__(self, x, y):
        self.position = (x, y)
        self.__visible = True
        self.__x = x
        self.__y = y

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def get_rect(self):
        pass

    def getLoc(self):
        return (self.__x, self.__y)

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def isVisible(self):
        return self.__visible

    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False

    def setLoc(self, newLoc):
        self.__x, self.__y = newLoc

    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
            return True
        return False
