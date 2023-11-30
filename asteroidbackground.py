import pygame
import random
from game_para import*
def draw_background(screen):
    star = pygame.image.load("../Asteroid/assets/sprites/star1.png").convert()
    star.set_colorkey((0,0,0))
    space = pygame.image.load("../Asteroid/assets/sprites/darkPurple.png").convert()
    space.set_colorkey((0,0,0))
    planet = pygame.image.load("../Asteroid/assets/sprites/planet03.png").convert()
    planet.set_colorkey((0,0,0))

    #make space
    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_width, tile_size):
            screen.blit(space,(x,y))

    #make stars
    for _ in range(16):
        x = random.randint(0, screen_width)
        y = random.randint(0,screen_height)
        screen.blit(star, (x,y))
    #draw the planet
    planet= pygame.image.load("../Asteroid/assets/sprites/planet03.png").convert()
    planet.set_colorkey((0,0,0))
    screen.blit(planet,(screen_width-tile_size+70,0))

def add_rocks(num_rocks):
    for _ in range(num_rocks):
        rocks.add(Rock(random.randint(screen_width, screen_width * 2), random.randint(0, screen_height - tile_size)))


class Rock(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image  = pygame.image.load("../Asteroid/assets/sprites/meteorGrey_big4.png").convert()
        self.image.set_colorkey((0,0,0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):       #BRODY HELPED MOVE MY ASTEROIDS
        #update the x position
        #self.x -= self.speed
        #self.rect.x = self.x
        self.y += self.speed
        self.rect.y += self.speed


    def draw(self, screen):
        screen.blit(self.image, self.rect)

rocks = pygame.sprite.Group()