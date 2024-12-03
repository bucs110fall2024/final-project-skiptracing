## Team Members: Individual 

## Project Description: Coffee brewing simulator! 

## Program Design: 

### Classes

#### Player
- **Attributes**:
  - `name` (str): Player's name
  - `x` (int): x-coordinate of the player's position
  - `y` (int): y-coordinate of the player's position
  - `img` (pygame.Surface): Image of the player
  
- **Methods**:
  - `__init__(self, name, x, y, img_file)`: Initializes the player object
  - `move_right(self)`: Moves player right by 1
  - `move_left(self)`: Moves player left by 1
  - `move_up(self)`: Moves player up by 1
  - `move_down(self)`: Moves player down by 1
  - `draw(self, screen)`: Draws the player on the screen

#### CoffeeOrder
- **Attributes**:
  - `customer_name` (str): Name of the customer
  - `coffee_type` (str): Type of coffee
  - `size` (str): Size of the coffee (small, medium, large)
  - `img` (pygame.Surface): Image of the coffee order

- **Methods**:
  - `__init__(self, customer_name, coffee_type, size, img_file)`: Initializes the coffee order object
  - `prepare(self)`: Prepares the coffee order
  - `serve(self)`: Serves the coffee order to the customer
  - `draw(self, screen)`: Draws the coffee order on the screen
  
<!-- 
start menu
buttons 
characters 
scrolling background
game over screen  -->

