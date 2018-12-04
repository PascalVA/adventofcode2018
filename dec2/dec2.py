#!/usr/bin/env python

with open("input.txt", "r") as f:
    ids = f.read().splitlines()

# PART 1
doubles = 0
tripples = 0

for id in ids:
    hastwo, hasthree = (0, 0)
    for char in id:
        count = id.count(char) 
        if count == 2:
            hastwo = 1
        if count == 3:
            hasthree = 1
    doubles += hastwo
    tripples += hasthree

print("PART 1: %d" % (doubles * tripples))

# PART 2
#ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
def matchIds(ids):
  for idx in ids:
      for idy in ids:
          diff = []
          for i in range(len(idx)):
              if idx[i] != idy[i]:
                  diff.append((i))
          if len(diff) == 1:
              result = list(idx)
              result.pop(diff[0])
              return "".join(result)
             
print("PART 2: \"%s\"" % matchIds(ids))
