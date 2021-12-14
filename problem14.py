"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 14
"""

import argparse
from collections import defaultdict
import re
from typing import Dict, List, Tuple


def solve_part1(lines: List[str]) -> int:
    start, insertions = parse_input(lines)
    sequence = do_iterations(start, insertions)
    hist = list(histogram(sequence).items())
    hist.sort(key=lambda c: c[1])

    _, min = hist[0]
    _, max = hist[-1]
    return max - min


def parse_input(lines: List[str]) -> Tuple[str, Dict[str, str]]:
    if len(lines) < 3:
        raise ValueError("Invalid input")

    start = lines[0]
    assert len(lines[1]) == 0
    insertions = dict()  # type: Dict[str, str]

    for i in range(2, len(lines)):
        parsed = re.match("([A-Z][A-Z]) -> ([A-Z])", lines[i])
        if not parsed:
            raise ValueError("Invalid input on line {}".format(i))

        pair = parsed.groups()[0]
        insertion = parsed.groups()[1]
        insertions[pair] = insertion

    return start, insertions


def do_iterations(start: str, insertions: Dict[str, str], iterations: int = 10) -> str:
    sequence = start
    for _ in range(iterations):
        next = ""
        for i in range(len(sequence)):
            pair = sequence[i : i + 2]
            next += pair[0]
            if pair in insertions:
                next += insertions[pair]

        sequence = next
    return sequence


def histogram(sequence: str) -> Dict[str, int]:
    result = defaultdict(int)  # type: Dict[str, int]
    for c in sequence:
        result[c] += 1
    return result


def solve_part2(lines: List[str]) -> int:
    """
    This approach will run out of memory
    """
    start, insertions = parse_input(lines)
    sequence = do_iterations(start, insertions, iterations=40)
    hist = list(histogram(sequence).items())
    hist.sort(key=lambda c: c[1])

    _, min = hist[0]
    _, max = hist[-1]
    return max - min


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 14")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem14.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    if args.part == 1:
        output = solve_part1(lines)
    elif args.part == 2:
        output = solve_part2(lines)
    else:
        raise ValueError("Unknown part")

    print(output)
