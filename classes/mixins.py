"""
Mixins are another common use case for multiple inheritance in Python.
Mixins are not intended to be instantiated and used directly.
They're used to provide commonly required functionality to derived classes.
 For example, an authentication mixin might add user authentication functionality to classes used for handling web requests.
"""
"""
The below AuthMixin class is used to add authentication-related functionality to derived classes. 
Notice the use of self.header in the is_authenticated method. 
This attribute is not defined as part of the AuthMixin class.
Mixin classes enhance derived classes and are not intended to be used as standalone classes.
The AuthMixin class requires that derived classes include a header attribute.
"""
import json

class AuthMixin:
    def is_authenticated(self):
        return self.header.get('token', '') == '0x24'

#@property -This makes as_json accessible like an attribute: data = response.as_json
class JSONMixin:
    @property
    def as_json(self):
        if not self.header.get('Content-Type', '').lower() == 'application/json':
            raise ValueError('unexpected content type')
        return json.loads(self.body)


class Request(AuthMixin, JSONMixin):
    def __init__(self, header, body):
        self.header = header
        self.body = body

    def process(self):
        if not self.is_authenticated():
            return 'invalid user'
        return self.as_json



if __name__ == '__main__':
    print(Request({'token': '0x24', 'Content-Type': 'application/json'}, '[0, 1, 2, 3, 5]').process())
    print(Request({'token': 'xxxx', 'Content-Type': 'application/json'}, '[6, 7, 8, 9, 5]').process())


"""
What is a Mixin Class?
A mixin is a special kind of class designed only to add reusable behavior to other classes through inheritance, without being a standalone class on its own.

Key Points:
Mixins provide additional methods or properties.
They don’t define their own state or main identity.
Used to compose functionality in classes without duplicating code.
Usually, mixins are small and focused on a single capability.

Why Use Mixins?
Imagine you have multiple classes that need logging functionality or serialization methods. 
Instead of rewriting those methods everywhere, you write a mixin class and inherit it wherever needed.
"""


class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class User(LoggerMixin):
    def __init__(self, name):
        self.name = name

    def greet(self):
        self.log(f"Greeting from {self.name}")
        print(f"Hello, {self.name}!")


class Product(LoggerMixin):
    def __init__(self, title):
        self.title = title

    def display(self):
        self.log(f"Displaying product: {self.title}")
        print(f"Product: {self.title}")



