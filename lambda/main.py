"""
Python's language syntax includes rules for creating inline callables named lambda functions.
Lambda functions are anonymous (unnamed) functions used to return the results of a single expression.
Lambda functions are commonly passed to higher order functions.
Python's language syntax includes rules for creating inline callables named lambda functions.
Lambda functions are anonymous (unnamed) functions used to return the results of a single expression.
Lambda functions are commonly passed to higher order functions.

Higher order functions are functions that accept and or return functions.
The standard library includes several higher order functions such as:
filter
map
min
sorted
"""

# add = lambda x, y=10: x + y
# assert add(1, 1) == 2
# assert add(1) == 11

normalize_name = lambda name, prefix='': f'{prefix} {name}'.title()

print(normalize_name('ada lovelace', 'countess'))


add = lambda a, b, c=10, /: a + b + c

print(add(5, 5))
print(add(5, 5, 5))


words = 'blue gone map yes main bird calm row to'.split()

for word in filter(lambda w: len(w) <= 3, words):
    print(word)

    # List of initials
people = ['K A', 'R O', 'L G', 'B B']

# Omitting a sort key uses the default sorting for the provided object type.
print(sorted(people))

# Sort by the initial of last name.
print(sorted(people, key=lambda p: p.split()[-1]))

#Lambda functions are useful for mocking and or patching other callables. Incorporating them judiciously into unit tests can improve readability.
class Datastore:

    def __init__(self):
        self.data = dict(zip(['a', 'b', 'c'], [100, 200, 300]))

    def query(self, endpoint, key, timeout=20):
        return self.data[key]


datastore = Datastore()
results = datastore.query('fake.database', 'b', timeout=10)
print('original ', results)

# replace the query method of the object bound to: datastore
datastore.query = lambda *_args, **_kwargs: 200
results = datastore.query('fake.database', 'b', timeout=10)
print('lambda   ', results)








