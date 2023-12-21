import pygame


class Projectile:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed

        # Load an image for the projectile
        original_image = pygame.image.load('assets/tank/projectile.png')
        self.image = pygame.transform.scale(original_image, (20, 20))

        # Get the rectangle of the image for collision detection
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self):
        # Move the projectile in the direction it is facing
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed

        # Update the rect position based on self.x and self.y
        self.rect.topleft = (self.x, self.y)

    def draw(self, window):
        """
        Draw the projectile on the window
        :param window: a  pygame.Surface object
        :return: None
        """
        # Draw the image on the window
        window.blit(self.image, self.rect)
