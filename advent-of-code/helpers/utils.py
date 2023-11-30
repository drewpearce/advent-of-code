ANSI_COLORS = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
]


def colored(text, color):
    if color is None:
        return text

    code = ANSI_COLORS.index(color.casefold())
    reset = '\x1b[0m'
    
    return f'\x1b[{code + 30}m{text}{reset}'
