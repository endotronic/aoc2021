from problem10 import (
    solve_part1,
    solve_part2,
    find_completion,
)
from typing import List


provided_example = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_problem10_part1() -> None:
    assert solve_part1(provided_example) == 26397


def test_problem10_part2() -> None:
    assert solve_part2(provided_example) == 288957


def test_find_completion() -> None:
    assert find_completion("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
    assert find_completion("[(()[<>])]({[<{<<[]>>(") == ")}>]})"
    assert find_completion("(((({<>}<{<{<>}{[]{[]{}") == "}}>}>))))"
