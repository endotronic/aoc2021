"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 1
"""

import argparse
from typing import List


def solve(depths: List[int], window_size: int = 1) -> int:
    num_increasing = 0

    for i in range(len(depths) - window_size):
        prev = sum(depths[i : i + window_size])
        curr = sum(depths[i + 1 : i + window_size + 1])
        if curr > prev:
            num_increasing += 1

    return num_increasing


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 1")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem1.txt"
    )
    parser.add_argument(
        "-w", "--window_size", help="sliding window size", type=int, default=1
    )
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        depths = [int(line) for line in file.readlines()]

    output = solve(depths, window_size=args.window_size)
    print(output)
