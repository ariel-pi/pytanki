import pygame
from obstacle import Obstacle
from settings import *
from animation import Explosion


def load_obstacles_from_file(file_name):
    """Loads obstacles from a map file and returns a list of Obstacle objects
    :param file_name: The name of the map file
    :return: A list of Obstacle coordinates"""
    obstacles = []
    with open(file_name, 'r') as file:
        for line in file:
            coordinates = eval(line)
            obstacles.append(Obstacle(*coordinates[0], *coordinates[1]))
    return obstacles


def game_over(massage):
    """
    Display a game over message and exit the game
    :param massage: a string to display
    :return: None
    """
    window.fill(WHITE)
    font = pygame.font.Font(None,
                            36)  # You can adjust font size and style as needed
    text = font.render(massage, True,
                       (255, 0, 0))  # Red text color
    text_rect = text.get_rect(center=(
        WIDTH // 2, HEIGHT // 2))  # Center the text on the screen
    window.blit(text, text_rect)
    pygame.display.update()
    close_window = False
    # Wait for the user to close the window
    while not close_window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                close_window = True
                break


def perform_explosion_animation(coordinates):
    """
    Create an explosion animation at the given coordinates
    :param coordinates: list of x,y coordinates
    :return: None
    """
    explosion = Explosion(coordinates[0], coordinates[1], explosion_frames)
    all_sprites.add(explosion)  # Add explosion to the sprite group
    explosion.play_sound()  # Play explosion sound


def get_projectile_obstacle_collisions(tank1,tank2, obstacles):
    """
    Check for collisions between obstacles and projectiles
    :param tank1: the first tank object
    :param tank2: the second tank object
    :param obstacles: list of obstacles objects
    :return: list of coordinates of the collisions
    """
    tanks_list = [tank1, tank2]
    hits = []
    for obstacle in obstacles:
        # Collision detection between projectiles and obstacles
        for tank in tanks_list:
            for projectile in tank.projectiles[
                              :]:  # Use a copy of the list to iterate and modify it
                if obstacle.check_collision(projectile.rect):
                    tank.projectiles.remove(projectile)
                    hits.append([projectile.rect.x, projectile.rect.y])
    return hits


def handle_projectile_tank_collision(tank1, tank2):
    """
    Check for collisions between projectiles and tanks
    :param tank1: the first tank object
    :param tank2: the second tank object
    :return: damaged Tank object if a collision was detected, False otherwise
    """
    # Collision detection between tanks and projectiles
    for tank in [tank1, tank2]:
        for projectile in tank.projectiles[:]:
            # Check collision between the projectile and the other tank
            other_tank = tank1 if tank == tank2 else tank2
            if projectile.rect.colliderect(other_tank.rect):
                # Game over condition - If a projectile hits the other tank, set running to False

                # You can perform additional actions upon game over, such as displaying a message or performing cleanup
                tank.projectiles.remove(projectile)
                return other_tank  # Exit the loop early since the game is over
    return False

# for keep the code clean, we will put all the main functions here

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))


def Window(window_title):
    """
    Create the game window, set the window title and return the window, Simulates the creation of a "Window object"
    :param window_title: the title of the window
    :return: the "Window" object
    """
    pygame.display.set_caption(window_title)

    return window


def draw_text(txt, x, y):
    # Font setup
    font = pygame.font.Font(None, 36)  # You can adjust the font size here
    number = 2  # Initial number to display
    # Draw the number in the top left corner
    text = font.render(txt, True, BLACK)
    window.blit(text, (x, y))  # Adjust the position as needed



# Load explosion frames and resize them to 50x50 pixels
explosion_frame_paths = [f'assets/explosion/explosion{i}.png' for i in range(1,8)]

explosion_frames = []
for frame_path in explosion_frame_paths:
    frame = pygame.image.load(frame_path).convert_alpha()
    frame = pygame.transform.scale(frame, (
    130, 130))  # Resize the frame to 50x50 pixels
    explosion_frames.append(frame)



clock = pygame.time.Clock()
# Create a sprite group to hold all sprites
all_sprites = pygame.sprite.Group()
