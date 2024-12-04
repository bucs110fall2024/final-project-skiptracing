import pygame 

def display_score(start_time, font, screen):
    current_time = int(pygame.time.get_ticks()/1000) - start_time # time in ms - start time so time doesn't go forever 
    score_surface = font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time 

def collision_sprite(player, obstacle_group):
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False 
    else: 
        return True 