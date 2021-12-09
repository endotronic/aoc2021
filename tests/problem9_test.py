from problem9 import (
    solve_part1,
)
from typing import List


provided_example = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]  # type: List[str]


def test_problem9_part1() -> None:
    assert solve_part1(provided_example) == 15
