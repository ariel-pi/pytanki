import pygame
from projectile import Projectile
from settings import WIDTH, HEIGHT,FIRE_RATE, PROJECTILE_SPEED

def _image_color_path(color):
    """
    Return the path of the tank image based on the given color
    :param color: string representing the color of the tank
    :return: path of the tank image
    """
    color_paths = {
        "red": "assets/tank/red_tank.png",
        "blue": "assets/tank/blue_tank.png",
        "green": "assets/tank/green_tank.png",
        "yellow": "assets/tank/yellow_tank.png",
        "purple": "assets/tank/purple_tank.png",
        "orange": "assets/tank/orange_tank.png",
        "pink": "assets/tank/pink_tank.png",
        "black": "assets/tank/black_tank.png",
        "white": "assets/tank/white_tank.png",
        "grey": "assets/tank/grey_tank.png",
        "turquoise": "assets/tank/turquoise_tank.png",
    }

    if color in color_paths:
        return color_paths[color]
    else:
        raise ValueError("Invalid tank color")


class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.image = None
        self.rect = None
        self.speed = None
        self.direction = "down"  # Initial direction
        self.projectiles = []  # List to store projectiles fired by the tank
        self.control = None
        self.last_fire_time = pygame.time.get_ticks()  # Variable to store the time of the last fired projectile
        self.fire_rate = FIRE_RATE  # Firing rate in milliseconds

    def define_color(self,color):
        """
        Define the color of the tank
        :param color: one of the following colors: red, blue, green, yellow, purple, orange, pink, black, white, grey, turquoise
        :return: None
        """
        image_path = _image_color_path(color)
        self.image = pygame.transform.scale(pygame.image.load(image_path),
                                            (50, 50))  # Resize the tank image
        # Update the self.rect to match the new dimensions and position of the resized surface
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
    def draw(self, window):
        """
        Draw the tank on the window
        :param window: a pygame.Surface object
        :return: None
        """
        window.blit(self.image, self.rect.topleft)

    def _rotate(self, rotation):
        """
        Rotate the tank image by the given angle
        :param rotation:
        :return:
        """
        self.image = pygame.transform.rotate(self.image, rotation)
        # Update the self.rect to match the new dimensions and position of the rotated surface
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate_to(self, target_direction):
        """
        Rotate the tank to the target direction
        :param target_direction:
        :return:
        """
        # Dictionary to map directions to their corresponding angles
        direction_to_angle = {
            "right": 0,
            "left": 180,
            "up": 90,
            "down": 270
        }
        # Calculate the angle of rotation needed to rotate to the target direction
        target_angle = direction_to_angle[target_direction]
        current_angle = direction_to_angle[self.direction]
        rotation_angle = target_angle - current_angle

        # Rotate the player using the existing 'rotate' method
        self._rotate(rotation_angle)

        # Update the current direction to the target direction
        self.direction = target_direction




    def is_free_to_move(self,other_tank,obstacles,new_x,new_y):
        """
        Check if the tank can move to the given position
        :param other_tank: the other tank object
        :param obstacles: list of obstacles objects
        :param new_x: where the tank will move to on the x-axis
        :param new_y: where the tank will move to on the y-axis
        :return: True if the tank can move to the given position, False otherwise
        """
        temp_rect = self.rect.copy()
        temp_rect.topleft = (new_x, new_y)

        can_move = True
        for obstacle in obstacles:
            if obstacle.check_collision(temp_rect):
                can_move = False
                break
        if other_tank.rect.colliderect(temp_rect):
            can_move = False
        return can_move



    def can_fire(self):
        """
        Check if the tank can fire a projectile
        :return: True if the tank can fire a projectile, False otherwise
        """
        # Check if enough time has passed since the last fired projectile
        current_time = pygame.time.get_ticks()
        return current_time - self.last_fire_time >= self.fire_rate
    def shoot(self):
        """
        Shoot a projectile from the tank
        :return: None
        """
        if self.can_fire():
            self.last_fire_time = pygame.time.get_ticks()  # Update the last fired time
            # Create a projectile based on tank direction and position
            projectile_speed = PROJECTILE_SPEED
            projectile = None
            if self.direction == "right":
                projectile = Projectile(self.rect.right, self.rect.centery-10,
                                        self.direction, projectile_speed)
            elif self.direction == "left":
                projectile = Projectile(self.rect.left, self.rect.centery-10,
                                        self.direction, projectile_speed)
            elif self.direction == "up":
                projectile = Projectile(self.rect.centerx-10, self.rect.top,
                                        self.direction, projectile_speed)
            elif self.direction == "down":
                projectile = Projectile(self.rect.centerx-10, self.rect.centery,
                                        self.direction, projectile_speed)

            # Append the projectile to the list of tank projectiles
            self.projectiles.append(projectile)




    def update_projectiles(self):
        """
        Update the position of projectiles and remove them if they go off-screen
        :return: None
        """
        for projectile in self.projectiles:
            projectile.move()

            # Remove projectile if it goes off-screen
            if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(
                    projectile.rect):
                self.projectiles.remove(projectile)

    def draw_projectiles(self, window):
        """
        Draw all projectiles fired by the tank
        :param window: a pygame.Surface object
        :return: None
        """
        # Draw all projectiles fired by the tank
        for projectile in self.projectiles:
            projectile.draw(window)
