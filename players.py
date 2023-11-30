import pygame
from game_para import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.forward_image = pygame.image.load("../Asteroid/assets/sprites/playerShip1_blue.png").convert()
        self.backward_image = pygame.transform.flip(self.forward_image, True, False).convert()
        self.backward_image.set_colorkey((0,0,0))
        self.forward_image.set_colorkey((0, 0, 0))
        self.rect = self.forward_image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1*PLAYER_SPEED

    def move_down(self):
        self.y_speed = 1*PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.y_speed = 0
        self.x_speed = 0

    def update(self):
        #to check if player went off the screen
        #update the x position
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x > screen_width-50:
            self.x_speed = 0
        if self.rect.x < 0:
            self.x_speed = 0
        if self.rect.y > screen_height-100:
            self.y_speed = 0
        if self.rect.y < 0:
            self.y_speed = 0

    def draw(self, screen):
        screen.blit(self.forward_image, self.rect)
