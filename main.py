from tank import Tank
from main_functions import *
from wraper import *
import pygame

# Initialize Pygame
pygame.init()

# TODO: create two tanks object
tank1 = Tank(50, 50, "red", "wasd")
tank2 = Tank(700, 500, "blue", "arrows")
# TODO: Set the amount of rejects for each tank
tank1_live = 3
tank2_live = 3

# TODO Load obstacles from a map file
obstacles = load_obstacles_from_file('maps/map1.txt')
# TODO Load the image for the background
background_image = load_background("assets/window/background.jpg")

# TODO: Create the game window
window = Window("Tanks game")
running = True
# Game loop
while running == True:
    # TODO Check if the player has pressed the close button on the window by calling exit_game_clicked()
    if exit_game_clicked():
        break
    # TODO Draw the background image
    window.blit(background_image, (0, 0))

    # TODO Draw obstacles
    for obstacle in obstacles:
        obstacle.draw(window)

    # TODO: Draw tanks lives
    draw_text("tank1: " + str(tank1_live), 10, 10)
    draw_text("tank2: " + str(tank2_live), 600, 10)

    # TODO: Draw projectiles
    tank1.draw_projectiles(window)
    tank2.draw_projectiles(window)

    # TODO: Draw tanks
    tank1.draw(window)
    tank2.draw(window)
    # TODO: Update the display
    update_display()

    # TODO Update projectile location
    tank1.update_projectiles()
    tank2.update_projectiles()

    # TODO: Get the keys pressed by the player
    keys_pressed = get_pressed_keys()

    # TODO handle tank1 movement
    tank1.handle_movement(tank2, obstacles, keys_pressed)

    # TODO handle tank2 movement
    tank2.handle_movement(tank1, obstacles, keys_pressed)

    # TODO: Check if the player has pressed the shoot button and if so shoot a projectile
    if "SPACE" in keys_pressed:
        tank1.shoot()
    if "RCTRL" in keys_pressed:
        tank2.shoot()

    # TODO: Check for collisions between obstacles and projectiles
    obstacles_collisions = get_projectile_obstacle_collisions(tank1, tank2,
                                                              obstacles)
    for collision in obstacles_collisions:
        perform_explosion_animation(collision)

    # TODO:check if a tank was hit by a projectile
    got_hit = tank_hit(tank1, tank2)
    if tank1 == got_hit:
        perform_explosion_animation([tank1.x + 25, tank1.y + 25])
        tank1_live -= 1
        if tank1_live == 0:
            game_over("game over tank 2 win!")  # Display a game over message
            running = False

    if tank2 == got_hit:
        perform_explosion_animation([tank2.x + 25, tank2.y + 25])
        tank2_live -= 1
        if tank2_live == 0:
            game_over("game over tank 1 win!")
            running = False

pygame.quit()
