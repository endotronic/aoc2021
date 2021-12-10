"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 7
"""

import argparse


def solve(input: str, part: int) -> int:
    crabs = [int(v) for v in input.split(",")]
    max_pos = max(crabs)
    histogram = [0 for _ in range(max_pos + 1)]
    for c in crabs:
        histogram[c] += 1

    costs = [0 for _ in range(max_pos + 1)]
    for i in range(max_pos + 1):
        for pos in range(max_pos + 1):
            costs[i] += histogram[pos] * cost(pos, i, part)
    return min(costs)


def cost(start_pos: int, end_pos: int, part: int) -> int:
    if part == 1:
        return abs(start_pos - end_pos)
    elif part == 2:
        # Memoizing this would help a lot
        return sum(range(abs(start_pos - end_pos) + 1))
    raise ValueError("Unknown part")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 7")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem7.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        input = file.readline().strip()

    output = solve(input, part=args.part)
    print(output)
