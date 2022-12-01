with open("data.txt") as f:
  data = f.read().split("\n\n")

  data = [sum(list(map(int, i.split("\n")))) for i in data]

# Part 1
print(f"Part 1: {max(data)}")

# Part 2
data.sort(reverse=True)

print(f"Part 2: {data[0] + data[1] + data[2]}")
