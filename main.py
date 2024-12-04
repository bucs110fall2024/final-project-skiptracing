import pygame 
import sys 
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
            
        player_walk_1 = pygame.image.load('assets/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0 # pick w1 or w2 
        self.player_jump = pygame.image.load('assets/Player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0 

    def player_input(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300: 
            self.gravity -= 20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 300: 
            self.rect.bottom = 300 


    def animation_state(self):
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        else: 
            self.player_index += .1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0 
            self.image = self.player_walk[int(self.player_index)]
            
    def update(self): 
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_frame_1 = pygame.image.load('assets/Fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('assets/Fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210 
        else: 
            snail_frame_1 = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('assets/Snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300 
        
        self.animation_index = 0 
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0 
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        self.animation_state()
        self.rect.x -= 6 
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time # time in ms - start time so time doesn't go forever 
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time 
    
def obstacle_movement(obstacle_list):
    if obstacle_list: 
        for obstacle_rect in obstacle_list: 
            obstacle_rect.x -= 5 
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []
            
def collisions(player, obstacles): 
    if obstacles: 
        for obstacle_rect in obstacles: 
            if player.colliderect(obstacle_rect):
                return False 
    return True 
                
def player_animation():
    global player_surface, player_index 
    
    if player_rect.bottom < 300: # if the player on ground... illusion player jump 
        player_surface = player_jump 
    else: # on floor 
        player_index += 0.1 # walk lol 
        if player_index >= len(player_walk): # if num too large, set back to 0 
            player_index = 0 
        player_surface = player_walk[int(player_index)]
    # play walking anim if player on floor 
    # display jump surf when player airbond 

# Initialize 
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
icon = pygame.image.load('assets/run.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock() # Clock object for FPS
test_font = pygame.font.Font('assets/Font/Pixeltype.ttf', 50) 
game_active = False 
start_time = 0 
score = 0

# Groups 
player = pygame.sprite.GroupSingle()
player.add(Player()) 
obstacle_group = pygame.sprite.Group()
#obstacle_group.update()


# Surfaces 
sky_surface = pygame.image.load('assets/sky.png').convert()
ground_surface = pygame.image.load('assets/ground.png').convert()

# Obstacles 
snail_frame_1 = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('assets/Snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0 
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('assets/Fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('assets/Fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0 
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load('assets/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('assets/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0 # pick w1 or w2 
player_jump = pygame.image.load('assets/Player/jump.png').convert_alpha()
player_surface = player_walk[player_index] # pick player walk 1 

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
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2 
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3 
pygame.time.set_timer(fly_animation_timer, 200)


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
                start_time = int(pygame.time.get_ticks()/1000)
                
        if game_active: 
            if event.type == obstacle_timer: 
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: 
                    snail_frame_index = 1 
                else: 
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
                
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: 
                    fly_frame_index = 1 
                else: 
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
            
            
    if game_active == True: 
        # Draw Background 
        screen.blit(sky_surface, (0,0)) # Blot image transfer 
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, 'Pink', text_rect) # '#c0e8dc' hexadecimal color :) 
        # pygame.draw.rect(screen, 'Pink', text_rect, 10) # draw rectangle shape 
        # screen.blit(text_surface, text_rect)
        score = display_score()
        

        # # Snail Movement 
        # snail_rect.x -= 4 # move surf that contains rect 
        # if snail_rect.right <= 0: 
        #     snail_rect.left = 800 
        # screen.blit(snail_surface, snail_rect)

        # Player Movement 
        player_gravity += 1
        player_rect.y += player_gravity # gravity! player falls down 
        if player_rect.bottom >= 300: # top of ground, bottom fo player 
            player_rect.bottom = 300 
        player_animation()
        screen.blit(player_surface, player_rect) # placing at rect 
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        
        
        
        # OBbstacle movemnt 
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision 
        game_active = collisions(player_rect, obstacle_rect_list) 
   
    # End Screen 
    else: 
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear() # remove enemies to restart 
        player_rect.midbottom = (80, 300) # reset rect pos 
        player_gravity = 0 # reset grav 
        
        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)
       
        if score == 0: 
            screen.blit(game_message, game_message_rect) 
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60) # while True loop <60fps
        