import pygame 
from random import randint
  
class Obstacle(pygame.sprite.Sprite):
    """
    A class to represent obstacles/enemies ingame. 
    """
    def __init__(self, type):
        """
        Initializes the obstacle object, loading images for different obstacles (fly/snail), 
        setting the initial image and rect for positioning, and initializing the animation index. 

        Args:
            type (str):The type of obstacle ('fly' or 'snail')
        """
        super().__init__()
        
        if type == 'fly':
            # Load fly animation frames  
            fly_frame_1 = pygame.image.load('assets/Fly/fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('assets/Fly/fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210 # flies should be flying lol 
        else: 
            # Load snail animation frames 
            snail_frame_1 = pygame.image.load('assets/Snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('assets/Snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300 # on ground 
        
        self.animation_index = 0 
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))
        
    def animation_state(self):
        """
        Updates the obstacle's animation state. 
        Advances animation frame of obstacle, cycling thru available frames to animate! 
        """
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0 
        self.image = self.frames[int(self.animation_index)]
        
    def update(self):
        """
        Update the obstacle's state. 
        Updates animation state, moves obstacle left, checks if obstacle should be destryed (removed from screen)
        """
        self.animation_state()
        self.rect.x -= 6 
        self.destroy()
    
    def destroy(self):
        """
        Destroys obtacle if it moves offscreen, and if so, removes obstacle from all sprite groups. 
        """
        if self.rect.x <= -100: # -100 ensures obst is FULLY offscreen 
            self.kill()
        