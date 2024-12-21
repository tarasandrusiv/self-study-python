# Write function that takes list of numbers, and returns the second largest number.
# If there's no second largest number in the list (empty list is passed, or list contains only the same number), function should return None.
# You should NOT use max/min built-n functions, sort/sorted.
# Write implementation that performs only one pass through the list (complexity O(n)).
# second_largest_number([])  # None
# second_largest_number([1, 1])  # None
# second_largest_number([1, 2, 3, 4, 5])  # 4


def second_largest_number(lst):
    max_number = 0
    lesser_number = 0
    for number in range(len(lst)):
        if number == len(lst) - 1:
            break
        elif lst[number] > lst[number + 1]:
            max_number = lst[number]
        else:
            max_number = lst[number + 1]
            lesser_number = lst[number]
    print(max_number)
    print(lesser_number)

second_largest_number([2, 1, 3, 4, 5, 45, 87, 555555, 6])

# my_list = [10, 20, 30, 40]
#
# # Use the range to track the current and next index
# for i in range(len(my_list)):
#     current_item = my_list[i]
#     next_item = my_list[i + 1] if i + 1 < len(my_list) else None
#     print(f"Current: {current_item}, Next: {next_item}")