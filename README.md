# PyTanki - Tank Game for Python Learning

PyTanki is a tank game designed to facilitate the learning process for students who wish to grasp fundamental concepts of Python programming and computer science. The game focuses on simplifying the codebase using Pygame and encapsulates various functionalities, allowing students to grasp a minimal set of functions while constructing a complete and engaging game.
<div align="center">
  <p>click on the image below for watching!</p>
  <a href="https://www.youtube.com/watch?v=TeQ8oLpG4fU">
    <img src="https://img.youtube.com/vi/TeQ8oLpG4fU/0.jpg" alt="PyTanki Gameplay Video" />
  </a>
</div>




## Target Audience

PyTanki is suitable for students who possess knowledge in the following subjects:
- Variables
- Conditions
- Loops
- Functions
- Object-Oriented Programming (OOP)

## Project Overview

The game involves two tanks engaged in a battle scenario, aiming to eliminate each other by firing projectiles. The students are provided with all the files except `main.py` and `tank.py`, which they must complete based on the provided skeleton code found in `main_skeleton.py` and `tank_skeleton.py`.

Upon distribution to students, these files can simply be renamed to `main.py` and `tank.py`.

## Getting Started

To get started with PyTanki, follow these steps:
1. Ensure you have Python installed on your system.
2. Install Pygame using `pip install pygame`.
3. Clone or download this repository to your local machine.

## Files in the Project

- **main.py**: This file acts as the main entry point for the game. It involves initializing the game window, managing player actions, handling collisions, and updating the game state.
- **main_skeleton.py**: Provides a skeletal structure of the `main.py` file with tasks marked as TODOs. Students need to complete the code based on these task prompts.
- **tank.py**: Contains the implementation for the Tank class responsible for tank movement, shooting projectiles, collision detection, and handling the tank's attributes.
- **tank_skeleton.py**: Provides a skeletal structure of the `tank.py` file with tasks marked as TODOs. Students need to complete the code based on these task prompts.
- **main_functions.py**: Contains helper functions used in `main.py` for functionalities such as handling collisions, drawing game elements, and managing game-over scenarios.
- **player.py**: Defines the Player class responsible for creating and managing the tanks' attributes and actions, including movement and shooting projectiles.
- **obstacle.py**: Implements the Obstacle class responsible for creating obstacles within the game environment.
- **projectile.py**: Contains the Projectile class responsible for creating, moving, and drawing projectiles fired by the tanks.
- **Animation.py**: Handles the explosion animation displayed upon projectile collisions.
- **settings.py**: Contains game settings such as screen dimensions, colors, firing rate, and projectile speed.
- **wraper.py**: Wraps certain Pygame operations to simplify the main program and provide a cleaner codebase.
- **maps/**: Contains map definitions defining obstacle locations for different game levels.
- **assets/**: Contains images used in the game, including tank images, projectile images, background images, etc.
- **map_creator.py**: An independent program to facilitate the creation of new maps by defining obstacle locations through a user-friendly interface.

## Getting Help

If you encounter any issues or have queries related to PyTanki, feel free to reach out by raising an issue in the repository or contacting the project maintainers.

### Contributors

- Ariel Pinhas - Sole Developer/Creator
- [GitHub](https://github.com/ariel-pi)
- [Linkdin](http://www.linkedin.com/in/ariel-pinhas)


## Contributing

Contributions to PyTanki are welcome! If you'd like to contribute enhancements, bug fixes, or new features, please fork this repository, make your changes, and submit a pull request.

## Acknowledgments

Special thanks to the contributors and the community for their support and feedback!

## License

This project is licensed under the MIT License.
