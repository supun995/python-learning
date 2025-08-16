import time
from rich import print
from functools import wraps


def timer(function):
    def wrapper():
        start = time.perf_counter()
        fnout = function()
        close = time.perf_counter()
        print(f'{function.__name__} completed in {close - start:0.5f} seconds.')
        return fnout
    return wrapper

@timer
def something_sorta_slow():
    return ''.join([str(n) for n in range(1_000_000) if n % 10_000 == 0.0])


print(something_sorta_slow.__name__)



"""
Notice that the something_sorta_slow function has been renamed to: wrapper. This can cause strange errors in third-party libraries. Python's standard library includes a mechanism for renaming the wrapper with the original name.

The 
functools.wraps
, opens in a new tab callable replaces several attributes of the wrapper with the corresponding attributes from the wrapped callable. Specifically the following attributes are copied: __module__, __name__, __qualname__, __annotations__ and __doc__.
"""

import time
from rich import print
from functools import wraps


def timer(function):

    @wraps(function)
    def wrapper():
        start = time.perf_counter()
        fnout = function()
        close = time.perf_counter()
        print(f'{function.__name__} completed in {close - start:0.5f} seconds.')
        return fnout
    return wrapper



@timer
def something_sorta_slow():
    return ''.join([str(n) for n in range(1_000_000) if n % 10_000 == 0.0])


print(something_sorta_slow.__name__)