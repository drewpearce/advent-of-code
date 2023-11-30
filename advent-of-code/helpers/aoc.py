import os
import re

import requests

from helpers.utils import colored


AOC_SESSION = os.environ.get('AOC_SESSION', '')


def call_aoc_api(method, path, data=None):
    url = f'https://adventofcode.com/{path}'
    caller = getattr(requests, method)
    response = caller(
        url,
        headers={'Cookie': f'session={AOC_SESSION}'},
        data=data
    )

    if not response.ok:
        raise Exception(f'Calling {url} failed:\n{response.status_code}: '
                        f'{response.text}')

    return response.status_code, response.content


def get_input(year, day):
    code, content = call_aoc_api('get', f'{year}/day/{day}/input')

    return content.decode('utf-8')


def submit_answer(year, day, part, answer):
    print(colored(
        f'Submitting answer for {year} Day {day} Part {part}: {answer}',
        'cyan',
    ))
    code, content = call_aoc_api(
        'post',
        f'{year}/day/{day}/answer',
        data={'level': str(part), 'answer': str(answer)},
    )
    match = re.search(
        r'<article><p>(.*)</p></article>', content.decode('utf-8'))
    content = match.group(1) if match else 'Unable to determine response'

    if "That's the right answer" in content:
        print(colored('Correct!', 'green'))
    elif "That's not the right answer" in content:
        print(colored('Incorrect', 'red'))
    elif 'Did you already complete it' in content:
        print(colored('Already completed?', 'yellow'))
    elif 'You gave an answer too recently' in content:
        msg = re.search(r'You have .* left to wait.', content).group(0)
        print(colored(f'Too soon! {msg}', 'yellow'))
    else:
        print(colored(content, 'magenta'))
