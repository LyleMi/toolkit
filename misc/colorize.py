#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Tool for colorize output
'''

# color names to indices
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

# levels to (background, foreground, bold/intense)
cyan = (None, 'cyan', None)
green = (None, 'green', None)
yellow = (None, 'yellow', None)
red = (None, 'red', None)

csi = '\x1b['
reset = '\x1b[0m'


def colorize(message, color):

    if color == 'cyan':
        color = cyan
    elif color == 'green':
        color = green
    elif color == 'red':
        color = red
    elif color == 'yellow':
        color = yellow
    else:
        return message

    bg, fg, effect = color
    params = []
    if bg in color_map:
        params.append(str(color_map[bg] + 40))

    if fg in color_map:
        params.append(str(color_map[fg] + 30))

    if effect in effect_map:
        params.append(effect_map[effect])

    message = ''.join([csi, ';'.join(params), 'm', message, reset])

    return message


if __name__ == '__main__':
    print colorize('test', 'cyan')
    print colorize('test', 'green')
    print colorize('test', 'red')
    print colorize('test', 'yellow')
