# Import random for random numbers
import random
import os
# Import the pygame module
import pygame
from pygame.constants import RLEACCEL

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

#ruta_base = os.path.dirname(_file_)
#ruta_a_recurs = os.path.join(ruta_base, "DI/Utils")

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
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

    try:
        ruta_base = os.path.dirname(_file_)
        ruta_a_recurs = os.path.join(ruta_base, "jet.png")

        def _init_(self):
            super(Player, self)._init_()
            self.surf = pygame.image.load("jet.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()
    except FileExistsError:
        print("El fitxer no existeix")

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    try:
        ruta_base = os.path.dirname(_file_)
        ruta_a_recurs = os.path.join(ruta_base, "missile.png")
        def _init_(self):
            super(Enemy, self)._init_()
            self.surf = pygame.image.load("missile.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )
            self.speed = random.randint(5, 20)
    except FileExistsError:
        print("El fitxer no existeix")

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    try:
        ruta_base = os.path.dirname(_file_)
        ruta_a_recurs = os.path.join(ruta_base, "cloud.png")

        def _init_(self):
            super(Cloud, self)._init_()
            self.surf = pygame.image.load("cloud.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 50, SCREEN_HEIGHT + 100),
                    random.randint(0, SCREEN_HEIGHT)
                )
            )
    except FileExistsError:
        print("El fitxer no existeix")

    def update(self):
        self.rect.move_ip(-self.speed, 5)

#Setupforsounds. Defaultsaregood.
pygame.mixer.init()

# Initialize pygame
pygame.init()

#Load and play background music
pygame.mixer.music.load("Apoxode_-_Electric_1.ogg")
pygame.mixer.music.play(loops=-1)

#Load all sound files
#Soundsources:Jon Fincher
move_up_sound=pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound=pygame.mixer.Sound("Falling_putter.ogg")
collision_sound=pygame.mixer.Sound("Collision.ogg")

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

#Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

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

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
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