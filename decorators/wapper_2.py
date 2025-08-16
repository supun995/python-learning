"""
The example below demonstrates a wrapper with additional arguments.
The make_wrapper function accepts a callable to wrap and a keyword argument.
The action argument is provided when the wrapper is created and accessible from the returned wrapper function.
The callable bound to the wrapped_callable name will now always use title as the action.

"""

from rich import print

def any_callable(argument_a, argument_b, argument_c=':)'):
    print(f'☎️  [blue]any_callable[/blue]: with arguments: {argument_a=} {argument_b=} {argument_c=}')


def make_wrapper(function, action=None):
    def wrapper(argument_a, argument_b, argument_c=None):
        print(f'☎️  [blue]wrapper[/blue] with arguments: {argument_a=} {argument_b=} {argument_c=}')
        print()
        if action in 'upper lower title'.split():
            argument_a = getattr(argument_a, action)()
            argument_b = getattr(argument_b, action)()

        return function(argument_a, argument_b, argument_c)
    return wrapper

wrapped_callable = make_wrapper(any_callable, 'title')
wrapped_callable('this is the way', 'b', 'c')

