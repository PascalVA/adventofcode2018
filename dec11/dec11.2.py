#!/usr/bin/env python

import re

serial = 4172 # input
#serial = 57 # sample 

def getPower(x, y):
    rackid = x + 10
    p = (rackid * y + serial) * rackid / 100 % 10 - 5
    return p

grid = {}
for x in range(1,301):
    for y in range(1,301):
        p = getPower(x, y)
        cell = "%d,%d" % (x, y)
        grid[cell] = p


highest = []
for cell, power in grid.items():
     x, y = cell.split(",")
     x, y = int(x), int(y)
     cellp = int(power)

     for size in range(1,301):
         tp = 0
         if size > 1:
             if x + size <= 300 and y + size <= 300:
               for xs in range(x, x + size):
                   searchkey = "%d,%d" % (xs, y)
                   tp += grid[searchkey]
               for ys in range(y, y + size):
                   searchkey = "%d,%d" % (x, ys)
                   tp += grid[searchkey]
    
               if not highest or highest[3] < tp:
                   highest = [x, y, size, tp]
                   print(highest)

print(highest)
