import pygame 
from random import choice 
from src.player import Player 
from src.obstacle import Obstacle 
from src.high_score import HighScore 

class Controller():
    def __init__(self):
        """
        Initializes the game by setting up the display, 
        loading assets, and creating game objects. 
        """ 
        # Initializations 
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Skiptracing')
        icon = pygame.image.load('assets/Player/player_stand.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock() # Clock object for FPS
        self.test_font = pygame.font.Font('assets/Font/Pixeltype.ttf', 50) 
        self.game_active = False 
        self.start_time = 0 
        self.score = 0
        self.high_score_manager = HighScore()

        # Groups 
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player()) 
        self.obstacle_group = pygame.sprite.Group()

        # Surfaces 
        self.sky_surface = pygame.image.load('assets/Backgrounds/sky.png').convert()
        self.ground_surface = pygame.image.load('assets/Backgrounds/ground.png').convert()

        # Intro Screen 
        self.player_stand = pygame.image.load('assets/Player/player_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center = (400, 200))
        self.game_name = self.test_font.render('Skiptracing', False, (111, 196, 169))
        self.game_name_rect = self.game_name.get_rect(center = (400, 80))
        self.game_message = self.test_font.render('Press space to run', False, (111, 196, 169))
        self.game_message_rect = self.game_message.get_rect(center = (400, 340))

        # Obstacle Timer 
        self.obstacle_timer = pygame.USEREVENT + 1 
        pygame.time.set_timer(self.obstacle_timer, 1500)

    
    def display_score(self):
        """
        Displays the current score onscreen. 
        Calculates score based on time elapsed. 

        Returns:
            int: The current score based on the elapsed time. 
        """
        current_time = int(pygame.time.get_ticks()/1000) - self.start_time # time in ms - start time so time doesn't go forever 
        score_surface = self.test_font.render(f"Score: {current_time}", False, (64, 64, 64))
        score_rect = score_surface.get_rect(center = (400, 50))
        self.screen.blit(score_surface, score_rect)
        return current_time 

    def collision_sprite(self):
        """
        Checks for collisions between the player and obstacles. 

        Returns:
            bool: False if a collision is detected, True otherwise. 
        """
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            return False 
        else: 
            return True 


    def gameLoop(self):
        """
        Main game loop. Handles events, updates game state, 
        Renders the game screen. 
        """
        while True: 
            for event in pygame.event.get():
                # Quit 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 
                    
                # Spawn obstacles, start game on space key if inactive 
                if self.game_active == True: 
                    if event.type == self.obstacle_timer: 
                        self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
                else: 
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                        self.game_active = True
                        self.start_time = int(pygame.time.get_ticks()/1000)
             
            # Draw Background         
            if self.game_active == True: 
                self.screen.blit(self.sky_surface, (0,0))
                self.screen.blit(self.ground_surface, (0,300))
                self.score = self.display_score()
                self.player.draw(self.screen)
                self.player.update()
                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()
                self.game_active = self.collision_sprite()
                
            # End Screen
            else: 
                self.screen.fill((94,129,162))
                self.screen.blit(self.player_stand, self.player_stand_rect)
                score_message = self.test_font.render(f"Your score: {self.score}", False, (111, 196, 169))
                score_message_rect = score_message.get_rect(center = (400, 330))
                self.screen.blit(self.game_name, self.game_name_rect)
                
                # Scoring 
                if self.score == 0: 
                    self.screen.blit(self.game_message, self.game_message_rect) 
                else:
                    # Save score 
                    if self.score > 0:
                        self.high_score_manager.insert_score(self.score)
                    
                        # Display high scores 
                        self.screen.blit(score_message, score_message_rect)
                        high_scores = self.high_score_manager.get_high_scores()
                        y_offset = 150
                        for idx, high_score in enumerate(high_scores):
                            score_text = self.test_font.render(f"Rank {idx+1}: {high_score[0]}", False, (111, 196, 169))
                            score_rect = score_text.get_rect(center = (700, y_offset))
                            self.screen.blit(score_text, score_rect)
                            y_offset += 45
                        
                        # Display retry message 
                        retry_message = self.test_font.render("Press space!", False, (111, 186, 160))
                        retry_message_rect = retry_message.get_rect(center = (150, 200))
                        self.screen.blit(retry_message, retry_message_rect)
        
            pygame.display.update()
            self.clock.tick(60)
            
if __name__ == "__main__": 
    controller = Controller()
    controller.gameLoop()