with open("data.txt") as f:
  data = f.read().split("\n")

  data = [x.split(" ") for x in data]

# Part 1
totalScore = 0

for item in data:
  if item[0] == "A":
    if item[1] == "X":
      totalScore += (3 + 1)
    elif item[1] == "Y":
      totalScore += (6 + 2)
    elif item[1] == "Z":
      totalScore += (0 + 3)

  elif item[0] == "B":
    if item[1] == "X":
      totalScore += (0 + 1)
    elif item[1] == "Y":
      totalScore += (3 + 2)
    elif item[1] == "Z":
      totalScore += (6 + 3)

  elif item[0] == "C":
    if item[1] == "X":
      totalScore += (6 + 1)
    elif item[1] == "Y":
      totalScore += (0 + 2)
    elif item[1] == "Z":
      totalScore += (3 + 3)

print(f"Part 1: {totalScore}")

# Part 2
totalScoreReal = 0

for item in data:
  if item[1] == "X":
    if item[0] == "A":
      totalScoreReal += (0 + 3)
    elif item[0] == "B":
      totalScoreReal += (0 + 1)
    elif item[0] == "C":
      totalScoreReal += (0 + 2)

  elif item[1] == "Y":
    if item[0] == "A":
      totalScoreReal += (3 + 1)
    elif item[0] == "B":
      totalScoreReal += (3 + 2)
    elif item[0] == "C":
      totalScoreReal += (3 + 3)

  elif item[1] == "Z":
    if item[0] == "A":
      totalScoreReal += (6 + 2)
    elif item[0] == "B":
      totalScoreReal += (6 + 3)
    elif item[0] == "C":
      totalScoreReal += (6 + 1)

print(f"Part 2: {totalScoreReal}")
