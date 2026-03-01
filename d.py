from pythonProject.home_task_19 import result

to_seconds = 24 * 60
print(f"20 days are {20 * to_seconds} minutes")
print(f"20 days are {35*24*60} minutes")


def days_to_units():
    print(f"20 days are {20 * to_seconds} minutes")

days_to_units()

lst = [21, 'ddd', True]
lst.append('22')
#Remove
lst.pop()
lst.pop(1)
lst.append('ddd')
lst.remove("ddd")
lst.clear()
del lst[0:1]
print(lst)


chars = list("Hello")
print(chars)
chars[-1] = "d"
print(chars[-1])
print(chars[::-1])



#1 Compare [3, 2, 1] and [1, 2, 3]
from collections import Counter

data = [1, 2, 3]
data2 = [3, 2, 1, 1]
compare_is_equal = (Counter(data)) == (Counter(data2))
print(compare_is_equal)


print(sorted(data) == sorted(data2))

#2 take only uniq elements
take_uniq_el = [1,2,3,2,1,3,5,6]
uniq = set(take_uniq_el)
print(uniq)

#3 reverse

make_reverse = [1, 2, 3, 4]
print(make_reverse[::-1])

#4 take last el by index

take_el = [1, 2, 3, 4, 5]
print(take_el[4:])
#5 take [3,4]
print(take_el[2:4])

#6 delete from dict
del_from_set = {'test': 1, 'test2': 2, 'test3': 3}
del del_from_set['test2']
print(del_from_set)

#7 add to dict

add_to_dict = {'test': 1, 'test2': 2, 'test3': 3}
add_to_dict['test4'] = 4
print(add_to_dict)
#return biggest value key
biggest_value = {'test': 1, 'test8': 8, 'test2': 2, 'test3': 3}
max_value = 0
for value in biggest_value.values():
    if value > max_value:
        max_value = value
print(max_value)


print(max(biggest_value.values()))






