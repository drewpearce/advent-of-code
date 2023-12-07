#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import date
from importlib import import_module
import os
import sys

from helpers.aoc import get_input
from helpers.aoc import submit_answer


DEF_YEAR = date.today().year
DEF_DAY = date.today().day


def get_args():
    parser = ArgumentParser(
        prog='run',
        description='Run a solution for a challenge.',
    )
    parser.add_argument(
        '-y',
        '--year',
        type=int,
        help='The challenge year',
        default=DEF_YEAR,
        choices=list(range(2015, DEF_YEAR + 1)),
    )
    parser.add_argument(
        '-d',
        '--day',
        type=int,
        help='The challenge day',
        default=DEF_DAY,
        choices=list(range(1, 26)),
    )
    parser.add_argument(
        '-p',
        '--part',
        type=int,
        help='The challenge part to submit',
        default=1,
        choices=[1, 2],
    )

    return parser.parse_args()


def get_day_module(year, day):
    day_name = f'0{day}' if day < 10 else str(day)
    sys.path.insert(
        0,
        os.path.abspath(os.path.join(
            os.path.dirname(__file__),
            '..',
            str(year),
        )),
    )

    return import_module(f'day_{day_name}')


def main():
    args = get_args()
    day = get_day_module(args.year, args.day)
    runner = getattr(day, f'part_{args.part}')
    answer = runner(get_input(args.year, args.day))
    submit_answer(args.year, args.day, args.part, answer)


if __name__ == '__main__':
    main()
