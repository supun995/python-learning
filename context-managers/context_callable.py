"""
Context managers can also be created with callables.
The contextlib.contextmanager decorator turns callables into context managers.
 Callable-based context managers must be generator functions.A generator function in Python is a special type of function that yields values one at a time, pausing between each, instead of returning them all at once.
 Code defined in the finally block is used as the __exit__ method.
 Code prior to the yield keyword is used as the body of the __enter__ method.
 The yield keyword signals the end of __enter__. A yielded value is used as the return value from __enter__.
"""

from contextlib import contextmanager

@contextmanager
def context():
    try:
        print('context opened')
        yield
    finally:
        print('context closed')

if __name__ == '__main__':
    with context():
        print('inside the context')

