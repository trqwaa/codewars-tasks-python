import functools
import operator
def grow(arr):
    y = functools.reduce(operator.mul, arr)
    return y