from problem14 import (
    solve,
    solve_v2,
    parse_input,
    do_iterations_v1,
)
from typing import List


provided_example = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip().split(
    "\n"
)


def test_problem14_iterations() -> None:
    start, insertions = parse_input(provided_example)
    assert len(do_iterations_v1(start, insertions, iterations=5)) == 97

    result = do_iterations_v1(start, insertions, iterations=10)
    assert len(result) == 3073
    assert result.count("B") == 1749
    assert result.count("C") == 298
    assert result.count("H") == 161
    assert result.count("N") == 865


def test_problem14_part1() -> None:
    assert solve(provided_example, iterations=10) == 1588
    assert solve_v2(provided_example, iterations=10) == 1588


def test_problem14_part2() -> None:
    assert solve_v2(provided_example, iterations=40) == 2188189693529
