# Pixel Runners! A Title that I'm proably gonna change. 

## Team Members: 
Sofie Caballes 

## Project Description: 
Pixel Runner is a 2D side-scrolling platformer. Your objective is to control a pixelated character and avoid enemies like snails and flies. The longer you live, the better your score. 

## GUI Design - Initial Design:
See assets/gui.jpg 

## Program Design - Features 
1. Start Menu
2. Animated characters
3. Obstacle collisions 
4. Game over screen 
5. Music 

### Classes: 

> Player Class 

Attributes: 
- `player_walk`: List of images used for players walking animation 
- `player_index`: Index to track current frame in the walking animation. 
- `player_jump`: Image used for the player's jumping animation. 
- `image`: Current image of player to be displayed. 
- `rect`: Rect object defining the player's position and size. 
- `gravity`: Value to simulate gravity's effect on the player. 

Methods: 
- `__init__(self)`: Initializes the player object. 
- `player_input(self)`: Handles player input for controlling the player. 
- `apply_gravity(self)`: Applies gravity to player, causing player to fall downward. 
- `animation_state(self)`: Updates the player's animation state based on whether the player is walking or jumping. 
- `update(self)`: Updates the player's state every frame, including handling input, applying gravity, and updating animation. 

> Obstacle Class 

Attributes: 
- `frames`: List of images used for obstacle's animation.
- `animation_index`: Index to track the current frame in the animation. 
- `image`: Current image of the obstacle to be displayed. 
- `rect`: Rect object defining the obstacle's position and size. 

Methods: 
- `__init__(self, type)`: Initialies the obstacle object, loading images based on the obstacle type (fly or snail). 
- `animation_state(self)`: Updates the obstacle's animation state by cycling through frames. 
- `update(self)`: Updates the obstacle's state each frame, including moving and possibly destroying obstacle. 
- `destroy(self)`: Destroys the obstacle if it moves off-screen. 