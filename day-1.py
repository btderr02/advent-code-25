pointer = 50
stop = 0
zeros = 0

input_array = []

with open("day-1-input.txt") as f:
  for x in f:
    input_array.append(x[:-1])

for i in input_array:
    direction = i[0:1]
    steps = int(i[1:])
    j = 0
    if direction == "R":
        while j < steps:
            pointer += 1
            j += 1
            if pointer == 100:
               pointer = 0
    if direction == "L":
        while j < steps:
            pointer -= 1
            j += 1
            if pointer == -1:
               pointer = 99
    if pointer == stop:
               zeros += 1

print(zeros)