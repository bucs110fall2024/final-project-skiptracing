import pygame 
import random 

class Customer:
    def __init__(self):
        self.order = random.choice(["Latte", "Cappuccino", "Espresso"])
        self.served = False
        self.rect = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 100, 150)  # Adjust the values as needed

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 128, 0), self.rect)  # Drawing the customer as a simple rectangle
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.order, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x, self.rect.y - 30))  # Adjust the position as needed
