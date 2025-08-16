"""
RLock (Reentrant Lock) allows the same thread to acquire the lock multiple times, useful in nested calls.
Ensures that even if something goes wrong inside the function, the lock is still released.Handle Exceptions in __exit__ .
A Semaphore(n) allows up to n threads to enter the critical section concurrently.Good when multiple readers are okay, but not too many.self.lock = threading.Semaphore(2)

"""

from contextlib import ContextDecorator
import threading
import time
import random

class ResourceLocker(ContextDecorator):
    def __init__(self):
        self.lock = threading.RLock()  # use reentrant lock

    def __enter__(self):
        print(f'{threading.get_ident()}: lock acquiring...')
        self.lock.acquire()
        print(f'{threading.get_ident()}: lock acquired.')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{threading.get_ident()}: lock releasing...')
        self.lock.release()
        print(f'{threading.get_ident()}: lock released.')

        if exc_type:
            print(f'Exception: {exc_type.__name__}: {exc_val}')
            return False  # don't suppress the error

locker = ResourceLocker()

@locker
def change_shared_resource():
    print(f'{threading.get_ident()}: working...')
    time.sleep(random.uniform(1, 3))
    if random.random() < 0.3:
        raise RuntimeError("simulated error")
    print(f'{threading.get_ident()}: done.')

def start_threads():
    threads = [threading.Thread(target=change_shared_resource) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_threads()