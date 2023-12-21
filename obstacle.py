import pygame

class Obstacle:
    def __init__(self, x1, y1, x2, y2, image_path='assets/window/obstacle.jpg'):
        self.rect = pygame.Rect(x1, y1, x2, y2)
        self.image = pygame.image.load(image_path)
        # Crop the image to the obstacle size
        self.image = self.image.subsurface(self.rect)

    def draw(self, window):
        """
        Draw the obstacle on the window
        :param window: pygame.Surface object
        :return: None
        """
        window.blit(self.image, self.rect.topleft)


    def check_collision(self, game_object):
        """
        Check if the obstacle collides with the given game object
        :param game_object: pygame.Rect object
        :return: True if the obstacle collides with the given game object, False otherwise
        """
        return self.rect.colliderect(game_object)
