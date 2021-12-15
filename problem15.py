"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 15
"""

import argparse
from heapq import heappop, heappush
from typing import Dict, List, Set, Tuple


def solve_part1(lines: List[str]) -> int:
    cavern = Cavern.from_string(lines)
    return cavern.dijkstra()


def solve_part2(lines: List[str]) -> int:
    cavern = Cavern.from_string(lines)
    cavern.add_part_2()
    return cavern.dijkstra()


class Cavern:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    @classmethod
    def from_string(cls, lines: List[str]) -> "Cavern":
        return cls([[int(val) for val in line] for line in lines])

    def add_part_2(self) -> None:
        new_matrix = [
            [
                (
                    self.get_risk_at(x % self.width, y % self.height)
                    + int(x / self.width)
                    + int(y / self.height)
                )
                for x in range(self.width * 5)
            ]
            for y in range(self.height * 5)
        ]

        for y in range(len(new_matrix)):
            for x in range(len(new_matrix[0])):
                if new_matrix[y][x] > 9:
                    new_matrix[y][x] -= 9

        self.matrix = new_matrix

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

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)

    def get_risk_at(self, x: int, y: int) -> int:
        return self.matrix[y][x]

    def dijkstra(self) -> int:
        risks = dict()  # type: Dict[Tuple[int, int], int]
        visited = set()  # type: Set[Tuple[int, int]]
        min_risk = [(0, (0, 0))]
        while min_risk:
            cur_risk, (x, y) = heappop(min_risk)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for nx, ny in self.get_neighbors_at(x, y):
                risk = cur_risk + self.get_risk_at(nx, ny)
                if (nx, ny) not in risks or risk < risks[(nx, ny)]:
                    risks[(nx, ny)] = risk
                    heappush(min_risk, (risk, (nx, ny)))

        return risks[(self.width - 1, self.height - 1)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 15")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem15.txt"
    )
    parser.add_argument("part", help="part (1|2)", type=int)
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    if args.part == 1:
        output = solve_part1(lines)
    elif args.part == 2:
        output = solve_part2(lines)
    else:
        raise ValueError("Unknown part")

    print(output)
