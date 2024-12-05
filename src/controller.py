import pygame 
import sys 
from random import choice 
from src.player import Player 
from src.obstacle import Obstacle 
from src.game import display_score, collision_sprite 
from src.high_score import create_connection, create_table, insert_score, get_high_scores

def main():
    """
    Central  function to run game. 
    Initializes game, sets up game window, loads assets, 
    contains main event handler game loop, updates game state, 
    renders game screen. 
    
    Includes logic for starting game, updating player and obstacle sprites, 
    and checking for collisions. 
    """
    # Initializations 
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Skiptracing')
    icon = pygame.image.load('assets/Player/player_stand.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock() # Clock object for FPS
    test_font = pygame.font.Font('assets/Font/Pixeltype.ttf', 50) 
    game_active = False 
    start_time = 0 
    score = 0
    conn = create_connection()
    create_table(conn) # initialize hi score table 

    # Groups 
    player = pygame.sprite.GroupSingle()
    player.add(Player()) 
    obstacle_group = pygame.sprite.Group()

    # Surfaces 
    sky_surface = pygame.image.load('assets/Backgrounds/sky.png').convert()
    ground_surface = pygame.image.load('assets/Backgrounds/ground.png').convert()

    # Intro Screen 
    player_stand = pygame.image.load('assets/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center = (400, 200))
    game_name = test_font.render('Skiptracing', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center = (400, 80))
    game_message = test_font.render('Press space to run', False, (111, 196, 169))
    game_message_rect = game_message.get_rect(center = (400, 340))

    # Timer 
    obstacle_timer = pygame.USEREVENT + 1 
    pygame.time.set_timer(obstacle_timer, 1500)

    # Game Loop 
    while True: 
    # Handle events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
                
            if game_active == True: 
                # Click to jump 
                if event.type == obstacle_timer: 
                    obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
            else: 
                # check if any button was pressed, work with a specific key 
                # Space to jump 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    
                    # Retrieve high scores 
                    high_scores = get_high_scores(conn)
                
        if game_active == True: 
            # Draw Background 
            screen.blit(sky_surface, (0,0))
            screen.blit(ground_surface, (0,300))
            score = display_score(start_time, test_font, screen)
            player.draw(screen)
            player.update()
            obstacle_group.draw(screen)
            obstacle_group.update()
            game_active = collision_sprite(player, obstacle_group)
            
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
                # save the score 
                if score > 0:
                    insert_score(conn, score)
                
                    # display high scores 
                    screen.blit(score_message, score_message_rect)
                    high_scores = get_high_scores(conn)
                    y_offset = 150
                    for idx, high_score in enumerate(high_scores):
                        score_text = test_font.render(f"Rank {idx+1}: {high_score[0]}", False, (111, 196, 169))
                        score_rect = score_text.get_rect(center = (700, y_offset))
                        screen.blit(score_text, score_rect)
                        y_offset += 45
        
        pygame.display.update()
        clock.tick(60) # 60fps 
        
if __name__=="__main__":
    main()