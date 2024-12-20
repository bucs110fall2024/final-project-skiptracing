import pygame 

# This is literally just practice because pygame has me tripping 




# Initialize pygame 
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800,600))

# Caption and Icon 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png') # Load image 
pygame.display.set_icon(icon) # Set display icon 

# Player 
playerImg = pygame.image.load('player.png')
playerX = 370 
playerY = 480 
playerX_change = 0 

def player(x, y): 
    screen.blit(playerImg, (x, y))

# Game Loop 
running = True 
while running: 
    # RGB: draw screen below all          
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
            
    # Movement 
        if event.type == pygame.KEYDOWN: # press button
            if event.key == pygame.K_LEFT: 
                print("left arrow pressed ")
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                print("right arrow pressed ")
                playerX_change = 0.2
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke has been released")
                playerX_change = 0

    playerX += playerX_change 
    
    if playerX <= 0: 
        playerX = 0 
    elif playerX >= 736: 
        playerX = 736 
    player(playerX, playerY) # Order matters. Call after screen drawn. 
    pygame.display.update() # Update display 