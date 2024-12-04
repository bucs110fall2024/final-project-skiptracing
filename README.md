# Pixel Runners! A Title that I'm proably gonna change. 

## Team Members: 
Sofie Caballes 

## Project Description: 
Pixel Runner is a 2D side-scrolling platformer. Your objective is to control a pixelated character and avoid enemies like snails and flies. The longer you live, the better your score. 

## GUI Design - Initial Design:
See assets/gui.jpg 

## Program Design

### Features 
1. Start Menu
2. Animated characters
3. Obstacle collisions 
4. Game over screen 
5. Music 

### Classes: 
#### Player Class 
*Attributes*: 
- `player_walk`: List of images used for players walking animation 
- `player_index`: Index to track current frame in the walking animation. 
- `player_jump`: Image used for the player's jumping animation. 
- `image`: Current image of player to be displayed. 
- `rect`: Rect object defining the player's position and size. 
- `gravity`: Value to simulate gravity's effect on the player. 

*Methods*: 
- `__init__(self)`: Initializes the player object. 
- `player_input(self)`: Handles player input for controlling the player. 
- `apply_gravity(self)`: Applies gravity to player, causing player to fall downward. 
- `animation_state(self)`: Updates the player's animation state based on whether the player is walking or jumping. 
- `update(self)`: Updates the player's state every frame, including handling input, applying gravity, and updating animation. 

#### Obstacle Class 
*Attributes*: 
- `frames`: List of images used for obstacle's animation.
- `animation_index`: Index to track the current frame in the animation. 
- `image`: Current image of the obstacle to be displayed. 
- `rect`: Rect object defining the obstacle's position and size. 

*Methods*: 
- `__init__(self, type)`: Initialies the obstacle object, loading images based on the obstacle type (fly or snail). 
- `animation_state(self)`: Updates the obstacle's animation state by cycling through frames. 
- `update(self)`: Updates the obstacle's state each frame, including moving and possibly destroying obstacle. 
- `destroy(self)`: Destroys the obstacle if it moves off-screen. 

## ATP 

1. Obstacles 
description: 
verify obstacle generation and movement 

steps: 
1. start the game 
2. verify that obstacles (flies and snails) are generated at random intervals. 
3. verify that obstacles move from right to left across screen. 
4. verify that obstacles are removed when they move off-screen. 

expected outcome: 
obstacles are generated, move correctly, and are removed when off-screen. 

<!-- 2. Player Movement 

description: 
verify the player's jump works as expected. 

steps: 
1. start the game 
2. press space to make the player jump 
3. verify the player jumps. 
4. let the player fall. 
5. verify the player falls due to gravity. 

expected outcome: 
the player responds to gravity and jumps correctly when the space key is pressed.  -->

<!-- 4. Collision Detection 
description: 
verify collision detection between the player and obstacles. 

steps: 
1. start the game. 
2. allow the player to collide with an obstacle. 
3. verify the game ends upon collision. 

expected outcome: collisions are detected correctly, ending the game.  -->

<!-- 5. Score Display 
description: 
verify score calculation and display. 

steps: 
1. start the game 
2. verify the score is calculate based on elapsed time since the game started. 
3. verify the score is displayed at the top center of the screen during gameplay. 

expected outcome: 
the score is calculated and displayed correctly.  -->

<!-- 6. Game Over Screen 
description: 
verify the game over screen display. 

steps: 
1. Start the game. 
2. Play until the player collides with an obstacle. 
3. Verify the game over screen displays the player's final score. 
4. Verify the game over message is shown with the option to restart the game by pressing the space key. 

expected outcome: 
The game over screen displays correctly with the final score and restart option. ('Press space') -->



| Step | Description | Results | 
| --- | --- | --- | 