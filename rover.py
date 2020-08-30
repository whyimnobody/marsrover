from collections import deque
from sys import exit


max_x, max_y = 10, 10


class Rover:
    """Object-representation of a Rover

	Each rover can be represented as an object with the position and orientation
	as properties
	"""

    POSSIBLE_ORIENTATIONS = ["N", "E", "S", "W"]  # The compass points as a list

    def __init__(self, x_position, y_position, orientation):
        """
		@param x_position: The rover's x-position
		@param y_position: The rover's y-position
		@param orientation: The direction the rover is facing
		"""
        # TODO(ksebopelo): Add check to ensure starting position is in plateau
        # TODO(ksebopelo): Add check to ensure orientation is valid
        # TODO(ksebopelo): Add check to ensure rovers don't collide (start)
        self.x_position = x_position
        self.y_position = y_position
        orientation_index = self.POSSIBLE_ORIENTATIONS.index(orientation.upper())
        self._orientation = deque(self.POSSIBLE_ORIENTATIONS)
        self._orientation.rotate(-orientation_index)

    @property
    def orientation(self):
        return self._orientation[0]

    def rotate(self, direction):
        """Rotate the rover in-place
		@param direction: The direction in which the rover should rotate
		"""
        if direction.upper() == "L":
            self._orientation.rotate(1)
        elif direction.upper() == "R":
            self._orientation.rotate(-1)
        else:
            print("Not a valid direction in which to rotate")

    def move(self):
        """Move the rover forward
		"""
        # TODO(ksebopelo): Add check to ensure rovers don't collide (moving)
        if self.orientation == "N":
            self.y_position = (
                self.y_position + 1 if self.y_position < max_x else self.y_position
            )
        elif self.orientation == "E":
            self.x_position = (
                self.x_position + 1 if self.x_position < max_y else self.x_position
            )
        elif self.orientation == "S":
            self.y_position = (
                self.y_position - 1 if self.y_position > 0 else self.y_position
            )
        elif self.orientation == "W":
            self.x_position = (
                self.x_position - 1 if self.x_position > 0 else self.x_position
            )

    def parse_commands(self, commands):
        """Parse the alternating instructions from input to rotate or move
		accordingly
		"""
        for cmd in commands:
            if cmd.upper() == "M":
                self.move()
            else:
                self.rotate(cmd)


def set_plateau_limits(coordinates):
    """Set the maximum x and maximum y coordinates
	@param coordinates: A string indicating the top right position of the plateau and setting the variables as specified
	"""
    coordinates = coordinates.split()
    return list(map(int, coordinates))


def prep_initial_rover_details(initial_points):
    """Return the initial coordinates as integers and orientation as an uppercase string
	@param initial_points: String containing initial points and orientations
	"""
    initial_input = initial_points.split()
    orientation = initial_input.pop()
    x_position, y_position = list(map(int, initial_input))

    return x_position, y_position, orientation


def execute_rover_commands(commands):
    """Abstraction of command execution for testing
	@param commands: List of commands as tendered for rover details
	"""
    rovers = []

    for each in range(len(commands) // 2):
        rover_coordinates = commands.pop(0)
        rover_movements = commands.pop(0)
        # Prepare the object with its position and orientation
        rover_input = prep_initial_rover_details(rover_coordinates)
        rover = Rover(*rover_input)
        # Move the rover and add the object to the rovers list!
        rover.parse_commands(rover_movements)
        rovers.append(rover)

    return rovers


def main_rover_application():
    """Provide a loop for user to input rover commands"""

    complete = False
    instructions = []
    rovers = []

    # The application run, where inputs are tendered
    while not complete:
        entry = input()
        if entry:
            instructions.append(entry)
        else:
            complete = True

    if not instructions:
        print("No instructions given.")
        return

    # Set the plateau limits with the first input
    plateau_limits = instructions.pop(0)
    max_x, max_y = set_plateau_limits(plateau_limits)

    # Set each rovers position, and move it accordingly
    rovers = execute_rover_commands(instructions)

    # Display final rover position and orientation for each rover
    for rover in rovers:
        print(f"{rover.x_position} {rover.y_position} {rover.orientation}")
