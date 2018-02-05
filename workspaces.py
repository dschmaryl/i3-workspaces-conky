#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from json import loads
from subprocess import check_output


# use hex codes here or the color variables from conkyrc
COLOR_FOCUSED = 'color8'
COLOR_UNFOCUSED = 'color4'
COLOR_INVISIBLE = 'color1'

COMMAND = 'i3-msg -t get_workspaces'

spaces = loads(check_output(COMMAND.split()).decode('utf-8'))
active_spaces = {space['num']: space['focused'] for space in spaces}
output = []

for i in range(1, 11):
    workspace_num = '0' if i == 10 else str(i)
    try:
        color = COLOR_FOCUSED if active_spaces[i] else COLOR_UNFOCUSED
        output.append('${' + color + '}' + workspace_num)
    except KeyError:
        output.append('${' + COLOR_INVISIBLE + '}' + workspace_num)

print(' '.join(output))
