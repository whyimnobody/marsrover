import random

import pytest

from rover import (
    execute_rover_commands,
    prep_initial_rover_details,
    Rover,
    set_plateau_limits,
)


@pytest.fixture
def given_rover_input():
    return [
        "5 5",
        "1 2 N",
        "LMLMLMLMM",
        "3 3 E",
        "MMRMMRMRRM",
    ]


@pytest.fixture
def given_rover_commands():
    return [
        "3 3 E",
        "MMRMMRMRRM",
    ]


def test_rover_rotate_left():
    rover = Rover(1, 2, "N")
    rover.rotate("L")
    assert rover.orientation == "W"


def test_rover_rotate_right():
    rover = Rover(4, 5, "S")
    rover.rotate("R")
    assert rover.orientation == "W"


def test_rover_move_forward_in_plateau():
    rover = Rover(1, 2, "S")
    rover.move()
    # NOTE: Garbage test, due to the way max_x and max_y are defined in script
    assert rover.y_position == 1


def test_rover_move_forward_edge_plateau():
    rover = Rover(0, 10, "W")
    rover.move()
    # NOTE: Garbage test, due to the way max_x and max_y are defined in script
    assert rover.x_position == 0


def test_rover_executes_commands(given_rover_commands):
    rovers = execute_rover_commands(given_rover_commands)
    rover = rovers[0]
    assert rover.__dict__ == Rover(5, 1, "E").__dict__


def test_prep_initial_rover_details():
    given_initial_details = "1 2 N"
    assert prep_initial_rover_details(given_initial_details) == (1, 2, "N")


def test_set_plateau_limits():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    sample_input = f"{x} {y}"
    assert set_plateau_limits(sample_input) == [x, y]
