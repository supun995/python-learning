

"""
import threading
import time

def task():
    print("Start")
    time.sleep(2)
    print("End")

thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)
thread1.start()
thread2.start()
#Both threads start immediately and sleep at the same time → parallel behavior

import time
from concurrent.futures import ThreadPoolExecutor

def blocking_task(n):
    print(f"Task {n} start")
    time.sleep(2)  # blocking
    print(f"Task {n} done")
    return n

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    results = list(executor.map(blocking_task, range(3)))

end = time.perf_counter()
print(f"Total time: {end - start:.2f} seconds")
"""
"""

"""




