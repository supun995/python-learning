"""
Debugging with print statements and logs have their use cases. However, sometimes you need something more interactive. The Python debugger enables users to inspect objects and run arbitrary Python code.

The Python debugger is a source code debugging module in the standard library called pdb. The pdb module provides a console which serves as a gateway between source code and the interpreter.

The pdb module provides multiple ways to run Python code under the control of the debugger. The debugger includes commands used to navigate through the code and pause on specific lines. While paused on specific lines, developers can inspect the state of the application

The Python debugger allows developers to set specific line numbers at which to pause. These are known as breakpoints. Setting breakpoints allows code to flow normally and pause when the interpreter encounters a breakpoint.
start with pdb python3 -m pdb playground/guess.py
The debugger remains inside of the play function until it returns. Once the debugged callable returns, the debugger advances to the line where the call originated and continues debugging.

The debugger advances outside of the play callable to the line in the main code block where the call was made. The next command stays inside its current scope and only exits once complete.

Combining next and step allows for more precise code navigation.
The debugger includes commands used to navigate through code in different ways. The next (n) and step (s) are two common commands for navigating code.

The next command is used to step through each line in a callable or frame. The debugger remains inside the currently debugged callable. When the debugger encounters calls to other callables they're run and the results are returned; then the debugger moves to the next line in the currently debugged callable.

The step command is used to step line-by-line through code, occasionally including code from built-in or third-party modules. When the debugger encounters calls to other callables it also debugs those callables.
The interact command opens up an interactive console inside the debugger. The console's global namespace includes all names in the current scope. Allowing the console to interact with a snapshot of the application at the time the interactive console was opened.
"""

import random

# Create a random number for the player to guess.
answer = random.randint(1, 10)


def inform(guess: chr):
    if guess == '=':
        print(f'{"you win":=^80}')
    elif guess == '-':
        print(f'{"higher":+^80}')
    elif guess == '+':
        print(f'{"lower":-^80}')
    else:
        raise ValueError(f'unknown guess type {guess}')


def play():
    # Prompt for a guess between 1 and 10 and convert the value to an int.
    # This application will fail if a non-numeric guess is entered.
    while (guess := int(input('guess a number between 1 and 10> '))) != answer:
        if guess > answer:
            inform('+')
        elif guess < answer:
            inform('-')
    else:
        inform('=')


if __name__ == '__main__':
    play()