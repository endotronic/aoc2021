"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 5
"""

import argparse
import attr
import re
from typing import List


def solve(input_lines: List[str], consider_diagonals: bool) -> int:
    lines = [Line.from_string(input_line) for input_line in input_lines]

    width = height = 0
    for line in lines:
        width = max(width, line.start.x, line.end.x)
        height = max(height, line.start.y, line.end.y)

    floor = OceanFloor(width=width + 1, height=height + 1)
    for line in lines:
        floor.add_line(line, consider_diagonals=consider_diagonals)

    return floor.get_num_overlaps()


@attr.s
class Point:
    x = attr.ib(type=int)
    y = attr.ib(type=int)


@attr.s
class Line:
    start = attr.ib(type=Point)
    end = attr.ib(type=Point)

    @property
    def is_horizontal(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_vertical(self) -> bool:
        return self.start.y == self.end.y

    @classmethod
    def from_string(cls, input_str: str) -> "Line":
        parsed = re.match("(\d+),(\d+) -> (\d+),(\d+)", input_str)
        if not parsed:
            raise ValueError("{} is not a valid line".format(input_str))

        parts = [int(v) for v in parsed.groups()]
        start = Point(x=parts[0], y=parts[1])
        end = Point(x=parts[2], y=parts[3])
        return Line(start, end)


class OceanFloor:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.matrix = [[0 for x in range(self.width)] for y in range(self.height)]

    def add_line(self, line: Line, consider_diagonals: bool) -> None:
        if line.is_horizontal:
            for y in range(
                min(line.start.y, line.end.y), max(line.start.y, line.end.y) + 1
            ):
                self.inc(line.start.x, y)
        elif line.is_vertical:
            for x in range(
                min(line.start.x, line.end.x), max(line.start.x, line.end.x) + 1
            ):
                self.inc(x, line.start.y)
        elif consider_diagonals:
            if abs(line.start.x - line.end.x) != abs(line.start.y - line.end.y):
                raise ValueError("Lines with slope other than 1 not supported")

            x_step = 1 if line.end.x > line.start.x else -1
            y_step = 1 if line.end.y > line.start.y else -1
            x = line.start.x
            y = line.start.y
            for _ in range(abs(line.start.x - line.end.x) + 1):
                self.inc(x, y)
                x += x_step
                y += y_step

    def get_num_overlaps(self) -> int:
        sum = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.value_at(x, y) > 1:
                    sum += 1

        return sum

    def value_at(self, x: int, y: int) -> int:
        return self.matrix[y][x]

    def inc(self, x: int, y: int) -> None:
        self.matrix[y][x] += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 5")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem5.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        filtered_lines = list(filter(lambda line: bool(line), lines))

    if args.part == 1:
        output = solve(filtered_lines, consider_diagonals=False)
    elif args.part == 2:
        output = solve(filtered_lines, consider_diagonals=True)
    else:
        raise ValueError("Unknown part")

    print(output)
