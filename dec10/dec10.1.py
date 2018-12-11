#!/usr/bin/env python

import re
from terminalplot import plot
from time import sleep

# parse points input
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

values=[]
for line in lines:
    # [[(x, y), (xv, yv)], ... ]
    matches = re.findall("<\s*(-?\d+),\s*(-?\d+)>", line)
    values.append([int(i) for sub in matches for i in sub])

def draw_state(values):
    xs, ys = [], []
    for value in values:
        xs.append(value[0])
        ys.append(value[1])

    if max(ys) == 128:
        plot(xs, ys)
        sleep(5)

def advance_state(values):
    for value in values:
        value[0] = value[0] + value[2]
        value[1] = value[1] + value[3]
    return values

# draw output per second
while True:
    draw_state(values)
    values = advance_state(values)
