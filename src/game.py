import pygame
import random 
import sys
from src.components import Button
from src.customer import Customer

class CoffeeGame:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.BG_COLOR = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Coffee Making Simulator!~")
        icon = pygame.image.load('assets/coffee.png') 
        pygame.display.set_icon(icon) # Set display icon 
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('assets/background.png')
        self.coffee_cup = pygame.image.load('assets/coffee_cup.png')
        self.heart_image = pygame.image.load('assets/heart.png')

        self.milk_button = Button("Add Milk", (50, 500), 30, "green")
        self.sugar_button = Button("Add Sugar", (200, 500), 30, "brown")

        self.customers = [Customer(50, 100), Customer(300, 100), Customer(550, 100)]
        self.current_order = None
        self.orders_completed = 0
        self.hearts = 3

    def check_order(self, ingredients):
        if self.current_order.order == ingredients:
            self.orders_completed += 1
            self.customers.remove(self.current_order)
            self.current_order = None
            print("Order completed!")
        else:
            self.hearts -= 1
            print("Wrong order!")

        if self.orders_completed == 3:
            print("You win!")
            pygame.quit()
            sys.exit()
        elif self.hearts == 0:
            print("Game over!")
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.milk_button.click(event):
                        ingredients = "coffee_milk"
                    elif self.sugar_button.click(event):
                        ingredients = "coffee_sugar"
                    else:
                        ingredients = "coffee_milk_sugar"
                    
                    if self.current_order:
                        self.check_order(ingredients)

            if not self.current_order and self.customers:
                self.current_order = random.choice(self.customers)

            self.screen.fill(self.BG_COLOR)
            self.screen.blit(self.bg_image, (0, 0))
            self.screen.blit(self.coffee_cup, (350, 250))
            self.milk_button.show(self.screen)
            self.sugar_button.show(self.screen)

            for customer in self.customers:
                customer.show(self.screen)

            for i in range(self.hearts):
                self.screen.blit(self.heart_image, (10 + i * 30, 10))

            pygame.display.flip()
            self.clock.tick(60)
