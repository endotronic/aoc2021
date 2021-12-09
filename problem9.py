"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 9
"""

import argparse
from math import prod
from typing import List, Set, Tuple


def solve_part1(lines: List[str]) -> int:
    cave = Cave([[int(val) for val in line] for line in lines])
    low_points = cave.get_low_points()
    return sum([cave.risk_level_at(x, y) for (x, y) in low_points])


def solve_part2(lines: List[str]) -> int:
    cave = Cave([[int(val) for val in line] for line in lines])
    low_points = cave.get_low_points()
    basin_sizes = [cave.get_basin_size_at(x, y) for (x, y) in low_points]
    basin_sizes.sort(reverse=True)
    return prod(basin_sizes[0:3])


class Cave:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def get_low_points(self) -> List[Tuple[int, int]]:
        low_points = []  # type: List[Tuple[int, int]]
        for y in range(self.height):
            for x in range(self.width):
                if self.is_low_point(x, y):
                    low_points.append((x, y))

        return low_points

    def get_basin_size_at(self, x: int, y: int) -> int:
        checked_points = set()  # type: Set[Tuple[int, int]]
        points_to_check = {(x, y)}

        while len(points_to_check) > 0:
            x, y = points_to_check.pop()
            checked_points.add((x, y))
            neighbors = self.get_open_neighbors_at(x, y)
            for nx, ny in neighbors:
                if (nx, ny) not in checked_points:
                    points_to_check.add((nx, ny))

        return len(checked_points)

    def get_neighbors_at(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = []  # type: List[Tuple[int, int]]
        if x > 0:
            neighbors.append((x - 1, y))
        if x < self.width - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < self.height - 1:
            neighbors.append((x, y + 1))

        return neighbors

    def get_open_neighbors_at(self, x: int, y: int) -> List[Tuple[int, int]]:
        return [
            (nx, ny)
            for (nx, ny) in self.get_neighbors_at(x, y)
            if self.value_at(nx, ny) != 9
        ]

    def get_neighbor_values(self, x: int, y: int) -> List[int]:
        return [self.value_at(nx, ny) for (nx, ny) in self.get_neighbors_at(x, y)]

    def is_low_point(self, x: int, y: int) -> bool:
        return min(self.get_neighbor_values(x, y)) > self.value_at(x, y)

    def value_at(self, x: int, y: int) -> int:
        return self.matrix[y][x]

    def risk_level_at(self, x: int, y: int) -> int:
        return 1 + self.value_at(x, y)

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 9")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem9.txt"
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
