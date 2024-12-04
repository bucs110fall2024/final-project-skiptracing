import pygame 
import random 

class Customer: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.order = random.choice(["coffee_milk", "coffee_sugar"])
        self.image = pygame.image.load('assets/customer.png')
        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        font = pygame.font.Font(None, 36)
        text = font.render(self.order, True, (0,0,0))
        screen.blit(text, (self.x, self.y-20))
        
        
        
# BUGS LIST 

# start screen 
# death screen 
# win screen 
# coffee making screen ( cup changes based on ingred)


# customers 
# larger, white? orders appear overhead 
# customers: larger, white, order appears overhead on textbox 
# one customer at a time 
# 
# timer countdown per customer 
# customers emote based on win / loss 
