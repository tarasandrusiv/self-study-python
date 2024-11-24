# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
# [3, 6, 9, 12]  # elements divided by 3
# [5, 10]  # elements divided by 5
# [0, 15]  # elements divided by 3 and by 5

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
divisible_by_three = []

for element in range(len(input_list)):
    if element % 3 == 0:
        if element % 5 == 0:
            continue
        divisible_by_three.append(element)

print(divisible_by_three) # elements divided by 3

divisible_by_five = []

for element in range(len(input_list)):
    if element % 5 == 0:
        if element % 3 == 0:
            continue
        divisible_by_five.append(element)

print(divisible_by_five) # elements divided by 5

divisible_by_both = []

for element in range(len(input_list)):
    if element % 3 == 0 and element % 5 == 0:
        divisible_by_both.append(element)

print(divisible_by_both)