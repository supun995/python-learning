"""
All objects in Python possess a quality known as truthiness that determines if the object represents a bool value of True or False.
Truthiness is determined by one of two possible magic methods: __bool__ or __len__.
If the __bool__ method is implemented the runtime uses it to determine truthiness.
The __len__ method is used as a fallback. User-defined objects omitting both magic methods evaluate as True.

All built-in object types include truthiness logic.
Numeric zero values and empty sequences evaluate as False.
Most other types evaluate as True.
The __len__ method works for objects with a natural representation of length.
Using an object's length to determine truthiness works well with sequences though,
it may not work for all objects.

The __bool__ method provides more precise control over an object's truthiness. The method below checks for at least one active account to determine the truthiness of the Accounts object.
"""

class Account:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active

class Accounts:

    def __init__(self, *accounts):
        self.accs = list(accounts)

    def __len__(self):
        print('called the __len__ method.')
        return len(self.accs)

    def __bool__(self):
        print('called the __bool__ method.')
        return any(a for a in self.accs if a.active)




def demonstrate():
    accs = Accounts(
        Account('primary'),
        Account('secondary', False),
    )

    print(f'accs contains {len(accs)} accounts')
    if accs:
        print('at least one account is active')


if __name__ == '__main__':
    demonstrate()



