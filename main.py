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
            self.gravity = -20

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

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False 
    else: 
        return True 
    
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
# #obstacle_group.update()


# Surfaces 
sky_surface = pygame.image.load('assets/sky.png').convert()
ground_surface = pygame.image.load('assets/ground.png').convert()

# Intro Screen 
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

# snail_animation_timer = pygame.USEREVENT + 2 
# pygame.time.set_timer(snail_animation_timer, 500)

# fly_animation_timer = pygame.USEREVENT + 3 
# pygame.time.set_timer(fly_animation_timer, 200)


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
            if event.type == obstacle_timer: 
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else: 
            # check if any button was pressed, work with a specific key 
            # Space to jump 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
               game_active = True
               start_time = int(pygame.time.get_ticks()/1000)
            
    if game_active == True: 
        # Draw Background 
        screen.blit(sky_surface, (0,0)) # Blot image transfer 
        screen.blit(ground_surface, (0,300))
        score = display_score()
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collision_sprite()
        
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
        