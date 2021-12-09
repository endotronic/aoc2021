from problem9 import (
    solve_part1,
    solve_part2,
)


provided_example = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def test_problem9_part1() -> None:
    assert solve_part1(provided_example) == 15


def test_problem9_part2() -> None:
    assert solve_part2(provided_example) == 1134
