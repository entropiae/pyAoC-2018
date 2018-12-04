from src.aoc_02_IMS import compute_checksum, find_adjacent_boxes_id


def test_step_1():
    puzzle_input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    output = compute_checksum(puzzle_input)
    assert output == 12


def test_step_2():
    puzzle_input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
    output = find_adjacent_boxes_id(puzzle_input)

    assert output == "fgij"
