"""
Encapsulation is an object-oriented programming (OOP) principle that focuses on bundling data (attributes) and methods (functions) into a single unit—a class—and restricting direct access to some of the object's components.
public	No underscore	Can be accessed from anywhere
_protected	One underscore	Intended for internal use (by convention)
__private	Two underscores	Name mangling (harder to access directly)
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._account_type = 'savings'  # protected (by convention)
        self.__balance = balance    # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
print(acc.owner)            # OK: public
print(acc._account_type)    # OK but discouraged
#print(acc.__balance)      # ❌ Error: AttributeError
print(acc.get_balance())    # ✅ Access through method