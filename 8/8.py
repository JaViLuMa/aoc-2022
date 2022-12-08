trees = 0

highestScore = 0


def part1(tree, upTrees, leftTrees, rightTrees, downTrees):
  global trees
  
  if len(upTrees) == 0 or len(leftTrees) == 0 or len(rightTrees) == 0 or len(downTrees) == 0:
    trees += 1
  else:
    intForest = int(forest[x][y])

    if intForest > max(upTrees) or intForest > max(leftTrees) or intForest > max(rightTrees) or intForest > max(downTrees):
      trees += 1


def howMany(tree, trees):
  howMany = 0

  for x in trees:
    if int(tree) > x:
      howMany += 1

    if int(tree) == x or int(tree) < x:
      howMany += 1
      break

  return howMany


def part2(tree, upTrees, leftTrees, rightTrees, downTrees):
  global highestScore
  
  if len(upTrees) == 0 or len(leftTrees) == 0 or len(rightTrees) == 0 or len(downTrees) == 0:
    highestScore = max(0, highestScore)
  
  upTrees = list(reversed(upTrees))
  leftTrees = list(reversed(leftTrees))

  howManyUp = howMany(tree, upTrees)
  howManyLeft = howMany(tree, leftTrees)
  howManyRight = howMany(tree, rightTrees)
  howManyDown = howMany(tree, downTrees)

  totalHowMany = howManyUp * howManyLeft * howManyRight * howManyDown

  highestScore = max(totalHowMany, highestScore)


lines = open("data.txt").read().splitlines()

forest = []

for line in lines:
  forest.append(list(line))

for x in range(len(forest)):
  for y in range(len(forest[x])):
    upTrees = []
    leftTrees = []
    rightTrees = []
    downTrees = []

    leftTrees.append(forest[x][:y])
    rightTrees.append(forest[x][y + 1:])

    for i in range(x):
      upTrees.append(forest[i][y])

    for i in range(x + 1, len(forest)):
      downTrees.append(forest[i][y])

    upTrees = [int(tree) for tree in upTrees]
    leftTrees = [int(tree) for tree in leftTrees[0]]
    rightTrees = [int(tree) for tree in rightTrees[0]]
    downTrees = [int(tree) for tree in downTrees]
    
# Part 1
    part1(forest[x][y], upTrees, leftTrees, rightTrees, downTrees)
    
# Part 2
    part2(forest[x][y], upTrees, leftTrees, rightTrees, downTrees)

print(f"Part 1: {trees}")
print(f"Part 2: {highestScore}")
