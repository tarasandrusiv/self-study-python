# There's a string with email address.
# Print True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'
from operator import index

email = "aaa@bbb.ccc"

comes_before = email.index('@') < email.index('.')
start_end = (email.startswith('@') != True) and (email.endswith('.') != True)
count = (email.count('@') == 1) and (email.count('.') == 1)

symbols_are_valid = True
for char in email:
    if char not in "@." and not char.isalnum():
        symbols_are_valid = False
        break

if comes_before == start_end == count == symbols_are_valid:
    print(True)
else:
    print(False)

print(comes_before, start_end, count, symbols_are_valid)


