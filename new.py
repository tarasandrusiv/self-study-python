# dates = ['1-Jan', '25-Dec', '12-Feb', '03-Jan', '30-Nov']
#
# sorted_dates = sorted(
#     dates,
#     key=lambda d: (
#         ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(d.split('-')[1]),
#         int(d.split('-')[0])
#     )
# )
#
# print(sorted_dates)
#
#
# a = ['dd', 'dsd', 'dsw']
#
# print(a.index(a.split('-')))

import pytest
def test_two_plus_two():
   assert 2 + 2 == 5

test_two_plus_two()