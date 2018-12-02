from src.aoc_01_chronal_calibration import compute_frequency, first_reached_twice


def test_step_1():
    assert compute_frequency(["+1", "+1", "+1"]) == 3
    assert compute_frequency(["+1", "+1", "-2"]) == 0
    assert compute_frequency(["-1", "-2", "-3"]) == -6


def test_step_2():
    assert first_reached_twice(["+1", "-1"]) == 0
    assert first_reached_twice(["+3", "+3", "+4", "-2", "-4"]) == 10
    assert first_reached_twice(["-6", "+3", "+8", "+5", "-6"]) == 5
    assert first_reached_twice(["+7", "+7", "-2", "-7", "-4"]) == 14
