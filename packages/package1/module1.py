import functools

m1a = 'AAA'

def func1(*args):
    """returns a reduced function / multiplies every element
    in the provided positional arguments.
    """
    return functools.reduce(lambda a, b: a * b, args)

def hidden_func3(x):
    return 100
