"""
Decorators require an additional function in order to allow arguments.
Previous wrappers used two functions.
The outer function accepts a callable to wrap and returns the innermost wrapper function.

Decorators requiring arguments include a third function.
The outermost function defines the required arguments and returns the next function.
The remaining two inner functions are similar to the previous examples.

"""

from rich import print

def decorator_with_args(action=None):
    def make_wrapper(function):
        def wrapper(argument_a, argument_b, argument_c=None):
            print(f'☎️  [blue]wrapper[/blue] with arguments: {argument_a=} {argument_b=} {argument_c=}')
            print()
            if action in 'upper lower title'.split():
                argument_a = getattr(argument_a, action)()
                argument_b = getattr(argument_b, action)()

            return function(argument_a, argument_b, argument_c)
        return wrapper
    return make_wrapper

@decorator_with_args('upper')
def some_callable(argument_a, argument_b, argument_c=':)'):
    print(f'☎️  [blue]any_callable[/blue]: with arguments: {argument_a=} {argument_b=} {argument_c=}')

some_callable('x', 'y', 'z')

