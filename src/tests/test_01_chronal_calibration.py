from src.aoc_01_chronal_calibration import compute_frequency


def test_step_1():
    assert compute_frequency(["+1", "+1", "+1"]) == 3
    assert compute_frequency(["+1", "+1", "-2"]) == 0
    assert compute_frequency(["-1", "-2", "-3"]) == -6
