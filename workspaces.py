#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import loads
from subprocess import check_output


# use hex codes or the color variables from conkyrc
COLOR_FOCUSED = 'color8'
COLOR_UNFOCUSED = 'color4'
COLOR_INVISIBLE = 'color1'

WORKSPACES_COMMAND = 'i3-msg -t get_workspaces'


def get_visible_workspaces():
    # returns a dict pairing the visible workspaces with the focused state of
    # each of these workspaces
    visible_spaces = loads(check_output(WORKSPACES_COMMAND.split()))
    return {space['num']: space['focused'] for space in visible_spaces}


def format_for_conky(visible_spaces):
    # formats to a single line of workspace numbers with different colors to
    # denote focused/unfocused/invisible states
    output = []
    for i in range(1, 11):
        try:
            color = COLOR_FOCUSED if visible_spaces[i] else COLOR_UNFOCUSED
            output.append('${%s}%i' % (color, i))
        except KeyError:
            output.append('${%s}%i' % (COLOR_INVISIBLE, i))
    return ' '.join(output)


if __name__ == '__main__':
    print(format_for_conky(get_visible_workspaces()))
