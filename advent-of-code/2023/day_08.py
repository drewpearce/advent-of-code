from collections import deque
from copy import copy
from functools import reduce
from math import lcm
import re

from helpers.aoc import get_input


def parse_data(data):
    lines = data.splitlines()
    _map = deque([0 if c == 'L' else 1 for c in data.splitlines()[0]])
    nodes = {
        f[0]: f[1:]
        for f in re.findall(r'(\w+) = \((\w+), (\w+)\)', data)
    }

    return _map, nodes


def traverse(pos, nodes, _map, part):
    counter = 0

    if part == 1:
        while pos != 'ZZZ':
            pos = nodes[pos][_map[0]]
            _map.rotate(-1)
            counter += 1
    elif part == 2:
        while pos[-1] != 'Z':
            pos = nodes[pos][_map[0]]
            _map.rotate(-1)
            counter += 1

    return counter


def part_1(_in):
    _map, nodes = parse_data(_in)
    
    return traverse('AAA', nodes, copy(_map), 1)


def part_2(_in):
    _map, nodes = parse_data(_in)
    courses = [
        traverse(key, nodes, copy(_map), 2)
        for key in nodes.keys()
        if key[-1] == 'A'
    ]

    return reduce(lcm, courses)


def main():
    _in = get_input(2023, 8)
    print(part_1(_in))
    print(part_2(_in))


if __name__ == '__main__':
    main()
