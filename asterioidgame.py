import pygame
import random
import sys
from rocks import Rock
from game_para import *

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Asteroid")

clock = pygame.time.Clock()
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
        rocks.add(Rock(random.randint(0, screen_width ), 0))


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


#draw the rocks
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


class Laser(pygame.sprite.Sprite):
    speed = -11
    def __init__(self,x,y):
        self.image = pygame.image.load("../Asteroid/assets/sprites/laserBlue13.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vel = [0,0]


    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

lasers = pygame.sprite.Group()

def shoot():
    l = Laser(player.rect.x, player.rect.y)     #Remy helped with shooting
    l.vel = (0, -player.rect.centery)
    mag = (l.vel[0]**2+l.vel[1]**2)**.5
    l.vel = [l.vel[0]/mag*5, l.vel[1]/mag*5]
    lasers.append(l)
#main loop
running = True
background = screen.copy()
draw_background(background)


#draw the rocks starts from the top and then goes down
for _ in range(5):
    rocks.add(Rock(random.randint(0,760),random.randint(0, 10)))

for rock in rocks:#adding more astroids if they leave the screen
    if rock.rect.y < - rock.rect.height:
        add_rocks(5)



#draw the first player
player = Player(screen_width/2, screen_height-100)
lasers = []
#different events that lets us know what key was pressed
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
                player.move_up()
            if event.key == pygame.K_DOWN:
                print("You pressed the key down key")
                player.move_down()
            if event.key == pygame.K_LEFT:
                print("You pressed the left key")
                player.move_left()

            if event.key == pygame.K_RIGHT:
                print("You pressed the key right key")
                player.move_right()

            if event.key == pygame.K_SPACE:
                shoot()
                print("You pressed the space button")


    screen.blit(background,(0,0,))

#updates the player
    player.update()
    rocks.update()
    for laser in lasers:
        laser.update()

#draws the player on the screen
    player.draw(screen)
    rocks.draw(screen)
    for laser in lasers:
        laser.draw(screen)
    pygame.display.flip()



#adding a score
    result = pygame.sprite.spritecollide(player, rocks, True)
    score_font = pygame.font.Font("../Asteroid/font/Black_Crayon.ttf", 60)
    if result:
        score += len(result)
        for _ in range(len(result)):
            add_rocks(1)
            print(result)
    #updates the score on the screen
    text = score_font.render(f"{score}", True, (255, 29, 0))
    screen.blit(text, (screen_width / 2-20,50))


    #flips to show the created game
    pygame.display.flip()
#sets frames
    clock.tick(60)


# create a gameover background
screen.blit(background,(0,0))
#game over message
message = score_font.render("GAME OVER",True, (0,0,0))
screen.blit(message, (screen_width/2-message.get_width()/2,screen_height/2))
screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/3))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()