import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        #TODO:turn the fish in the opposite direction
        self.forward_image = pygame.image.load("Asteroid/assets/sprites/playerShip1_blue.png").convert()
        self.backward_image = pygame.transform.flip(self.forward_image, True, False).convert()
        self.backward_image.set_colorkey((0,0,0))
        self.forward_image.set_colorkey((0, 0, 0))
        self.rect = self.forward_image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0