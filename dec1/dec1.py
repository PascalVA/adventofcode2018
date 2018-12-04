#!/usr/bin/env python

dup = False
freq = 0
seen = []

with open("input.txt", "r") as f:
    inList = f.read().splitlines()

while not dup:
    for item in inList:
        freq = freq + int(item)
        if freq in seen:
            dup = freq
            break
        seen.append(freq)

print("PART 1: %d" % dupl)

print("PART 2: %d" % reduce(lambda x, y: int(x) + int(y), inList))
