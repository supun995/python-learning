"""
Single inheritance represents a chain of base classes. The runtime searches for methods in a specific order. First the current class is checked before working up through the hierarchy all the way up to the root object base class. The conceptual simplicity of single inheritance makes it relatively intuitive to understand.
Multiple inheritance is a far less straightforward concept which requires careful design to avoid common pitfalls. Many programming languages/runtimes are intentionally limited to single inheritance to avoid the potential complexity. Multiple base classes might include implementations of the same method.
"""
"""
The "diamond problem" (sometimes referred to as the "Deadly Diamond of Death"[6]) is an ambiguity that arises when two classes B and C inherit from A, and class D inherits from both B and C.
 If there is a method in A that B and C have overridden, and D does not override it, then which version of the method does D inherit: that of B, or that of C?
 The runtime includes logic to determine the order that base classes are checked for a requested method. 
 This is referred to as the method resolution order, commonly abbreviated mro.
  Every object type includes a list of base classes representing the method resolution order.
The runtime uses the 
C3 linearization algorithm
, opens in a new tab to determine the method resolution order.

Guido van Rossum the creator of Python describes C3 thusly:

Basically, the idea behind C3 is that if you write down all of the ordering rules imposed by inheritance relationships in a complex class hierarchy, the algorithm will determine a monotonic ordering of the classes that satisfies all of them. If such an ordering can not be determined, the algorithm will fail.

While the C3 algorithm is outside the scope of this lab, here's a summary of how it impacts the method resolution order.

Derived classes are checked before base classes.
Classes inheriting from multiple base classes maintain the base class order specified in the class definition.
Classes are never repeated.
"""


class A:
    def run(self):
        print('a')


class B(A):
    def run(self):
        print('b')


class C(A):
    def run(self):
        print('c')


class D(C, B): ...



if __name__ == '__main__':
    D().run()

    print('as method', D.mro())
    print('attribute', D.__mro__)

"""
Multiple inheritance is omitted in many other programming languages/runtimes due to the potential method resolution ambiguity. Effective multiple inheritance requires careful design in order to avoid tangled object hierarchies that are difficult to maintain. Two common use cases for multiple inheritance include method delegation and mixins.
"""