from src.aoc_02_IMS import compute_checksum


def test_step_1():
    input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    output = compute_checksum(input)
    assert output == 12
