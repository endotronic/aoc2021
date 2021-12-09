"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 2
"""

import argparse
from typing import List


def solve_part1(moves: List[str]) -> int:
    horizontal = depth = 0

    for move in moves:
        command, amount_str = move.strip().split()
        amount = int(amount_str)

        if command == "forward":
            horizontal += amount
        elif command == "up":
            depth -= amount
        elif command == "down":
            depth += amount
        else:
            raise ValueError("Unknown command")

    return horizontal * depth


def solve_part2(moves: List[str]) -> int:
    horizontal = depth = aim = 0

    for move in moves:
        command, amount_str = move.strip().split()
        amount = int(amount_str)

        if command == "forward":
            horizontal += amount
            depth += aim * amount
        elif command == "up":
            aim -= amount
        elif command == "down":
            aim += amount
        else:
            raise ValueError("Unknown command")

    return horizontal * depth


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 2")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem2.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        moves = file.readlines()

    if args.part == 1:
        output = solve_part1(moves)
    elif args.part == 2:
        output = solve_part2(moves)
    else:
        raise ValueError("Unknown part")

    print(output)
