from problem1 import solve


def test_problem1_part1() -> None:
    assert solve([]) == 0
    assert solve([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7
    assert solve([3, 2, 1]) == 0
    assert solve([1, 3, 2]) == 1


def test_problem1_part2() -> None:
    assert solve([], window_size=3) == 0
    assert solve([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], window_size=3) == 5
    assert solve([3, 2, 1, 3, 1], window_size=2) == 1
    assert solve([1, 3, 2, 5, 6, 7], window_size=2) == 4
