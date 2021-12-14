"""
ADVENT OF CODE 2021
Contestant: Kevin Wood
Problem: 12
"""

import argparse
import attr
from collections import OrderedDict
from typing import Any, Dict, List, Set


@attr.s(eq=False)
class Node:
    name = attr.ib(type=str)
    is_small = attr.ib(type=bool)
    connections = attr.ib(type=Set["Node"])


def solve_part1(lines: List[str]) -> int:
    nodes_by_name = parse_input(lines)

    # Traverse
    start = nodes_by_name["start"]
    ongoing_paths = [[start]]  # type: List[List[Node]]
    finished_paths = []  # type: List[List[Node]]

    while ongoing_paths:
        cur_path = ongoing_paths.pop()
        last_node = cur_path[-1]
        for conn in last_node.connections:
            if not conn.is_small or conn not in cur_path:
                new_path = cur_path + [conn]
                if conn.name == "end":
                    finished_paths.append(new_path)
                else:
                    ongoing_paths.append(new_path)

    return len(finished_paths)


def solve_part2(lines: List[str]) -> int:
    nodes_by_name = parse_input(lines)

    # Traverse
    start = nodes_by_name["start"]
    ongoing_paths = [[start]]  # type: List[List[Node]]
    finished_paths = []  # type: List[List[Node]]

    while ongoing_paths:
        cur_path = ongoing_paths.pop()
        last_node = cur_path[-1]
        for conn in last_node.connections:
            if not conn.is_small or small_is_ok(cur_path, conn):
                new_path = cur_path + [conn]
                if conn.name == "end":
                    finished_paths.append(new_path)
                else:
                    ongoing_paths.append(new_path)

    results = set([",".join([n.name for n in path]) for path in finished_paths])
    return len(results)


def parse_input(lines: List[str]) -> Dict[str, Node]:
    nodes_by_name = dict()  # type: Dict[str, Node]
    for line in lines:
        a, b = line.split("-")
        if a not in nodes_by_name:
            is_small = a.lower() == a
            nodes_by_name[a] = Node(name=a, is_small=is_small, connections=set())
        if b not in nodes_by_name:
            is_small = b.lower() == b
            nodes_by_name[b] = Node(name=b, is_small=is_small, connections=set())

        # Connections both ways - graph is not directed
        nodes_by_name[a].connections.add(nodes_by_name[b])
        nodes_by_name[b].connections.add(nodes_by_name[a])

    # Validation
    assert "start" in nodes_by_name
    assert "end" in nodes_by_name
    return nodes_by_name


def small_is_ok(cur_path: List[Node], conn: Node) -> bool:
    if conn.name == "start":
        return False

    if conn not in cur_path:
        return True

    visited_smalls = [node for node in cur_path if node.is_small]
    if len(set(visited_smalls)) == len(visited_smalls):
        return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code 2021, problem 12")
    parser.add_argument(
        "-i", "--input_file", help="path to input file", default="input/problem12.txt"
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
