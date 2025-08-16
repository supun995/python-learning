"""
Method delegation can assist with the diamond problem by delegating method calls to base classes.
The built-in super callable used with single inheritance returns the base class.
When used with multiple inheritance the super callable demonstrates its true power.

Consider the following goal: create a dictionary that normalizes keys as lowercase alphanumeric characters.
This can be easily accomplished by using the built-in dict type as a base class.
"""

from collections import defaultdict

def normalize_key(key):
    return ''.join([char.lower() for char in key if char.isalpha()])

class NormalizedDict(dict):
    def __setitem__(self, k, v):
        super().__setitem__(normalize_key(k), v)

    def __getitem__(self, k):
        return super().__getitem__(normalize_key(k))

#The below AdjustedValueDict also derives from the built-in dict class.
# It overrides the constructor and the __setitem__ method and delegates to the base class.
# The constructor accepts a numeric value used to multiply the value prior to setting.
class AdjustedValueDict(dict):
    def __init__(self, factor, *args, **kwargs):
        self.factor = factor
        super().__init__(*args, **kwargs)

    def __setitem__(self, k, v):
        super().__setitem__(k, v * self.factor)


#*args	Collects extra positional args	Tuple greet("Alice", "Bob", "Charlie")
#**kwargs	Collects extra keyword args	Dictionary print_info(name="Alice", age=30, city="New York")

if __name__ == '__main__':
    scores = NormalizedDict()
    scores['Ada Lovelace'] = 1_314
    scores['Carl Sagan  '] = 1_236
    scores['Grace Hopper'] = 2_349

    print(scores)
    print(NormalizedDict.mro())



