import pygame 
import sys 

# Initialize pygame and variables 
pygame.init()
screenWidth = 800 
screenHeight = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Runner')
icon = pygame.image.load('assets/run.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock() # Clock object for FPS
test_font = pygame.font.Font('assets/Font/Pixeltype.ttf', 50) 

# Create surfaces 
sky_surface = pygame.image.load('assets/sky.png').convert()
ground_surface = pygame.image.load('assets/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black').convert()
snail_surface = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
snail_x_pos = 600 
player_surface = pygame.image.load('assets/Player/player_walk_1.png')

while True: 
    # Entire game runs 
    # Draw all elements 
    # update everything 
    # Event Loop (look at all player input)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

    screen.blit(sky_surface, (0,0)) # Blot image transfer 
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    snail_x_pos -= 4 # move snail 
    if snail_x_pos <= -100: 
        snail_x_pos = 800 # reset snail to right 
    screen.blit(snail_surface, (snail_x_pos, 250))
    
    pygame.display.update()
    clock.tick(60) # while True loop <60fps
    