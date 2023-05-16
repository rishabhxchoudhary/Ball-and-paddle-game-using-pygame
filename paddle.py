"""
This file defines the Paddle class, representing a paddle object in the game.

The Paddle class inherits from the Drawable class and adds properties and methods
specific to the paddle object. It handles the drawing and movement of the paddle,
as well as interaction with other objects in the game.
"""
import pygame
from drawable import Drawable


class Paddle(Drawable):
    def __init__(self, width, height, color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height

    def draw(self, surface):
        if self.isVisible():
            pygame.draw.rect(surface, self.__color, self.get_rect())

    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2,  screenHeight - (self.__height), self.__width, self.__height)

    def update_position(self, mouse_x):
        self.position = (mouse_x, self.position[1])

    def setColor(self, color):
        self.__color = color

    def setWidth(self, width):
        self.__width = width
