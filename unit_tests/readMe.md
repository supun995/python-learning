The 
unittest module
, opens in a new tab is Python's built-in testing module. Used to create and run unit and integration tests.

All software contains developer made assumptions.

Areas of code where assumptions are made:

Callable parameters and return types
Object types
Nullability
Idempotency
Data structures
...
Erroneous assumptions can result in software defects of varying degrees of severity. Unittest enables developers to test software assumptions using Python code.

Unittest is designed around the notion of performing an action and making an assertion regarding the results.

Actions are events which produce or change: objects and or external resources.

Resources include: files, databases, etc. Actions include: operations, and callables.

Actions are taken and assertions are made about the state of the results. Assertions raise an exception when results don't match what's expected. Indicating that a codified assumption is no longer accurate.

