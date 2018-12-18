#!/usr/bin/env python

from pprint import pprint
from copy import deepcopy

# parse input
area = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        area.append([char for char in line.rstrip()])


def count_surrounding(area, acres, y, x, char):
    count = 0
    ystart, yend = y, y
    xstart, xend = x, x

    if y != 0:
        ystart = y -1
    if y != len(area) -1:
        yend = y + 1
    if x != 0:
        xstart = x -1
    if x != len(acres) -1:
        xend = x + 1

    for yi in range(ystart, yend + 1):
        for xi in range(xstart, xend + 1):
            if y == yi and x == xi:
                continue
            if area[yi][xi] == char:
                count += 1

    return count


def print_area(area):
    for line in area:
        print("".join(line))
    print("")

end_area = deepcopy(area)
for i in range(10):
    for y, acres in enumerate(area):
        for x, acre in enumerate(acres):
            if acre == '|':  # trees
                if count_surrounding(area, acres, y, x, '#') > 2:
                    end_area[y][x] = '#'
            elif acre == '#':  # lumberyard
                if count_surrounding(area, acres, y, x, '#') > 0 \
                and count_surrounding(area, acres, y, x, '|') > 0:
                    end_area[y][x] = '#'
                else:
                    end_area[y][x] = '.'
            else:  # open
                if count_surrounding(area, acres, y, x, '|') > 2:
                    end_area[y][x] = '|'
    area = deepcopy(end_area)

lumberyards = 0
woodedacres = 0

for acres in area:
    for acre in acres:
        if acre == '#':
            lumberyards += 1
        if acre == '|':
            woodedacres += 1

result = lumberyards * woodedacres
print(result)

