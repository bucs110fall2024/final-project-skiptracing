import pygame 
import random 

class Customer: 
    def __init__(self, x, y): 
        self.x, self.y = x, y 
        self.order = random.choice(["coffee_milk", "coffee_sugar", "coffee_milk_sugar"])
        self.image = pygame.image.load('assets/customer.png')
        
    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        font = pygame.font.Font(None, 36)
        text = font.render(self.order, True, (0,0,0))
        screen.blit(text, (self.x, self.y-20))