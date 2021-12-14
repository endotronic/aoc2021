"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 13
"""

import argparse
import re
from typing import List, Tuple


def solve(lines: List[str], part: int) -> int:
    width = 0
    height = 0
    coords = []  # type: List[Tuple[int, int]]
    for i, line in enumerate(lines):
        if not line:
            break
        x, y = line.strip().split(",")
        coords.append((int(x), int(y)))

        if int(x) >= width:
            width = int(x) + 1
        if int(y) >= height:
            height = int(y) + 1

    index_of_folds = i + 1
    for i in range(index_of_folds, len(lines)):
        parser = re.match("fold along (x|y)=(\d+)", lines[i])
        if not parser:
            raise Exception("Bad input")

        axis = parser.groups()[0]
        fold_over_val = int(parser.groups()[1])
        if axis == "x":
            width = fold_over_val
            for ci, (cx, cy) in enumerate(coords):
                if cx > fold_over_val:
                    coords[ci] = (fold_over_val - (cx - fold_over_val), cy)
        if axis == "y":
            height = fold_over_val
            for ci, (cx, cy) in enumerate(coords):
                if cy > fold_over_val:
                    coords[ci] = (cx, fold_over_val - (cy - fold_over_val))
        if part == 1:
            break

    uniq_coords = set()
    for cx, cy in coords:
        uniq_coords.add((cx, cy))

    for cy in range(height):
        line = ""
        for cx in range(width):
            if (cx, cy) in uniq_coords:
                line += "#"
            else:
                line += "."
        print(line)

    return len(uniq_coords)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 13")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem13.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    output = solve(lines, part=args.part)
    print(output)
