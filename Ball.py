import pygame


class Ball(pygame.Surface):

    MAX_VEL = 5

    def __init__(self, x, y):

        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = 20
        self.height = 20
        self.color = pygame.Color(255, 0, 0)
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        super().__init__((self.width, self.height))
        self.fill(self.color)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self, window):
        window.blit(self, (window.get_width() / 2, window.get_height() / 2))
