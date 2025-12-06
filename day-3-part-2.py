input_array = []
joltage = []

with open("day-3-input.txt") as f:
    input_array = [line.strip() for line in f if line.strip()]
#print(input_array)
#input_array = input_array[:10]
""" input_array = ('987654321111111',
'811111111111119',
'234234234234278',
'818181911112111'
) """

def find_max(number, exclusion):
    max_value = -1
    index = -1
    for i in range(0,len(number)-exclusion):
        if int(number[i]) > max_value:
            max_value = int(number[i])
            index = i
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
    length = 2
    max_value = find_max(i, length - 1)
    max_indices = find_max_indices(max_value, i)
    bank_joltage = max_value
    for j in max_indices:
        number_rest = i[j+1:]
        for k in range(1,length):
            max = -1
            max_candidate = find_max(number_rest, length - 2)
            if max_candidate > second_max:
                second_max = max_candidate
            bank_joltage.append(max)
    joltage.append(int(bank_joltage))

print(joltage[:10])
print(sum(joltage))