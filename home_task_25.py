'''Write decorator skip_if that takes two arguments:
- condition: boolean expression
- reason: string, default value empty string
If condition is calculated as True, function shouldn't be performed and if reason is not empty, reason should be printed
If condition is False, then function should be performed as usual'''


def skip_if(condition, reason=''):
   def decorator(func):
       def wrapper():
           if condition:
                print (reason)
           else:
               return func()
       return wrapper
   return  decorator

@skip_if(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
   assert 2 + 2 == 5

test_two_plus_two()  # 'Skipped because of JIRA-123 bug' is printed

@skip_if(condition=False, reason='Skipped because of JIRA-123 bug')
def test_two_minus_two():
   assert 2 - 2 == 5, "condition is false"

test_two_minus_two()  # assertion error