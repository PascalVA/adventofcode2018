#!/usr/bin/env python

import re

# instruction set
def addr(r, a, b, c):
    r[c] = r[a] + r[b]

def addi(r, a, b, c):
    r[c] = r[a] + int(b)

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]

def muli(r, a, b, c):
    r[c] = r[a] * int(b)

def banr(r, a, b, c):
    r[c] = r[a] & r[b]

def bani(r, a, b, c):
    r[c] = r[a] & int(b)

def borr(r, a, b, c):
    r[c] = r[a] | r[b]

def bori(r, a, b, c):
    r[c] = r[a] | int(b)

def setr(r, a, b, c):
    r[c] = r[a]

def seti(r, a, b, c):
    r[c] = int(a)

def gtir(r, a, b, c):
    r[c] = int(
        int(a) > r[b]
    )

def gtri(r, a, b, c):
    r[c] = int(
        r[a] > int(b)
    )

def gtrr(r, a, b, c):
    r[c] = int(
        r[a] > r[b]
    )

def eqir(r, a, b, c):
    r[c] = int(
        int(a) == r[b]
    )

def eqri(r, a, b, c):
    r[c] = int(
        r[a] == b
    )

def eqrr(r, a, b, c):
    r[c] = int(
        r[a] == r[b]
    )


# create samples datastructure
def toListOfInts(it):
    return [int(i) for i in it]

index = 0
samples = [{}]
with open('input.1.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        if line == "":
            samples.append({})
            index = len(samples) - 1
        else:
            matches = re.match("^(Before|After):\s+\[(\d+), (\d+), (\d+), (\d+)\]", line)
            if matches:
                samples[index][matches.groups()[0].lower()] = toListOfInts(matches.groups()[1:])
            else:
                matches = re.match("(\d+) (\d+) (\d+) (\d+)", line)
                samples[index]["func"] = toListOfInts(matches.groups())


instructionmap = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

for sample in samples:
    sample["count"] = 0
    I, A, B, C = sample["func"]
    for name, func in instructionmap.items():
        sreg = list(sample["before"])  # copy
        sres = list(sample["after"])   # copy
        func(sreg, A, B, C)
        if sreg == sres:
            sample["count"] += 1

print("PART1: %d" % len(filter(lambda s: s["count"] > 2, samples)))


# PART 2
opcodes = {}
for i in range(16):
    opcodes[i] = instructionmap.values()

for sample in samples:
    I, A, B, C = sample["func"]
    for func in opcodes[I]:
        sreg = list(sample["before"])  # copy
        sres = list(sample["after"])   # copy
        func(sreg, A, B, C)
        if sreg != sres:
            opcodes[I].remove(func)


found = []
while len(found) != 16:
    for code, funcs in opcodes.items():
        if len(funcs) == 1:
            if funcs[0] not in found:
                found.append(funcs[0])
        else:
            opcodes[code] = [func for func in funcs if func not in found]

# set register default
reg =  [0, 0, 0, 0]

with open('input.2.txt', 'r') as f:
    for line in f.readlines():
        matches = re.match("(\d+) (\d+) (\d+) (\d+)", line.rstrip())
        I, A, B, C = toListOfInts(matches.groups())
        opcodes[I][0](reg, A, B, C)

print("PART2: %d" % (reg[0],))
