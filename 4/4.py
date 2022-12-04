with open("data.txt") as f:
  data = f.read().split()

  data = [x.split(",") for x in data]

fullyContainedPart1 = 0
fullyContainedPart2 = 0

for item in data:
  for i in range(len(item)):
    f, s = map(int, item[i].split("-"))

    item[i] = list(range(f, s + 1))

# Part 1
  if all(x in item[1] for x in item[0]) or all(x in item[0] for x in item[1]):
    fullyContainedPart1 += 1

# Part 2
  if len(set(item[0]).intersection(*item[1:])) > 0:
    fullyContainedPart2 += 1

print(f"Part 1: {fullyContainedPart1}")
print(f"Part 2: {fullyContainedPart2}")
