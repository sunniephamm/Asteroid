import pygame
import pygame.mixer
import random
import sys
from rocks import Rock
from game_para import *
from asteroidbackground import *
from players import Player
#initialize pygame
pygame.init()
pygame.mixer.init()
#create the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Asteroid")
pygame.mixer.music.load("../Asteroid/MUSIC/Main Title Theme _ Rebel Blockade Runner.mp3")

pygame.mixer.music.play(-1)

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


#draw the rocks
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
        self.rect.center = (x, y)


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


def show_instructions(screen):
    instruction_font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)

    title_text = title_font.render("Asteroid Game", True, (255, 255, 255))
    screen.blit(title_text, (screen_width / 2 - title_text.get_width() / 2, 50))

    instructions = [
        "Welcome to Asteroids! "
        "Instructions:",
        "Use Arrow Keys to move the player.",
        "Press Spacebar to shoot lasers.",
        "Get points by colliding with the asteroids.",
        "Press Enter to start the game."
    ]

    y_offset = 150
    for text in instructions:
        text_render = instruction_font.render(text, True, (92, 102, 191))
        screen.blit(text_render, (screen_width / 2 - text_render.get_width() / 2, y_offset))
        y_offset += 40

    pygame.display.flip()

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_key = False
show_instructions(screen)
#main loop
running = True
background = screen.copy()
draw_background(background)


#draw the rocks starts from the top and then goes down
for _ in range(5):
    rocks.add(Rock(random.randint(0,760),random.randint(0, 10)))

for rock in rocks:#adding more astroids if they leave the screen
    if rock.rect.y >= rock.rect.height:
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