"""
Not all base classes provide their own implementations.
Some base classes are intended to serve as interfaces for developers to override.
This type of base class is referred to as an abstract base class.
Abstract base classes define an interface that derived classes must implement.

The standard library includes a module named
abc
, opens in a new tab used for creating abstract base classes.
"""

from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def render(self): ...

class Text(Renderable):
    def __init__(self, text):
        self.text = text
    def render(self):
        return self.text

class UppercaseText(Text):
    def render(self):
        return self.text.upper()

class Money(Renderable):
    def __init__(self, money, currency='$'):
        self.money = money
        self.currency = currency

    def render(self):
        return f'{self.currency}{self.money}'


if __name__ == '__main__':
    renderables = [
        Text('hello person'),
        UppercaseText('hello person'),
        Money(3.14)
    ]

    for renderable in renderables:
        print(renderable.render())

"""
For this application there is no obvious default implementation for the render method. 
An abstract base class is an optimal choice in this use case. 
It ensures that classes with Renderable in the base class hierarchy must implement the render method.


"""

