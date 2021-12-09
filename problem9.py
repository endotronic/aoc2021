"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 9
"""

import argparse
from typing import List


def solve_part1(line: List[str]) -> int:
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 9")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem9.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        moves = file.readlines()

    if args.part == 1:
        output = solve_part1(moves)
    else:
        raise ValueError("Unknown part")

    print(output)
