from problem15 import (
    solve_part1,
    solve_part2,
)
from typing import List


provided_example = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip().split(
    "\n"
)


def test_problem15_part1() -> None:
    assert solve_part1(provided_example) == 40


def test_problem15_part2() -> None:
    assert solve_part2(provided_example) == 315
