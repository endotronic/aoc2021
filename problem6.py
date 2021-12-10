"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 6
"""

import argparse
from typing import List


def solve(initial_state: str, num_days: int) -> int:
    fish = [int(f) for f in initial_state.split(",")]
    for _ in range(num_days):
        num_fish = len(fish)
        for i in range(num_fish):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                fish.append(8)

    return len(fish)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 6")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem6.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        input = file.readline().strip()

    if args.part == 1:
        output = solve(input, num_days=80)
    elif args.part == 2:
        output = solve(input, num_days=256)
    else:
        raise ValueError("Unknown part")

    print(output)
