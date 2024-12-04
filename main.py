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
text_surface = test_font.render('My game', False, 'Black').convert() # can change to rgb tuple :) 
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_surface = pygame.image.load('assets/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300)) # like a surface, but makes placing much easier can be mid or topo left etc. 

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
    pygame.draw.rect(screen, 'Pink', text_rect) # '#c0e8dc' hexadecimal color :) 
    pygame.draw.rect(screen, 'Pink', text_rect, 10) # draw rectangle shape 
    screen.blit(text_surface, text_rect)

    snail_rect.x -= 4 
    if snail_rect.right <= 0: 
        snail_rect.left = 800 
    screen.blit(snail_surface, snail_rect)
    
    #player_rect.left += 1 # dont move surf, move rect that contains surf
    screen.blit(player_surface, player_rect) # placing at rect 
    
    pygame.display.update()
    clock.tick(60) # while True loop <60fps
    