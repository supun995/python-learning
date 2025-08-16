"""
Decorators can be stacked to create a chain of wrappers.
Decorators are evaluated by the interpreter from bottom to top.
The example below applies two decorators to the a_callable function.
The title_case decorator is evaluated first followed by the exclaim_it function.

"""

from rich import print

def title_case(function):
    def wrapper(text):
        return function(text).title()
    return wrapper

def exclaim_it(function):
    def wrapper(text):
        return f'{function(text)}!'
    return wrapper

@exclaim_it
@title_case
def a_callable(text):
    return text.lower()


print(a_callable('THIS IS THE WAY'))

