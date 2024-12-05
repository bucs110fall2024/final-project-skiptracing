# import pygame 

# # def display_score(start_time, font, screen):
# #     """
# #     Displays the current score onscreen. 
# #     Calculates score based on time elapsed. 

# #     Args:
# #         start_time (int): The starting time of the game in milliseconds. 
# #         font (pygame.font.Font): The font used to create the score text. 
# #         screen (pygame.Surface): The game screen surface where the score will be displayed. 

# #     Returns:
# #         int: The current score based on the elapsed time. 
# #     """
# #     current_time = int(pygame.time.get_ticks()/1000) - start_time # time in ms - start time so time doesn't go forever 
# #     score_surface = font.render(f"Score: {current_time}", False, (64, 64, 64))
# #     score_rect = score_surface.get_rect(center = (400, 50))
# #     screen.blit(score_surface, score_rect)
# #     return current_time 

# # def collision_sprite(player, obstacle_group):
# #     """
# #     Checks for collisions between the player and obstacles. 
# #     If collision is detected, clears all obstacles and returns False. 
# #     Otherwise, returns True. 

# #     Args:
# #         player (pygame.sprit.GroupSingle): The player's sprite group. 
# #         obstacle_group (pygame.sprite.Group): The group of obstacle sprites. 

# #     Returns:
# #         bool: False if a collision is detected, True otherwise. 
# #     """
# #     if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
# #         obstacle_group.empty()
# #         return False 
# #     else: 
# #         return True 