from problem6 import (
    solve,
    rotate_array,
)


def test_problem6_part1() -> None:
    assert solve("3,4,3,1,2", num_days=18) == 26
    assert solve("3,4,3,1,2", num_days=80) == 5934


def test_problem6_part2() -> None:
    assert solve("3,4,3,1,2", num_days=256) == 26984457539


def test_rotate_array() -> None:
    assert rotate_array([]) == []
    assert rotate_array([8]) == [8]
    assert rotate_array([1, 2, 3]) == [2, 3, 1]
