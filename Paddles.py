import Settings, pygame


class Paddle(pygame.Surface):

    def __init__(self, x, y):


        self.width = 30 #* (Settings.ini.WIDTH / 1200)
        self.height = 80
        self.x = x
        self.y = (y - self.height/2)
        self.color = pygame.Color(0, 255, 0)
        super().__init__((self.width, self.height))
        self.fill(self.color)
        self.rect = pygame.Rect(self.x , self.y, self.width, self.height)


    def Move(self, window,up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.y != 0:
            self.y -= 10
        elif keys[down_key] and self.y + self.height <= window.get_height():
            self.y += 10
        self.rect.x, self.rect.y = (self.x, self.y)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)





