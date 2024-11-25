# There is a list of at least two float elements.
# Create a new list. It should contain elements of initial list, and between them should be added average of that elements.

lst = [1, 2, 3, 4, 6]

new_lst = [(lst[i] + lst[i + 1]) / 2 for i in range(len(lst) - 1)]
result = new_lst + lst
sorted_result = sorted(result)
print(new_lst)
print(sorted_result)
