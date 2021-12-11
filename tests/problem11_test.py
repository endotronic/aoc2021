from problem11 import (
    solve_part1,
    solve_part2,
)
from typing import List


provided_example = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


def test_problem11_part1() -> None:
    assert solve_part1(provided_example) == 1656


def test_problem11_part2() -> None:
    assert solve_part2(provided_example) == 195
