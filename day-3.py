input_array = []
joltage = []

with open("day-3-input.txt") as f:
    input_array = [line.strip() for line in f if line.strip()]
#print(input_array)

""" input_array = ('987654321111111',
'811111111111119',
'234234234234278',
'818181911112111'
) """

def find_max(number, exclusion, exclude_end):
    max_value = -1
    if exclude_end == True:
        for i in range(0,len(number)-1):
            if int(number[i]) > max_value:
                max_value = int(number[i])
    else:
        for i in range(0,len(number)):
            if int(number[i]) > max_value:
                max_value = int(number[i])
    return max_value

def find_max_indices(max_value, number):
    max_indices = []
    location = 0
    for i in number:
        if int(i) == max_value:
            max_indices.append(location)
        location += 1
    return max_indices
    
for i in input_array:
    max_value = find_max(i, 0, True)
    max_indices = find_max_indices(max_value, i)
    second_max = -1
    for j in max_indices:
        number_rest = i[j+1:]
        second_max_candidate = find_max(number_rest, max_value, False)
        if second_max_candidate > second_max:
            second_max = second_max_candidate
    bank_joltage = str(max_value) + str(second_max)
    joltage.append(int(bank_joltage))

print(joltage[:10])
print(sum(joltage))