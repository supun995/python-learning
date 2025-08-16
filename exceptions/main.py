"""
Exceptions disrupt normal code flow in order to report exceptional conditions. Exceptional conditions include failed and interrupted operations. Exceptions inform the Python runtime that the normal code flow cannot continue. They occur for a wide range of reasons including: attempting to open a non-existent file, experiencing a dropped network connection, etc. The runtime is made aware of exceptions when they are raised in code.

Exceptions are specific object types that cause the runtime to break the current code flow when raised. The Python runtime includes many built-in exception types that might be raised by the standard library. Any class deriving from the
BaseException, opens in a new tab class is considered an exception by the runtime.

Exception hierarchy courtesy of the Python documentation
BaseException
BaseExceptionGroup
GeneratorExit
KeyboardInterrupt
SystemExit
Exception
    ArithmeticError
        FloatingPointError
        OverflowError
        ZeroDivisionError
    AssertionError
    AttributeError
    BufferError
    EOFError
    ExceptionGroup [BaseExceptionGroup]
    ImportError
        ModuleNotFoundError
    LookupError
        IndexError
            KeyError
    MemoryError
    NameError
        UnboundLocalError
    OSError
        BlockingIOError
        ChildProcessError
        ConnectionError
            BrokenPipeError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionResetError
        FileExistsError
        FileNotFoundError
        InterruptedError
        IsADirectoryError
        NotADirectoryError
        PermissionError
        ProcessLookupError
            TimeoutError
    ReferenceError
    RuntimeError
        NotImplementedError
        RecursionError
    StopAsyncIteration
    StopIteration
    SyntaxError - IndentationError - TabError
    SystemError
    TypeError
    ValueError - UnicodeError - UnicodeDecodeError - UnicodeEncodeError - UnicodeTranslateError
        Warning
        BytesWarning
        DeprecationWarning
        EncodingWarning
        FutureWarning
        ImportWarning
        PendingDeprecationWarning
        ResourceWarning
        RuntimeWarning
        SyntaxWarning
        UnicodeWarning
        UserWarning

"""

try:
    print('from try')
except:
    print('from except')
else:
    print('from else')
finally:
    print('from finally')


# try:
#     print('from try')
#     raise Exception
# except:
#     print('from except')
# else:
#     print('from else')
# finally:
#     print('from finally')

try:
    f = open('dataset.txt', 'w')
    f.write('python is neat')
finally:
    f.close()
    print('file closed!')
"""
NOTE: Context managers are the preferred means of performing cleanup actions when available.
"""
class KeyboardListener: ...

listeners = {}
klistener = KeyboardListener()

try:
    name = klistener.name
except:
    name = klistener.__class__.__name__

listeners[name] = klistener

print(listeners)





"""
"""

try:
    raise Exception('kaboom!')
except Exception as ex:
    print(ex.args)
"""
"""
from random import choice

def random_exception(*exceptions):
    raise choice(exceptions)

try:
    random_exception(
        OSError('os broke?'),
        IndexError('not cool'),
        AttributeError('where did it go?'),
        KeyboardInterrupt,
        SystemError,
    )
    # Specific exceptions can be handled independently.
except OSError as ex:
    print('os errors are the worst')
    print(ex)
    # Multiple exceptions can be handled within the same except block.
except (IndexError, AttributeError) as ex:
    print('wrong index or missing attribute, we have a problem.')
    print(ex)
    # Exception handlers don't have to name-bind the exception.
except KeyboardInterrupt:
    print('stop interrupting me')
    # Omitting an exception handles all unhandled exceptions.
except:
    print('catch all without binding exception')



"""
"""

scores = [0.45, 0.90, 0.92, 1.0, None]
try:
    with open('dataset.txt', 'w') as ds:
        try:
            for score in scores:
                ds.write(f'{score * 100}\n')
        except ValueError as ex:
            print(ex)

except OSError as ex:
    print(ex)


