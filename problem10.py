"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 10
"""

import argparse
from math import floor
from typing import List, Optional

OPENERS = "([{<"
CLOSERS = ")]}>"
SCORES = [3, 57, 1197, 25137]


def solve_part1(lines: List[str]) -> int:
    score = 0

    for line in lines:
        state = []
        for c in line:
            if c in OPENERS:
                i = OPENERS.index(c)
                state.append(i)
            if c in CLOSERS:
                i = CLOSERS.index(c)
                z = state.pop()
                if i != z:
                    score += SCORES[i]
                    break
    return score


def solve_part2(lines: List[str]) -> int:
    scores = []
    for line in lines:
        completion = find_completion(line)
        if completion:
            score = 0
            for c in completion:
                score *= 5
                score += CLOSERS.index(c) + 1
            scores.append(score)
    scores.sort()
    return scores[floor(len(scores) / 2)]


def find_completion(line: str) -> Optional[str]:
    state = []
    for c in line:
        if c in OPENERS:
            state.append(c)
        if c in CLOSERS:
            z = state.pop()
            if CLOSERS.index(c) != OPENERS.index(z):
                return None
    if state:
        state.reverse()
        result = ""
        for c in state:
            result += CLOSERS[OPENERS.index(c)]
        return result
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 10")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem10.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        filtered_lines = list(filter(lambda line: bool(line), lines))

    if args.part == 1:
        output = solve_part1(filtered_lines)
    elif args.part == 2:
        output = solve_part2(filtered_lines)
    else:
        raise ValueError("Unknown part")

    print(output)
