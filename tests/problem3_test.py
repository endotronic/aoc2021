from problem3 import (
    get_sums,
    get_gamma_and_epsilon,
    solve_part1,
    get_oxygen_generator_rating,
    get_co2_scrubber_rating,
    solve_part2,
)


provided_example = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_get_sums() -> None:
    assert get_sums(provided_example) == [7, 5, 8, 7, 5]
    assert get_sums(["001", "001", "011", "011"]) == [0, 2, 4]


def test_get_gamma_and_epsilon() -> None:
    assert get_gamma_and_epsilon([7, 5, 8, 7, 5], len(provided_example)) == (22, 9)
    assert get_gamma_and_epsilon([1, 2, 3], 3) == (3, 4)


def test_problem3_part1() -> None:
    assert solve_part1(provided_example) == 198


def test_get_oxygen_generator_rating() -> None:
    assert get_oxygen_generator_rating(provided_example) == 23


def test_get_co2_scrubber_rating() -> None:
    assert get_co2_scrubber_rating(provided_example) == 10


def test_problem3_part2() -> None:
    assert solve_part2(provided_example) == 230
