from problem2 import solve_part1, solve_part2


def test_problem2_part1() -> None:
    assert solve_part1([]) == 0
    assert (
        solve_part1(
            [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ]
        )
        == 150
    )


def test_problem2_part2() -> None:
    assert solve_part2([]) == 0
    assert (
        solve_part2(
            [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ]
        )
        == 900
    )
