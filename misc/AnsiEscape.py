#!/usr/bin/env python
# -*- coding:utf-8 -*-


class AnsiEscape(object):

    """Tool for Ansi Escape Codes
    refer:
    http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
    https://en.wikipedia.org/wiki/ANSI_escape_code
    """

    # color names to indices
    # 8-color, most computer and terminal support this
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    effect_map = {
        'default': '0',
        'highlight': '1',
        'underline': '4',
        'blink': '5',
        'inverse': '7',
        'invisible': '8'
    }

    csi = '\u001b['
    reset = '\u001b[0m'

    # cursor move
    # n means how many pos
    cursor = {
        'up': '\u001b[%dA',
        'down': '\u001b[%dB',
        'right': '\u001b[%dC',
        'left': '\u001b[%dD',
        # down %d line and move to beginnging of line
        'downLine': '\u001b[%dE',
        # up %d line and move to beginnging of line
        'upLine': '\u001b[%dF',
        # set cur to row %d
        'row': '\u001b[%dG',
        # set cur to row %d col %d
        'set': '\u001b[%d;%dH',
        # save cur position
        'save': '\u001b[s',
        # load cur position
        'load': '\u001b[u',
    }

    def __init__(self):
        super(AnsiEscape, self).__init__()

    @classmethod
    def colorize(cls, message, fg=None, bg=None, effect=None):
        params = []
        if fg in cls.color_map:
            params.append(str(cls.color_map[fg] + 30))
        elif isinstance(fg, int):
            params.append(str(fg))
        if bg in cls.color_map:
            params.append(str(cls.color_map[bg] + 40))
        elif isinstance(bg, int):
            params.append(str(bg))
        if effect in cls.effect_map:
            params.append(cls.effect_map[effect])
        elif isinstance(effect, int):
            params.append(str(effect))
        message = ''.join([
            cls.csi,
            ';'.join(params),
            'm', message,
            cls.reset
        ])
        return message

    @classmethod
    def color256(cls, message, color):
        '''
        256-color, not all terminal support this
        color should be 0 to 255
        '''
        params = ['38', '5', str(color)]
        message = ''.join([
            cls.csi,
            ';'.join(params),
            'm', message,
            cls.reset
        ])
        return message

    @classmethod
    def color256bg(cls, message, color):
        '''
        256-color background, not all terminal support this
        color should be 0 to 255
        '''
        params = ['48', '5', str(color)]
        message = ''.join([
            cls.csi,
            ';'.join(params),
            'm', message,
            cls.reset
        ])
        return message

    @classmethod
    def moveCursor(cls, action, pos=0, row=0, col=0):
        if action == 'set':
            return cls.cursor[action] % (row, col)
        elif action in ['save', 'load']:
            return cls.cursor[action]
        else:
            return cls.cursor[action] % pos


def _testBase():
    C = AnsiEscape.colorize
    print(C('red', 'red'))
    print(C('green', 'green'))
    print(C('yellow', 'yellow'))
    print(C('blue', 'blue'))
    print(C('magenta', 'magenta'))
    print(C('cyan', 'cyan'))
    print(C('white', 'white'))


def _testEffect():
    C = AnsiEscape.colorize
    print(C('red;blue', 'red', 'blue'))
    print(C('red;highlight', 'red', None, 'highlight'))
    print(C('green;underline', 'green', None, 'underline'))
    print(C('yellow;invisible', 'yellow', None, 'invisible'))


def _test256():
    for i in range(256):
        print(AnsiEscape.color256(str(i), i), end='\t')
    for i in range(256):
        print(AnsiEscape.color256bg(str(i), i), end='\t')


def _testCursor():
    import time
    import random
    lines = [0, 0, 0, 0]
    for i in range(5):
        for j in range(4):
            k = lines[j]
            k += random.randint(2, 10)
            print(AnsiEscape.moveCursor('left', 100), end='', flush=True)
            print('#' * k + '\t' + str(k) + '%', flush=True)
            lines[j] = k
            time.sleep(0.1)
        if i != 4:
            print(AnsiEscape.moveCursor('up', 4), end='', flush=True)


def _testCursor2():
    import time
    import random
    lines = [0, 0, 0, 0]
    for i in range(5):
        for j in range(4):
            k = random.randint(1, 50)
            print(AnsiEscape.moveCursor('row', k), end='', flush=True)
            print('#' * k + '\t' + str(k) + '%', flush=True)
            time.sleep(0.1)
        print(AnsiEscape.moveCursor('upLine', 4), end='', flush=True)


def _testCursor3():
    import time
    import random
    for i in range(4):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        z = random.randint(1, 100)
        print(AnsiEscape.moveCursor('set', row=x, col=y), end='', flush=True)
        print('#' * z + '\t' + str(z) + '%', end='', flush=True)
        time.sleep(0.5)

def _testCursor4():
    print(AnsiEscape.moveCursor('save'), end='', flush=True)
    for i in range(10):
        print('...')
    print(AnsiEscape.moveCursor('load'), end='', flush=True)
    print('...')


if __name__ == '__main__':
    _test256()
