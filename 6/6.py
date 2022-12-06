def find_marker(data, size):
  marker = ""

  for i in range(len(data)):
    marker += data[i]

    if len(marker) > size:
      marker = marker[1:]
    
    if len(marker) == size and len(set(marker)) == size:
      return i + 1


data = open("data.txt").read()

# Part 1
print(f"Part 1: {find_marker(data, 4)}")

# Part 2
print(f"Part 2: {find_marker(data, 14)}")
