#!/usr/bin/env python

from argparse import ArgumentParser
from datetime import date
import os

from helpers.utils import colored


DEF_YEAR = date.today().year
DEF_DAY = date.today().day
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def get_args():
    parser = ArgumentParser(
        prog='scaffold-day',
        description="Setup an Advent of Code work file for a day's challenge",
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

    return parser.parse_args()


def create_dir(year):
    year_dir = os.path.join(BASE_DIR, str(year))
    if not os.path.isdir(year_dir):
        os.mkdir(year_dir)

    return year_dir


def create_file(path, year, day):
    day_name = f'0{day}' if day < 10 else str(day)
    day_path = os.path.join(path, f'day_{day_name}.py')

    if os.path.isfile(day_path):
        print(colored(f'Already Exists:\n{day_path}', 'yellow'))
    else:
        with open(os.path.join(BASE_DIR, 'tools', 'scaffold.txt')) as f:
            template = f.read()

        data = template.replace(
            '{{year}}', str(year)).replace('{{day}}', str(day))

        with open(day_path, 'w') as f:
            f.write(data)
        
        print(colored(f'Successfully scaffolded:\n{day_path}', 'green'))


def main():
    args = get_args()
    year_dir = create_dir(args.year)
    create_file(year_dir, args.year, args.day)


if __name__ == '__main__':
    main()