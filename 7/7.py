from collections import defaultdict
from os import path, sep

dirSizes = defaultdict(int)

lines = open("data.txt").readlines()

cwd = ""

for line in lines:
  parts = line.strip().split(" ")

  if parts[0] == "$" and parts[1] == "cd":
    cwd = path.normpath(path.join(cwd, parts[2]))

  if parts[0].isnumeric():
    dirs = cwd.split("/")

    for i in range(len(dirs)):
      dirPath = path.normpath(path.join(*dirs[:i + 1]))
      
      dirSizes[dirPath] += int(parts[0])

space = 70000000 - dirSizes["."]

sizes = dirSizes.values()

# Part 1
totalSizesOfDirs = sum((x for x in sizes if x <= 100000))

print(f"Part 1: {totalSizesOfDirs}")

# Part 2
directoryAfterFreeSpace = min((x for x in sizes if x + space >= 30000000))

print(f"Part 2: {directoryAfterFreeSpace}")
