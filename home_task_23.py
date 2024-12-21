'''Write function that takes list of numbers, and returns the second largest number.
If there's no second largest number in the list (empty list is passed, or list contains only the same number), function should return None.
You should NOT use max/min built-n functions, sort/sorted.
Write implementation that performs only one pass through the list (complexity O(n)).'''
from operator import index


def second_largest_number(lst):
    max_number = 0
    lesser_number = 0
    for number in range(len(lst)):
        if number == len(lst) - 1:
            break
        if lst[number] > lst[number + 1] and lst[number] >= max_number:
            max_number = lst[number]
        else:
            if lst[number + 1] > max_number:
                max_number = lst[number + 1]
            if lst[number] > lesser_number or index(lst[number]) == len(lst):
                lesser_number = lst[number]
            else:
                continue
    print(max_number)
    print(lesser_number)
second_largest_number([2, 1, 3, 4, 5, 45, 87, 555555, 6, 77999, 0, 32, 2, 33333333333, 99999999999999, 453, 0])
