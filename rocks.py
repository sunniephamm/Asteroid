import pygame
import random

class Rock(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image  = pygame.image.load("Asteroid/assets/sprites/meteorGrey_big4.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        #update the x position
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

rocks = pygame.sprite.Group()