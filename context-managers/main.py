"""
Context managers are objects that create a runtime context where developer-defined code is executed at the start and end of the context. Context managers provide developers with a Pythonic way to perform opening and closing actions such as closing files, connections, etc.
"""

#Without context manager:

try:
    f = open('users.csv', 'w')
    f.write('yuzu,nimbus')
finally:
    f.close()

#With context manager:

with open('users.csv', 'w') as f:
    f.write('yuzu,nimbus')

"""
Python allows context managers to be created with classes andcallables. Class-based context managers are created byimplementing the 
context manager protocol
, opens in a new tab. Classesbecome context managers by implementing the __enter__ and__exit__ magic methods.

The Context class in the below example implements the contextmanager protocol. The __enter__ method accepts zero arguments.The __exit__ method accepts three arguments related to runtimeexceptions raised inside the context.

The output from the code below demonstrates the order ofoperations for context managers. The __enter__ method is calledwhen the context opens. Code defined inside the block scope ofthe context manager is run next. The __exit__ method is calledwhen the context closes.
"""