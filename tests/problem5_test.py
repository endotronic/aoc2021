from problem5 import (
    solve,
)
from typing import List


provided_example = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]  # type: List[str]


def test_problem5_part1() -> None:
    assert solve(provided_example, consider_diagonals=False) == 5


def test_problem5_part2() -> None:
    assert solve(provided_example, consider_diagonals=True) == 12
