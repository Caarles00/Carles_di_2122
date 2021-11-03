from posixpath import join
import random
import os
import time
import sqlite3

import random
import os
import time

# Import the pygame module
import pygame
from pygame import font
from pygame import display
from pygame.constants import JOYHATMOTION, K_SPACE, RLEACCEL
from pygame.display import update

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

BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

#Initialize value punts = 0
punts = 0 
level = 1
temps = True
color = BLUE

#Creacio base de datos SQLite
def create_table(con):
    cursor = con.cursor()
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS Max_Score(score INT)")
        cursor.execute("INSERT INTO Max_Score VALUES (0)")

        print("Table Max_Score created")
    except sqlite3.OperationalError:
        print("Max_Score already exists")

def conexion():
    try:
        conexion=sqlite3.connect("bd1.bd")
        create_table(conexion)
        return conexion
    except sqlite3.OperationalError:
        print("Error")

con = conexion()


def update(points):
    cursor = con.cursor()
    cursor.execute("UPDATE Max_Score SET score={}".format(points))
    con.commit()

def read():
    cursor = con.cursor()
    var_cursor = cursor.execute("SELECT score FROM Max_Score").fetchone()
    return var_cursor[0]


#Setupforsounds. Defaultsaregood.
pygame.mixer.init()

#Load all sound files
#Soundsources:Jon Fincher
move_up_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Rising_putter.ogg"))
move_down_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Falling_putter.ogg"))
collision_sound=pygame.mixer.Sound(os.path.join(ruta_a_recurs, "Collision.ogg"))
sonido_disparo = pygame.mixer.music.load(os.path.join(ruta_a_recurs, "disparo.mp3"))


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join(ruta_a_recurs, "jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

        #Vides del personatge
        self.vides = 3

        #Cadencia de dispars
        self.cadencia = 750
        self.ultim_dispar = pygame.time.get_ticks()

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
        if pressed_keys[K_SPACE]:

            ahora = pygame.time.get_ticks()
            if (ahora - self.ultim_dispar > self.cadencia):
                player.shot()
                #sonido_disparo.play()
                self.ultim_dispar = ahora

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
    def shot(self):
        bullet = Shot(self.rect.centerx, self.rect.centery)
        shots.add(bullet)
    
# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(ruta_a_recurs, "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),                    
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2 * level, 10 + 3 * level)
    

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

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Utils/bala.png").convert(), (20, 20)) 
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
    
    def update(self):
        self.rect.x += 20
        if self.rect.bottom < 0:
            self.kill()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#global vel_creacio
#vel_creacio = 100

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

ADDNIGHT = pygame.USEREVENT + 3
pygame.time.set_timer(ADDNIGHT, 15000)


#Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
shots = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True

font_score = pygame.font.SysFont("comicsans", 20, True)
text_intro = pygame.font.SysFont("console", 30, True)
text_result = pygame.font.SysFont("console", 80, True)
estar_en_intro = True

musica_intro = pygame.mixer.music.load(os.path.join(ruta_a_recurs, "intro.ogg"))
pygame.mixer.music.play(loops=-1)

fondo_intro = pygame.image.load(os.path.join(ruta_a_recurs, "jet_intro1.jpg")).convert()
fondo_intro = pygame.transform.scale(fondo_intro,(SCREEN_WIDTH, SCREEN_HEIGHT))

#Pantalla de benvinguda
while(estar_en_intro):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.blit(fondo_intro, (0, 0))
    title = text_result.render("Jet Game", 1, (WHITE))
    record = text_intro.render("Current record: " + str(read()), 1, (WHITE))
    instrucciones = text_intro.render("Press p to play", 1, (GREEN))
    screen.blit(title, (200, 100))
    screen.blit(instrucciones, (250, 550))
    screen.blit(record, (230, 500))

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_p]:
        estar_en_intro = False
    
    pygame.display.update()

#Load and play background music
pygame.mixer.music.stop()
pygame.mixer.music.load(os.path.join(ruta_a_recurs, "Apoxode_-_Electric_1.ogg"))
pygame.mixer.music.play(loops=-1)

vc_temp = 0
# Main loop
while running:
    vc = int(50 + 200//level)
    if vc_temp != vc:
        vc_temp = vc 
        pygame.time.set_timer(ADDENEMY, vc)

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

        elif event.type == ADDNIGHT:
            if(temps == True):
                color = BLUE
                temps = False
            else:
                color = BLACK
                temps = True

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # Update cloud position
    clouds.update()

    # Update cloud position
    shots.update()

    colision = pygame.sprite.groupcollide(enemies, shots, True, False)   

    # Fill the screen with blue
    screen.fill((color))

    #Add 10 points to score when the enemies passes the left edge of the screen
    for i in enemies:
        if i.rect.right < 10:
            punts += 10
            if(punts%500 == 0):
                level += 1

    # Text de puntuacio
    text_score = font_score.render("Score: " + str(punts), True, (RED))
    text_level = font_score.render("Level: " + str(level), True, (RED))
    text_vidas = font_score.render("Lives: " + str(player.vides), True , (RED))

    #Text position
    screen.blit(text_score, (10, 10))
    screen.blit(text_level, (10, 30))
    screen.blit(text_vidas, (10, 50))

    shots.draw(screen)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollide(player, enemies, True):
        # If so, then remove the player and stop the loop
        collision_sound.play()
        player.vides -= 1 

        if player.vides <= 0:
            running = False
            player.kill()                
            print(punts)
            
            pygame.mixer.music.stop()
            musica_final = pygame.mixer.music.load(os.path.join(ruta_a_recurs, "game_over.ogg"))
            pygame.mixer.music.play(loops=-1)
            time.sleep(1)
            pygame.mixer.music.stop()

            #Pantalla final
            final = True
            while final:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    
                    screen.fill((0,0,0))
                    titul = text_result.render("GAME OVER :(", 1, (WHITE))
                    instrucciones = text_intro.render("PRESS ENTER TO QUIT THE GAME...",1 , (RED))
                    pts = text_intro.render("Points achived: " + str(punts), 1, (WHITE))
                    lvl = text_intro.render("Level reached: " + str(level), 1, (WHITE))
                    
                    if punts > read():
                        print("pato")
                        update(punts)
                        text_congrats = text_intro.render("Congrats, new record!", 1, (WHITE))
                        screen.blit(text_congrats, (220, 250))

                    screen.blit(titul, (SCREEN_WIDTH//2-SCREEN_HEIGHT//2, 75))
                    screen.blit(pts, (220, 300))
                    screen.blit(lvl, (220, 350))
                    screen.blit(instrucciones, (120, 500))

                    pygame.display.update()

                    tecla = pygame.key.get_pressed()

                    if tecla[pygame.K_RETURN]:
                        final = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)


# Get the set of keys pressed and check for user input
pressed_keys = pygame.key.get_pressed()

#Alldone!Stopandquitthemixer.
pygame.mixer.quit()