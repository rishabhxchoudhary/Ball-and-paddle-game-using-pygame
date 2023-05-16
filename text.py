"""
This file defines the Text class, representing a text object in the game.

The Text class inherits from the Drawable class and adds properties and methods
specific to the text object. It handles rendering and displaying text on the game surface.
"""

from drawable import Drawable
import pygame


class Text(Drawable):
    def __init__(self, message="Pygame", x=0, y=0, color=(0, 0, 0), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)

    def draw(self, surface):
        self.__surface = self.__fontObj.render(
            self.__message, True, self.__color)
        surface.blit(self.__surface, self.get_rect())

    def get_rect(self):
        return self.__surface.get_rect()

    def setMessage(self, message):
        self.__message = message
