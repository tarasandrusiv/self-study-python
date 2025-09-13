# Write function using regular expressions that takes email as string, and returns True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'
# email = "aaa@bbb.ccc"  # True

import re

pattern = r"(^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$)"

email = "aaab4bb@ff3fcm.m"

regexp_obj = re.compile(pattern)
result = regexp_obj.search(email)
print(bool(result))





