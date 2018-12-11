#!/usr/bin/env python

import re

serial = 4172 # input
#serial = 42 # sample 

def getPower(x, y):
    # default algo
    rackid = x + 10
    p = (float(rackid * y) + serial) * rackid / 100

    # grab 100's
    p = re.match("(-)?[^\.]*([0-9])\.", str(p)).groups()

    # handle negative numbers
    if p[0]:
        p = int("".join(p))
    else:
        p = int(p[1])

    return p - 5


grid = []
for x in range(1,301):
    for y in range(1,301):
        p = getPower(x, y)
        grid.append([x, y, p])

highest = []
index = 1
for cella in grid:
     if index > 100:
         index = 1

     if cella[0] + 3 <= 300 and cella[1] + 3 <= 300:
        tp = cella[2]
        otp = cella[2]
        for xs in range(3):
            tmpx = cella[0] + xs
            for ys in range(3):
                tmpy = cella[1] + ys
                for cellb in grid:
                    if cellb[0] == tmpx and cellb[1] == tmpy:
                        tp = tp + cellb[2]
        tp = tp - otp
        if not highest or highest[2] < p:
            print("higher value found: ", [cella[0], cella[1], tp])
            highest = [cella[0], cella[1], tp]

     index = index + 1
     if index == 100:
         print("currently processed: ", [cella[0], cella[1], tp])

print(highest)
