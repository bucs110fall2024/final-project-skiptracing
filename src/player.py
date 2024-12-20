import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initializes the player object, inlcuding loading player 
        images for walking and jumping animations, 
        setting the initial image and rect 
        for positioning, and initializing gravity. 
        """
        super().__init__() 
        player_walk_1 = pygame.image.load('assets/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0 # pick walk 1 or walk 2 !
        self.player_jump = pygame.image.load('assets/Player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0 

    def player_input(self): 
        """
        Establishes jump mechanic. Use space to jump. Will only jump if player is touching floor. 
        (No air double jumps into infinity!!!)
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300: 
            self.gravity = -20

    def apply_gravity(self):
        """
        Applies gravity to player, causing player to fall downward. 
        """
        # Increase player's vertical position each frame. 
        self.gravity += 1 
        self.rect.y += self.gravity 
        # Prevent player from falling below ground level 
        if self.rect.bottom >= 300: 
            self.rect.bottom = 300 

    def animation_state(self):
        """
        Updates player's animation state. 
        """
        # Jumping animation ( if player midair )
        if self.rect.bottom < 300: 
            self.image = self.player_jump
        # Walking animation ( if player on ground )
        else: 
            self.player_index += .1
            if self.player_index >= len(self.player_walk): # if anim index > length of walking animation frames, reset to 0 
                self.player_index = 0 
            self.image = self.player_walk[int(self.player_index)] # sets current sprite to correct walking frame 
            
    def update(self): 
        """
        Updates player state. Handles player input, gravity, and animation state for player for each frame. 
        """
        self.player_input()
        self.apply_gravity()
        self.animation_state()