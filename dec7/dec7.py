#!/usr/bin/env python

from re import match

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

def unique_keys(listx, listy):
    result = []
    for key in listx:
        if key not in listy:
           result.append(key)
    return result

processed = []

# build a dependency list
while True:
    keys = []
    key_deps = []
    dep_tree = {}
    for line in lines:
        matches = match('^Step (.) must be finished before step (.) can begin.$', line)
        dep, key = matches.groups()

        if key not in dep_tree.keys():
            dep_tree[key] = []

        if dep not in processed:
            dep_tree[key].append(dep)

        if dep not in processed:
            if key not in keys:
                keys.append(key)
            if dep not in key_deps:
                key_deps.append(dep)

    todo_keys = unique_keys(key_deps, keys)
    if not todo_keys:
        processed.append(unique_keys(list(dep_tree.keys()), processed)[0])
        break
    else:
        processed.append(sorted(todo_keys)[0])

# PART 1
print("".join(processed))
