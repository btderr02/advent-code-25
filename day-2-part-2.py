import math

f = open("day-2-input.txt", "r")
input = f.read()
f.close()

input_list = input.split(",")
ranges_list = []
for i in input_list:
    ranges_list.append(i.split("-"))
invalid_ids = []

# Holy type changes
def invalid_checker(number):
    number = str(number)
    num_length = int(len(number))
    for window_size in range(1, math.floor((num_length/2) + 1)):
        iterations = (num_length/window_size) - 1
        if iterations % 1 != 0:
            continue
        iterations = int(iterations)
        matches = 0
        for iteration in range(1,iterations+1):
            og_number = number[:window_size]
            test_number = number[(iteration * window_size):(iteration * window_size) + window_size]
            if og_number != test_number:
                break
            else:
                matches += 1
        if matches == iterations:
            invalid_ids.append(int(number))
            return


for i in ranges_list:
    start = i[0]
    end = i[1]
    # Need to add a 1 to the end to make the range inclusive
    for j in range(int(start),int(end)+1):
        invalid_checker(j)

print(sum(invalid_ids))