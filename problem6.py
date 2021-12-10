"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 6
"""

import argparse
from typing import List

MAX_FISH_COUNTER = 9


def solve(initial_state: str, num_days: int) -> int:
    num_fish_by_day = [0 for _ in range(MAX_FISH_COUNTER)]
    for days in [int(f) for f in initial_state.split(",")]:
        num_fish_by_day[days] += 1

    for _ in range(num_days):
        cycled_count = num_fish_by_day[0]
        num_fish_by_day = num_fish_by_day[1:MAX_FISH_COUNTER] + [0]
        num_fish_by_day[6] += cycled_count
        num_fish_by_day[8] += cycled_count

    return sum(num_fish_by_day)


def rotate_array(arr: List[int]) -> List[int]:
    if not arr:
        return []
    n = len(arr)
    return arr[1:n] + [arr[0]]


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
