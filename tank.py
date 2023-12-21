from player import Player


class Tank(Player):
    def __init__(self, x, y, color, control):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = "down"  # Initial direction
        self.control = control
        self.define_color(color)


    def move_to(self,new_x,new_y,new_direction):
        """
        Move the tank to a new location and rotate it to the new direction
        :param new_x: where to move the tank on the x axis
        :param new_y: where to move the tank on the y axis
        :param new_direction: the new direction of the tank
        :return: None
        """
        self.x = new_x
        self.y = new_y
        self.rotate_to(new_direction)

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
        # TODO: implement tank movement
        new_x = self.x
        new_y = self.y
        if self.control == "wasd":
            up = "W"
            down = "S"
            left = "A"
            right = "D"
        else:
            up = "UP ARROW"
            down = "DOWN ARROW"
            left = "LEFT ARROW"
            right = "RIGHT ARROW"
        new_direction = self.direction

        if left in keys_pressed_list:
            new_x = self.x - self.speed
            new_direction = "left"
        elif right in keys_pressed_list:
            new_x = self.x + self.speed
            new_direction = "right"
        elif up in keys_pressed_list:
            new_y = self.y - self.speed
            new_direction = "up"
        elif down in keys_pressed_list:
            new_y = self.y + self.speed
            new_direction = "down"
        #TODO: check if the tank can move to the new location
        if self.is_free_to_move(other_tank,obstacles, new_x, new_y):
            self.move_to(new_x, new_y, new_direction)



