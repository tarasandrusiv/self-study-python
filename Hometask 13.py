# There's a string with email address.
# Print True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'
from operator import index

email = "aaab@bbccc."

count = True
comes_before = True
symbols_are_valid = True
start_end = True

if (email.count('@') == 1) and (email.count('.') == 1):
    comes_before = email.index('@') < email.index('.')
    if comes_before:
        start_end = (email.startswith('@') != True) and (email.endswith('.') != True)
        if start_end:
            for char in email:
                if char not in "@." and not char.isalnum():
                    symbols_are_valid = False
                    break
        else:
            start_end = False
    else:
        comes_before = False
else:
    print(False)



if comes_before == start_end == count == symbols_are_valid:
    print(True)
else:
    print(False)

print(comes_before, start_end, count, symbols_are_valid)


