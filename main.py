import pygame, math, Settings, sys, random, Paddles
from Paddles import Paddle
from Ball import Ball

pygame.init()

window = pygame.display.set_mode(Settings.SCREEN, pygame.RESIZABLE)

pygame.display.set_caption('Pong 2.0 Extreme')


paddle_left = Paddle(10, window.get_height() / 2)
paddle_right = Paddle(window.get_width() - 40, window.get_height() /2)
ball = Ball(window.get_height() / 2, window.get_width() / 2)
running = True
color = pygame.Color(0, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(color)
    paddle_left.Move(window,pygame.K_w, pygame.K_s)
    paddle_right.Move(window, pygame.K_UP, pygame.K_DOWN)
    window.blit(paddle_left.paddle, (paddle_left.x, paddle_left.y))
    window.blit(paddle_right.paddle, ((window.get_width() - paddle_right.width) - 10, paddle_right.y))
    window.blit(ball, (ball.x, ball.y))

    ball.move()
    print(ball.x, ball.y)

    pygame.display.flip()

