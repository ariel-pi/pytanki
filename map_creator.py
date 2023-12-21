
# This program is independent. This program allows you to quickly create new maps
#  by quickly defining the locations of the obstacles and an easy-to-use interface.
# Creating a new obstacle is done by clicking and dragging the mouse.
# Deleting an obstacle object is done by right-clicking on the obstacle.
# Pressing S will save to a file.
# At the beginning of the program, the name of the map must be entered.



import pygame
import sys
from settings import *

map_name = input("Enter map name: ")

# Initialize pygame
pygame.init()

# Set up the display
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Drawing Program")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Rectangles list
rectangles = []

def save_rectangles(filename):
    """
    Save the rectangles list to a file
    :param filename: the name of the file to save to
    :return: None
    """
    with open(filename, 'w') as f:
        for rect in rectangles:
            f.write(f"{rect}\n")




def main():
    running = True
    drawing = False
    current_rect = None

    while running:
        WINDOW.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button (add rectangle)
                    drawing = True
                    start_pos = pygame.mouse.get_pos()
                    current_rect = [start_pos, (0, 0)]
                elif event.button == 3:  # Right mouse button (remove rectangle)
                    click_pos = pygame.mouse.get_pos()
                    for rect in rectangles:
                        if pygame.Rect(*rect).collidepoint(*click_pos):
                            rectangles.remove(rect)
                            print("Rectangle removed")
                            break

            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    end_pos = pygame.mouse.get_pos()
                    current_rect[1] = (end_pos[0] - current_rect[0][0], end_pos[1] - current_rect[0][1])

            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    drawing = False
                    print(current_rect)
                    rectangles.append(tuple(current_rect))
                    current_rect = None

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    save_rectangles(f"maps/{map_name}.txt")
                    print(f"the map saved to maps/{map_name}.txt")

        for rect in rectangles:
            pygame.draw.rect(WINDOW, RED, (*rect[0], *rect[1]), 2)

        if current_rect:
            pygame.draw.rect(WINDOW, BLACK, (*current_rect[0], *current_rect[1]), 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

