import pygame 
import random 

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coffee Maker Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
customer_timer = 0
customer_interval = 5000  # time in milliseconds
customers = []

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) 

class Customer:
    def __init__(self):
        self.order = random.choice(["Latte", "Cappuccino", "Espresso"])
        self.served = False
        self.rect = pygame.Rect(random.randint(0, WIDTH-100), random.randint(0, HEIGHT-100), 50, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 128, 0), self.rect)
        draw_text(self.order, font, WHITE, surface, self.rect.x, self.rect.y - 20)
