"""
Commonly developers need to extend or augment the functionality of a callable without modifying the callable itself.
This form of metaprogramming is accomplished by wrapping one callable with another.
Wrappers sit between callers and callables and perform operations before and or after calling the wrapped callable.

Wrappers accept a callable object and return a callable matching the argument signature of the wrapped callable.
The returned callable becomes a replacement for the wrapped callable.

Wrappers are easy to create in Python because everything in Python (including callables) is an object.
Functions and methods are both callable objects that can be used as arguments for other callables.
Wrapping callables is so common that the language includes a shorthand syntax named: decorators.
"""

from rich import print


def any_callable(argument_a, argument_b, argument_c=':)'):
        print(f'☎️  [blue]any_callable[/blue]: with arguments: {argument_a=} {argument_b=} {argument_c=}')


def make_wrapper(function):
    def wrapper(argument_a, argument_b, argument_c=None):
        print(f'☎️  [blue]wrapper[/blue] with arguments: {argument_a=} {argument_b=} {argument_c=}')
        print()
        return function(argument_a.upper(), argument_b * 10, argument_c)
    return wrapper


any_callable('a', 'b', 'c')
print()

#manual wrapping

wrapped_callable = make_wrapper(any_callable)
wrapped_callable('a', 'b', 'c')

