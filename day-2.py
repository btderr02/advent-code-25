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
    if (len(number) % 2 == 1):
        return
    first_half = number[0:int(len(number)/2)]
    second_half= number[int(len(number)/2):len(number)]
    if int(first_half) == int(second_half):
        invalid_ids.append(int(number))

for i in ranges_list:
    start = i[0]
    end = i[1]
    # Need to add a 1 to the end to make the range inclusive
    for j in range(int(start),int(end)+1):
        invalid_checker(j)
        
print(sum(invalid_ids))