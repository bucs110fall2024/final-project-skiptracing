import pygame 
import sys 

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time # time in ms - start time so time doesn't go forever 
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time 
    
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
game_active = False 
start_time = 0 
score = 0

# Create surfaces 
sky_surface = pygame.image.load('assets/sky.png').convert()
ground_surface = pygame.image.load('assets/ground.png').convert()
# text_surface = test_font.render('My game', False, 'Black').convert() # can change to rgb tuple :) 
# text_rect = text_surface.get_rect(center = (400, 50))


snail_surface = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_surface = pygame.image.load('assets/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300)) # like a surface, but makes placing much easier can be mid or topo left etc. 
player_gravity = 0 
player_stand = pygame.image.load('assets/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runnner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 340))

# Timer 
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer, 900)


while True: 
    # Entire game runs 
    # Draw all elements 
    # update everything 
    # Event Loop (look at all player input)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
            
        if game_active == True: 
            # Click to jump 
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity -= 20
                
            # check if any button was pressed, work with a specific key 
            # Space to jump 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20 
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
                
        if event.type == obstacle_timer and game_active: 
            print('test')
            

    if game_active == True: 
        # Draw Background 
        screen.blit(sky_surface, (0,0)) # Blot image transfer 
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, 'Pink', text_rect) # '#c0e8dc' hexadecimal color :) 
        # pygame.draw.rect(screen, 'Pink', text_rect, 10) # draw rectangle shape 
        # screen.blit(text_surface, text_rect)
        score = display_score()
        

        # Snail Movement 
        snail_rect.x -= 4 # move surf that contains rect 
        if snail_rect.right <= 0: 
            snail_rect.left = 800 
        screen.blit(snail_surface, snail_rect)

        # Player Movement 
        player_gravity += 1
        player_rect.y += player_gravity # gravity! player falls down 
        if player_rect.bottom >= 300: # top of ground, bottom fo player 
            player_rect.bottom = 300 
        screen.blit(player_surface, player_rect) # placing at rect 
        
        # Collision End 
        if snail_rect.colliderect(player_rect):
            game_active = False # KEYYYY. 

    # End Screen 
    else: 
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        
        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)
       
        if score == 0: 
            screen.blit(game_message, game_message_rect) 
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60) # while True loop <60fps
        