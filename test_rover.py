import random

import pytest

from rover import (
    POSSIBLE_ORIENTATIONS,
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


def test_prep_initial_rover_details():
    given_initial_details = "1 2 N"
    assert prep_initial_rover_details(given_initial_details) == (1, 2, "N")


def test_set_plateau_limits():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    sample_input = f"{x} {y}"
    assert set_plateau_limits(sample_input) == [x, y]
