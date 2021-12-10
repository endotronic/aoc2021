from problem6 import (
    solve,
)


def test_problem6_part1() -> None:
    assert solve("3,4,3,1,2", num_days=18) == 26
    assert solve("3,4,3,1,2", num_days=80) == 5934


def test_problem6_part2() -> None:
    assert solve("3,4,3,1,2", num_days=256) == 26984457539
