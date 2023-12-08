from math import prod
from math import sqrt
import re

from sympy import solve
from sympy import symbols

from helpers.aoc import get_input


def parse_data(data):
    lines = data.splitlines()
    races = zip(
        [int(d) for d in re.findall(r'\d+', lines[0])],
        [int(d) for d in re.findall(r'\d+', lines[1])]
    )

    return races


def determine_winning(race_time, target_distance):
    x = symbols('x')
    expr = x * (race_time - x) > target_distance
    charge_times = solve(expr)

    for arg in charge_times.args:
        expr = str(arg)
        
        if expr.startswith('x'):
            end = int(eval(expr.split(' < ')[1]))
        else:
            start = eval(expr.split(' < ')[0])
            start = start + 1 if isinstance(start, int) else int(start)

    return range(start, end)


def part_1(_in):
    races = parse_data(_in)
    winning = [determine_winning(*r) for r in races]

    return prod([len(w) for w in winning])


def part_2(_in):
    lines = _in.splitlines()
    _range = determine_winning(
        int(lines[0].replace('Time:', '').replace(' ', '')),
        int(lines[1].replace('Distance:', '').replace(' ', '')),
    )
    return len(_range)


def main():
    _in = get_input(2023, 6)
    print(part_1(_in))
    print(part_2(_in))


if __name__ == '__main__':
    main()
