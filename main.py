import pygame, math, Settings, sys, random, Paddles
from Paddles import Paddle
from Ball import Ball
import Helpers.FileReader as FileReader

pygame.init()

# Grab settings from Settings.ini before executing anything #
settings_imported = FileReader.read_settings_file("Settings.ini")
Settings.import_settings(settings_imported)

window = pygame.display.set_mode(Settings.SCREEN, pygame.RESIZABLE)

pygame.display.set_caption('Pong 2.0 Extreme')

clock = pygame.time.Clock()


paddle_left = Paddle(10, window.get_height() / 2)
paddle_right = Paddle(window.get_width() - 40, window.get_height() /2)
ball = Ball(window.get_width() / 2, window.get_height() / 2)
running = True
color = pygame.Color(0, 0, 0)

while running:
    # Wait for one full frame at framerate (also grab delta time -- time since last frame passed) #
    delta_time: float = clock.tick(Settings.FPS)

    # Handle Pygame Events #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            Settings.SCREEN = event.size
            Settings.WIDTH, Settings.HEIGHT = event.size
            paddle_left.x = 10
            paddle_left.y = window.get_height() / 2
            paddle_right.x = window.get_width() - 40
            paddle_right.y = window.get_height() /2
    # Handle Input From Players #


    # Handle Collision #

    #if balls right side is greater than or = right paddles left side balls direction needs to reverse
    if ball.x + ball.get_width() >= paddle_right.x or\
        ball.x <= paddle_left.x + paddle_left.get_width() and\
        ball.y <= paddle_left.y + paddle_left.get_height() and\
        ball.y >= paddle_left.y:
            ball.x_vel *= -1


    if ball.y <= 0 or ball.y + ball.get_height() >= Settings.HEIGHT:
        ball.y_vel *= -1

    print(paddle_right.get_bounding_rect().x)
    #if ball.x <= 0:
    #    ball reset
    #if ball.x + ball.get_width() >= Settings.WIDTH:
    #    ball reset
    #if balls left side is less than or equal to left paddles right side balls direction needs to reverse

    # Update Game Objects (move, collide, etc.) #
    paddle_left.Move(window,pygame.K_w, pygame.K_s)
    paddle_right.Move(window, pygame.K_UP, pygame.K_DOWN)
    ball.move()

    # Handle Drawing Window #
    window.fill(color)
    window.blit(paddle_left, (paddle_left.x, paddle_left.y))
    window.blit(paddle_right, ((window.get_width() - paddle_right.width) - 10, paddle_right.y))
    window.blit(ball, (ball.x, ball.y))

    # Fully update screen with changes #
    pygame.display.flip()

