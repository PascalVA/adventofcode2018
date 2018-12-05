#!/usr/bin/python

with open("input.txt", "r") as f:
    polymer = f.readlines()[0].rstrip()

#polymer = "dabAcCaCBAcCcaDA"

def str_remove_indexes(polymer, indexes):
    lst = list(polymer)
    indexes = sorted(indexes)
    offset = 0
    for i in indexes:
        del(lst[i-offset])
        offset += 1
    return "".join(lst)

def solve(polymer):
    found = 1
    while found == 1:
        found = 0
        for i, c in enumerate(polymer):
            if i != 0:
                if polymer[i].lower() == polymer[i-1].lower() and polymer[i] != polymer[i-1]:
                    polymer = str_remove_indexes(polymer, [i-1, i])
                    found = 1
                    break

            if i != len(polymer)-1:
                if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
                    polymer = str_remove_indexes(polymer, [i, i+1])
                    found = 1
                    break
    return len(polymer)

# PART 1
print("PART 1: %d" % (solve(polymer,)))

# PART 2
lengths = []
chars = set(polymer.lower())
for char in chars:
    polymer_redacted = polymer.replace(char, "").replace(char.upper(), "")
    lengths.append(solve(polymer_redacted))

print("PART 2: %d" % (min(lengths),))
