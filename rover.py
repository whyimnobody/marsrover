from collections import deque


class Rover:
    """Object-representation of a Rover

    Each rover can be represented as an object with the position and orientation
    as properties
    """

    def __init__(self, x_position, y_position, orientation):
        """
        @param x_position: The rover's x-position
        @param y_position: The rover's y-position
        @param orientation: The direction the rover is facing
        """

        self.x_position = x_position
        self.y_position = y_position
        orientation_index = possible_orientations.index(orientation.upper())
        self.orientation = deque(possible_orientations).rotate(orientation_index)

    def rotate(self, direction):
        """Rotate the rover in-place
        @param direction: The direction in which the rover should rotate
        """
        pass

    def move(self):
        """Move the rover forward
        """
        pass


possible_orientations = ["N", "E", "S", "W"]  # The compass points as a list


def set_plateau_limits(coordinates):
    """Set the maximum x and maximum y coordinates
    @param coordinates: A string indicating the top right position of the plateau and setting the variables as specified
    """
    pass


def prep_initial_rover_points(initial_points):
    """Return the initial coordinates as integers and orientation as an uppercase string
    @param initial_points: String containing initial points and orientations
    """
    pass


