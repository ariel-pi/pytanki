from player import Player


class Tank(Player):
    def __init__(self, x, y, color, control):
        super().__init__()
        # TODO: initialize the tank attributes


    def move_to(self,new_x,new_y,new_direction):
        """
        Move the tank to a new location and rotate it to the new direction
        :param new_x: where to move the tank on the x axis
        :param new_y: where to move the tank on the y axis
        :param new_direction: the new direction of the tank
        :return: None
        """
        # TODO: implement tank movement

        # TODO: Don't change
        self.rect.topleft = (self.x, self.y)

    def handle_movement(self, other_tank, obstacles, keys_pressed_list):
        """
        Handle the movement of the tank
        :param other_tank: the other tank object
        :param obstacles: list of obstacles objects
        :param keys_pressed_list: list of keys pressed by the player
        :return: None
        """
        # TODO: handle tank movement

        #TODO: check if the tank can move to the new location
        pass



