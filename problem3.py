"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 3
"""

import argparse
from typing import List, Tuple


def solve(lines: List[str]) -> int:
    if not lines or not lines[0]:
        return ValueError("Missing input")

    sums = get_sums(lines)
    gamma, epsilon = get_gamma_and_epsilon(sums, len(lines))
    return gamma * epsilon


def get_sums(lines: List[str]) -> List[int]:
    sums = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for i, bit in enumerate(line):
            assert bit in ("0", "1")
            sums[i] += int(bit)

    return sums


def get_gamma_and_epsilon(sums: List[int], num_lines: int) -> Tuple[int, int]:
    half_of_num_lines = num_lines / 2
    gamma = epsilon = 0
    for bit_position, bits_sum in enumerate(sums):
        bit_rank = len(sums) - bit_position - 1
        bit_value = 2 ** bit_rank
        if bits_sum > half_of_num_lines:
            gamma |= bit_value
        elif bits_sum < half_of_num_lines:
            epsilon |= bit_value
        else:
            raise Exception(
                "Cannot determine most common bit in position {}".format(bit_position)
            )

    return gamma, epsilon


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 3")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem3.txt"
    )
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        filtered_lines = list(filter(lambda line: bool(line), lines))

    output = solve(lines)
    print(output)
