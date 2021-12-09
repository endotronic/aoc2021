"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 4
"""

import argparse
from typing import List


def solve_part1(lines: List[str]) -> int:
    calls = [int(val) for val in lines[0].strip().split(",")]
    boards = make_boards(lines)

    boards_that_won = []  # type: List[BingoBoard]
    for call in calls:
        for board in boards:
            board.call(call)
            if board.is_won():
                boards_that_won.append(board)

        if boards_that_won:
            if len(boards_that_won) > 1:
                raise Exception("Multiple boards won in one round")
            else:
                return boards_that_won[0].score() * call

    raise Exception("No boards won")


def solve_part2(lines: List[str]) -> int:
    calls = [int(val) for val in lines[0].strip().split(",")]
    boards = make_boards(lines)

    for call in calls:
        boards_to_remove = []  # type: List[BingoBoard]
        for board in boards:
            board.call(call)
            if board.is_won():
                boards_to_remove.append(board)

        for done_board in boards_to_remove:
            boards.remove(done_board)

        if len(boards) == 0:
            if len(boards_to_remove) == 1:
                return boards_to_remove[0].score() * call
            else:
                raise Exception("Boards won simultaneously")

    raise Exception("No boards won")


def make_boards(lines: List[str]) -> List["BingoBoard"]:
    assert len(lines) >= 7 and (len(lines) - 2) % 6 == 5

    boards = []  # type: List[BingoBoard]
    for n in range(2, len(lines), 6):
        boards.append(BingoBoard.from_strings(lines[n : n + 5]))

    return boards


class BingoBoard:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.called = [
            [False for x in range(self.width)] for y in range(self.height)
        ]  # type: List[List[bool]]

    @classmethod
    def from_strings(cls, lines: List[str]) -> "BingoBoard":
        assert len(lines) == 5
        matrix = [[int(val) for val in line.strip().split()] for line in lines]
        return cls(matrix)

    def call(self, value: int) -> None:
        for y in range(self.height):
            for x in range(self.width):
                if self.value_at(x, y) == value:
                    self.called[y][x] = True

    def is_won(self) -> bool:
        for row in range(self.height):
            if all(self.get_row_state(row)):
                return True
        for col in range(self.width):
            if all(self.get_column_state(col)):
                return True
        return False

    def score(self) -> int:
        sum = 0
        for y in range(self.height):
            for x in range(self.width):
                if not self.is_called_at(x, y):
                    sum += self.value_at(x, y)
        return sum

    def value_at(self, x: int, y: int) -> int:
        return self.matrix[y][x]

    def is_called_at(self, x: int, y: int) -> bool:
        return self.called[y][x]

    def get_row_state(self, row: int) -> List[bool]:
        return self.called[row]

    def get_column_state(self, col: int) -> List[bool]:
        return [self.is_called_at(col, row) for row in range(self.height)]

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 4")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem4.txt"
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
