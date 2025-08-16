"""
The wrappers in the above examples match the argument signature of the wrapped callable.
However, decorators are often applied to callables with unknown signatures.
The example below uses the packing/unpacking syntax to represent multiple positional and keyword arguments with individual arguments.

The wrapper defines two arguments: args and kwargs.
The single asterisk in front of args instructs the interpreter to pack all positional arguments into args as a tuple.
The double asterisk packs all keyword arguments into kwargs as a dictionary.

"""

from rich import print

def decorator_with_args(action=None):
    def make_wrapper(function):
        def wrapper(*args, **kwargs):
            print(f'☎️  [blue]wrapper[/blue] with arguments: {args=} {kwargs=}')
            if len(args) >= 2:
                args = list(args)
                args[0] = getattr(args[0], action)()
                args[1] = getattr(args[1], action)()

            return function(*args, **kwargs)
        return wrapper
    return make_wrapper


@decorator_with_args('upper')
def a_callable(argument_a, argument_b, argument_c=':)'):
    print(f'☎️  [blue]a_callable[/blue]: {argument_a=} {argument_b=} {argument_c=}', end='\n\n')


@decorator_with_args('title')
def b_callable(argument_a, argument_b, argument_c=':)', argument_d='(:'):
    print(f'☎️  [blue]b_callable[/blue]: {argument_a=} {argument_b=} {argument_c=} {argument_d=}', end='\n\n')


a_callable('this is the way', 'hello friend')
b_callable('this is the way', 'hello friend', argument_d='hungry')


