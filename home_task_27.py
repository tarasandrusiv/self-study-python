'''Write generator function that takes two arguments:
lst - list
iter_num - integer with default value None
Generator should return items from the list one by one. When generator comes to the last item, it should start from the beginning and repeat it iter_num times.
If iter_num is None, generator should return items infinitely'''


def list_item_generator(lst, iter_num=None):
    if iter_num is None:   # infinite loop
        while True:
            for item in lst:
                yield item
    else:   # repeat exactly iter_num times
        for _ in range(iter_num):
            for item in lst:
                yield item


# Example usage
lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=20):
    print(i)






