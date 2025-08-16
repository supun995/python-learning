"""
Decorators are a shorthand syntax for creating wrappers.
Decorators are placed above a callable definition with a preceding @ symbol.
Following the @ symbol the decorator callable is called using the standard callable syntax.
"""

from rich import print

def im_a_decorator(function):
    def wrapper(argument_a, argument_b, argument_c=None):
        print(f'☎️  [blue]wrapper[/blue] with arguments: {argument_a=} {argument_b=} {argument_c=}')
        print()
        return function(argument_a.upper(), argument_b * 10, argument_c)
    return wrapper

@im_a_decorator
def some_callable(argument_a, argument_b, argument_c=':)'):
    print(f'☎️  [blue]any_callable[/blue]: with arguments: {argument_a=} {argument_b=} {argument_c=}')


some_callable('this is the way', 'b', 'c')

