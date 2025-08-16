"""
Callable-based context managers are allowed to yield a single object that will be accessible via the as keyword.
The example below yields an open file that's accessible via the as keyword.
The built-in contextlib, opens in a new tab module includes many useful objects for producing and working with context managers.
The ContextDecorator base class allows context managers to be used as decorators.
The example below demonstrates the something_sorta_slow being decorated with the context class.
Calling the something_sorta_slow function results in the __enter__ method being called first, followed by something_sorta_slow, and finally __exit__ is called.

Using context managers as decorators can separate resource management from the business logic inside the decorated callable.
The ResourceLocker class in the below code inherits the ContextDecorator base class.
A module-wide instance is created named locker.
The locker instance is both a context manager and a decorator.
Decorating the change_shared_resource function ensures that a lock is acquired before the function is called.
The start_threads function creates three threads that call the change_shared_resource function.
The output demonstrates attempts made to acquire the lock for each thread.
The lock is released after the change_shared_resource function completes allowing access to the next thread.


"""

from contextlib import ContextDecorator
import random
import threading_example
import time


class ResourceLocker(ContextDecorator):

    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        print(f'{threading.get_ident()}: lock acquiring.')
        self.lock.acquire()
        print(f'{threading.get_ident()}: lock acquired.')

    def __exit__(self, *exc_info):
        print(f'{threading.get_ident()}: lock releasing.')
        self.lock.release()
        print(f'{threading.get_ident()}: lock released.')

locker = ResourceLocker()

@locker
def change_shared_resource():
    print(f'{threading.get_ident()}: resource changed.')
    time.sleep(random.randint(1, 10))

def start_threads():
    threads = [threading.Thread(target=change_shared_resource) for i in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    start_threads()


"""
Using context managers as decorators can separate resource management from the business logic inside the decorated callable. 
The ResourceLocker class in the below code inherits the ContextDecorator base class. 
A module-wide instance is created named locker. 
The locker instance is both a context manager and a decorator. 
Decorating the change_shared_resource function ensures that a lock is acquired before the function is called. 
The start_threads function creates three threads that call the change_shared_resource function. 
The output demonstrates attempts made to acquire the lock for each thread. 
The lock is released after the change_shared_resource function completes allowing access to the next thread
Notice that only the thread holding the lock is able to call the change_shared_resource function. 
Each thread attempts to acquire a lock as soon as the change_shared_resource function is called. 
The lock ensures the acquire method doesn't complete until the lock can be acquired.
"""