"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 11
"""

import argparse
from typing import List, Set, Tuple


def solve_part1(lines: List[str], steps: int = 100) -> int:
    board = OctopusMatrix.from_string(lines)
    for _ in range(steps):
        board.step()
    return board.total_flashes


def solve_part2(lines: List[str]) -> int:
    board = OctopusMatrix.from_string(lines)
    steps = 0
    while not board.is_synced():
        board.step()
        steps += 1

    return steps


class OctopusMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.total_flashes = 0
        self.flashed_coordinates = set()  # type: Set[Tuple[int, int]]

    @classmethod
    def from_string(cls, lines: List[str]) -> "OctopusMatrix":
        return cls([[int(val) for val in line] for line in lines])

    def step(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.inc(x, y)

        self.flashed_coordinates = set()
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] > 9:
                    self.matrix[y][x] = 0

    def inc(self, x: int, y: int) -> None:
        self.matrix[y][x] += 1
        if self.matrix[y][x] > 9 and (x, y) not in self.flashed_coordinates:
            self.flashed_coordinates.add((x, y))
            self.total_flashes += 1

            for nx, ny in self.get_neighbors_at(x, y):
                self.inc(nx, ny)

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
        if x > 0 and y > 0:
            neighbors.append((x - 1, y - 1))
        if x < self.width - 1 and y > 0:
            neighbors.append((x + 1, y - 1))
        if x > 0 and y < self.height - 1:
            neighbors.append((x - 1, y + 1))
        if x < self.width - 1 and y < self.height - 1:
            neighbors.append((x + 1, y + 1))

        return neighbors

    def is_synced(self) -> int:
        v = self.matrix[0][0]
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] != v:
                    return False

        return True

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 11")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem11.txt"
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
