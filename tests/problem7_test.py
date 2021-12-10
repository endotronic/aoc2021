from problem7 import (
    solve,
)


def test_problem7_part1() -> None:
    assert solve("16,1,2,0,4,2,7,1,2,14", part=1) == 37


def test_problem7_part2() -> None:
    assert solve("16,1,2,0,4,2,7,1,2,14", part=2) == 168
