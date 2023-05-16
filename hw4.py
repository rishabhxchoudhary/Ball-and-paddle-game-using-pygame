"""
This file contains the main game logic and serves as the entry point for the game.

The game uses the Pygame library to create a simple ball and paddle game.
The player controls a paddle at the bottom of the screen and tries to bounce
the ball off the paddle to hit targets. The player earns points for successful hits,
but loses points if the ball hits the bottom. The game ends if the player
reaches the win points or his score is less than 0, and displays appropriate messages.

You will instantly loose if you hit left or right side of the baddle.
"""

import pygame
from ball import Ball
from paddle import Paddle
from text import Text


pygame.init()

X = 800
Y = 600
surface = pygame.display.set_mode((X, Y))

DREXEL_BLUE = (7, 41, 77)  # Initial color of the ball

WHITE = (255, 255, 255)  # Initial color of the background

GREEN = (0, 255, 0)  # Easy level color of the ball
ORANGE = (255, 153, 0)  # Medium level color of the ball
RED = (255, 0, 0)  # Hard level color of the ball


GAMEPOINT = 1000
WINPOINTS = 50
LOSEPOINTS = -100

myBall = Ball(400, 300, 25, DREXEL_BLUE)

PADDLE_WIDTH = 200
myPaddle = Paddle(PADDLE_WIDTH, 25, DREXEL_BLUE)

myScoreBoard = Text("Score: 0", 10, 10)
running = True
fpsClock = pygame.time.Clock()
numHits = 0

# Function to restart the game


def restart_game():
    global numHits
    numHits = 0
    myBall.setX(400)
    myBall.setY(300)
    myBall.setVisible(True)
    myPaddle.setVisible(True)
    myScoreBoard.setMessage("Score: " + str(numHits))


while running:
    surface.fill(WHITE)
    # pygame.draw.rect(surface, (123, 123, 123), myBall.get_rect())
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreBoard.draw(surface)

    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed()*-1)
        numHits += WINPOINTS
        myScoreBoard.setMessage("Score: " + str(numHits))

    if myBall.getLoc()[1]+myBall.getYSpeed()+myBall.getRadius() >= Y:
        numHits += LOSEPOINTS
        myScoreBoard.setMessage("Score: " + str(numHits))

    if numHits >= GAMEPOINT:
        myScoreBoard.setMessage("You Win! Press Enter to restart.")
        myBall.setVisible(False)
        myPaddle.setVisible(False)

    if numHits < 0:
        myScoreBoard.setMessage("You Lose! Press Enter to restart.")
        myBall.setVisible(False)
        myPaddle.setVisible(False)

    if numHits < GAMEPOINT//3:
        myBall.setColor(GREEN)
        myPaddle.setColor(GREEN)
        myPaddle.setWidth(PADDLE_WIDTH)

    elif numHits < 2*GAMEPOINT//3:
        myBall.setColor(ORANGE)
        myPaddle.setColor(ORANGE)
        myPaddle.setWidth(PADDLE_WIDTH//2)

    else:
        myBall.setColor(RED)
        myPaddle.setColor(RED)
        myPaddle.setWidth(PADDLE_WIDTH//3)

    if myBall.isVisible():
        myBall.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not myBall.isVisible() and not myPaddle.isVisible():
                    restart_game()

    pygame.display.update()
    if numHits < GAMEPOINT//3:
        fpsClock.tick(500)
    elif numHits < 2*GAMEPOINT//3:
        fpsClock.tick(1000)
    else:
        fpsClock.tick(3000)
exit()
