#!/usr/bin/env python

# AGAIN BAD CODE, ENJOY THE READ :-)

from time import time, sleep
from re import match
from time import sleep
from multiprocessing import Process, Queue

totalTimeSeconds = 0
processed = []

index = 0
key_times = {}
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    index += 1
    key_times[char] = index

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

def unique_keys(listx, listy):
    result = []
    for key in listx:
        if key not in listy:
           result.append(key)
    return result

def find_unlocked(dep_tree):
    unlocked = []
    for k,v in dep_tree.items():
        if not v:
            unlocked.append(k)
    return unlocked

def clean_key(key):
    for k, v in dep_tree.items():
        delete_keys = []
        try:
            index = v.index(key)
            del(v[index])
        except ValueError:
            pass
        if key in dep_tree.keys():
            delete_keys.append(key)
    for key in delete_keys:
        del(dep_tree[key])

# build original work tree
keys = set()
key_deps = []
dep_tree = {}

for line in lines:
    matches = match('^Step (.) must be finished before step (.) can begin.$', line)
    dep, key = matches.groups()
    keys.add(dep)
    keys.add(key)
    if key not in dep_tree.keys():
        dep_tree[key] = []
    dep_tree[key].append(dep)

keys = sorted(list(keys))
dep_tree_keys = sorted(dep_tree.keys())
missing_keys = unique_keys(keys, dep_tree.keys())
for missing_key in missing_keys:
    dep_tree[missing_key] = []

# use dependecy tree to assign work
def worker(q, rq):
    while True:
        key = q.get()
        sleeptime = (60 + key_times[key]) / 1000
        sleep(sleeptime)
        rq.put(key)

q = Queue()
rq = Queue()
for i in range(5):
    Process(target=worker, args=(q,rq)).start()

already_put = []
result = []
start = time()
while len(dep_tree.keys()) > 0:
    tasks = find_unlocked(dep_tree)
    for task in tasks:
        if task not in already_put:
            q.put(task)
            already_put.append(task)
    done = rq.get()
    clean_key(done)
    result.append(done)


print(result)
