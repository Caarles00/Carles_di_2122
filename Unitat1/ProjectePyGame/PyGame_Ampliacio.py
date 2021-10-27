# Import random for random numbers
import random
import os
import time

# Import the pygame module
import pygame
from pygame import font
from pygame.constants import RLEACCEL

ruta_base = os.path.dirname(__file__)
ruta_a_recurs = os.path.join(ruta_base, "Utils")

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join(ruta_a_recurs, "jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(ruta_a_recurs, "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),                    random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
    

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(ruta_a_recurs, "cloud.png")).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)            
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )            
        )
    

    def update(self):
        self.rect.move_ip(-5 ,0)
        if self.rect.right < 0:
            self.kill()

#Setupforsounds. Defaultsaregood.
pygame.mixer.init()

# Initialize pygame
pygame.init()

#Load and play background music
pygame.mixer.music.load(os.path.join(ruta_a_recurs, "Apoxode_-_Electric_1.ogg"))
pygame.mixer.music.play(loops=-1)

#Load all sound files
#Soundsources:Jon Fincher
move_up_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Rising_putter.ogg"))
move_down_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Falling_putter.ogg"))
collision_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Collision.ogg"))


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

#Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

#Initialize value punts = 0
punts = 0 
level = 1

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Update cloud position
    clouds.update()

    # Fill the screen with blue
    screen.fill((135, 206, 250))

    #Add 20 points to score when the enemies passes the left edge of the screen
    for i in enemies:
        if i.rect.right < 10:
            punts += 10
            if(punts%500 == 0):
                level += 1
                #for j in range(level):
                ADDENEMY = pygame.USEREVENT + 1 * level
                pygame.time.set_timer(ADDENEMY, 250 * level)

    # Text de puntuacio
    font_score = pygame.font.SysFont("Courier", 15)
    text_score = font_score.render("Score: ", True, (255, 255, 255))#White color
    text_level = font_score.render("Level: ", True, (255, 255, 255))#White color
    num_score = font_score.render(str(punts), True, (255, 255, 255))
    num_level = font_score.render(str(level), True, (255, 255, 255))

    #Show text 
    print(font_score)
    print(text_score)
    print(num_score)
    print(text_level)
    print(num_level)

    #Text position
    screen.blit(text_score, (10, 10))
    screen.blit(num_score, (70, 10))
    screen.blit(text_level, (10, 30))
    screen.blit(num_level, (70, 30))


    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        collision_sound.play()
        time.sleep(1)
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Get the set of keys pressed and check for user input
pressed_keys = pygame.key.get_pressed()

#Alldone!Stopandquitthemixer.
pygame.mixer.music.stop()
pygame.mixer.quit()