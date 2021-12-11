"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 8
"""

import argparse
from itertools import permutations
from typing import List, Mapping, Optional

segments_to_dec = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def solve_part1(lines: List[str]) -> int:
    occurrences = 0
    for line in lines:
        _, outputs_str = line.split("|")
        outputs = outputs_str.strip().split()
        for o in outputs:
            if len(o) in (2, 4, 3, 7):
                occurrences += 1

    return occurrences


def solve_part2(lines: List[str]) -> int:
    total = 0
    for line in lines:
        inputs_str, outputs_str = line.split("|")
        mapping = find_mapping(inputs_str.strip().split())
        total += get_value(outputs_str.strip().split(), mapping)

    return total


def find_mapping(inputs: List[str]) -> Mapping[str, str]:
    mappings = [
        dict(p)
        for p in list(
            tuple(zip(p, ("a", "b", "c", "d", "e", "f", "g")))
            for p in permutations("abcdefg")
        )
    ]
    for mapping in mappings:
        if all([get_digit(input, mapping) is not None for input in inputs]):
            return mapping

    raise Exception("No mapping makes sense")


def get_digit(input: str, mapping: Mapping[str, str]) -> Optional[int]:
    transformed = [mapping[c] for c in input]
    transformed.sort()  # alphabetize
    return segments_to_dec.get("".join(transformed))


def mapping_to_str(mapping: Mapping[str, str]) -> str:
    inv_map = dict(zip(mapping.values(), mapping.keys()))
    return "".join([inv_map[c] for c in "abcdefg"])


def get_value(outputs: List[str], mapping: Mapping[str, str]) -> int:
    value = 0
    for i, output in enumerate(outputs):
        place = len(outputs) - i - 1
        digit = get_digit(output, mapping)
        value += digit * (10 ** place)

    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 8")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem8.txt"
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
