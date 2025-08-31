
'''Write decorator call_counter that takes path to file as argument.
Decorated function should log total number of calls to passed file.
Several functions could log to the same file.'''


def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            with open(path, 'w') as f:
                f.writelines(f'Function "{func.__name__}" was called {wrapper.calls} times')
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator


@call_counter('text.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
print(add(3, 5))
#


# data.txt content:
# Function 'add' was called 1 times
# Function 'add' was called 2 times

# def func():
#     func.calls += 1
#
#
# func.calls = 0
#
# func()
# func()
# func()
# print(func.calls)
