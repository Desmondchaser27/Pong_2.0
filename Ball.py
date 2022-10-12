import pygame

class Ball:
    MAX_VEL = 5

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = 20
        self.height = 20
        self.color = pygame.Color(255, 0, 0)
        self.ball = pygame.Surface((self.width, self.height))
        self.ball.fill(self.color)
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def move(self, x, y):
        self.x += self.x_vel
        self.y += self.y_vel
