# Write function lst2dict(lst) that takes list and returns dictionary.
# Dictionary should contain key-value pairs, where
# - key is list element on even position (0, 2, 4, ...)
# - value corresponding to this key is the list element, following after key
# If list has odd length, last item shouldn't be taken into account.
# lst2dict([0, 1, 2, 3])  # {0: 1, 2: 3}
# lst2dict(['a', 'A', 'b', 'B', 'c'])  # {'a': 'A', 'b': 'B'}


def lst2dict(lst):
    d1 = dict()
    for l in range(0, len(lst), 2):
        if l + 1 < len(lst):
            d1[l] = lst[l + 1]
    return d1

print(lst2dict([0, 's', 'l', 3, 4, 65, 66, 87, 123]))
