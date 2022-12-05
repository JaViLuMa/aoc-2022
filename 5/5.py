from copy import deepcopy
import re


stacks = {
  1: ["N", "D", "M", "Q", "B", "P", "Z"],
  2: ["C", "L", "Z", "Q", "M", "D", "H", "V"],
  3: ["Q", "H", "R", "D", "V", "F", "Z", "G"],
  4: ["H", "G", "D", "F", "N"],
  5: ["N", "F", "Q"],
  6: ["D", "Q", "V", "Z", "F", "B", "T"],
  7: ["Q", "M", "T", "Z", "D", "V", "S", "H"],
  8: ["M", "G", "F", "P", "N", "Q"],
  9: ["B", "W", "R", "M"]
}

copyOfStacks = deepcopy(stacks)

with open("data.txt") as f:
  data = f.read().splitlines()

  regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
  moves = [regex.findall(line)[0] for line in data]
  moves = [(int(move[0]), int(move[1]), int(move[2])) for move in moves]

# Part 1
for move in moves:
  howMuch = move[0]
  fromStack = move[1]
  toStack = move[2]

  for x in range(howMuch):
    stacks[toStack].append(stacks[fromStack].pop())

lastElements = [stack[-1] for stack in stacks.values()]

print(f"Part 1: {''.join(lastElements)}")

# Part 2
stacks = copyOfStacks

for move in moves:
  howMuch = move[0]
  fromStack = move[1]
  toStack = move[2]

  stacks[toStack] += stacks[fromStack][-howMuch:]
  
  stacks[fromStack] = stacks[fromStack][:-howMuch]

lastElements = [stack[-1] for stack in stacks.values()]

print(f"Part 2: {''.join(lastElements)}")
