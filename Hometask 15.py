# Find the sum and product of the elements of the list greater than the number MIN and less than the number MAX (both boundaries inclusive).
# If there are no such elements, print None object for both the sum and the product.
from functools import reduce

lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

filtered_list = [element for element in lst if MIN <= element <= MAX]

print(filtered_list)

if filtered_list:
    elements_sum = sum(filtered_list)
    elements_product = reduce(lambda x, y: x * y, filtered_list)
else:
    elements_sum = None
    elements_product = None

print('Sum : ',elements_sum)
print('Products : ',elements_product)
