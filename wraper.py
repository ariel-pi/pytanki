
#The functions in this file are intended to wrap the operations that pygame is
# required to perform. The purpose of this file is to simplify the main program.
#If the students are familiar with using pygame, the contents of the functions
# in this file can be transferred to the main program.


import pygame
from main_functions import handle_projectile_tank_collision, all_sprites, \
    clock, FPS, window
from settings import WIDTH, HEIGHT


def update_display():
    """
    This function updates the display and draws all sprites onto the window.
    :return: None
    """
    all_sprites.update()  # Update all sprites
    all_sprites.draw(window)  # Draw all sprites onto the window
    pygame.display.flip()
    clock.tick(FPS)


def get_pressed_keys():
    """
    This function returns a list of all keys that are currently pressed.
     only keys that are relevant to the game will be stored in the list.
    :return: list of keys that are currently pressed
    """
    keys_pressed = pygame.key.get_pressed()
    keys = []
    if keys_pressed[pygame.K_w]:
        keys.append("W")
    if keys_pressed[pygame.K_a]:
        keys.append("A")
    if keys_pressed[pygame.K_s]:
        keys.append("S")
    if keys_pressed[pygame.K_d]:
        keys.append("D")
    if keys_pressed[pygame.K_UP]:
        keys.append("UP ARROW")
    if keys_pressed[pygame.K_DOWN]:
        keys.append("DOWN ARROW")
    if keys_pressed[pygame.K_LEFT]:
        keys.append("LEFT ARROW")
    if keys_pressed[pygame.K_RIGHT]:
        keys.append("RIGHT ARROW")
    if keys_pressed[pygame.K_SPACE]:
        keys.append("SPACE")
    if keys_pressed[pygame.K_RCTRL]:
        keys.append("RCTRL")
    return keys


def tank_hit(tank1, tank2):
    """
    This function checks if a tank was hit by a projectile.
    :param tank1: the first tank object
    :param tank2: the second tank object
    :return: Tank object if a collision was detected, False otherwise
    """
    return handle_projectile_tank_collision(tank1, tank2)


def exit_game_clicked():
    """
    This function checks if the exit button was clicked.
    :return: True if the exit button was clicked, False otherwise
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def load_background(path):
    """
    This function loads the background image from the given path.
    :param path: path to the background image
    :return: pygame.Surface object of the background image
    """
    background_image = pygame.image.load(path)

    # Scale the image to fit the screen if needed
    background_image = pygame.transform.scale(background_image,
                                              (WIDTH, HEIGHT))
    return background_image
