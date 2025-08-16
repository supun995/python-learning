import asyncio
from contextlib import asynccontextmanager


class AsyncResourceLocker:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def __aenter__(self):
        print(f'{asyncio.current_task().get_name()}: acquiring lock...')
        await self.lock.acquire()
        print(f'{asyncio.current_task().get_name()}: lock acquired.')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f'{asyncio.current_task().get_name()}: releasing lock...')
        self.lock.release()
        print(f'{asyncio.current_task().get_name()}: lock released.')

        if exc_type:
            print(f'Exception: {exc_type.__name__} - {exc_val}')
            return False  # propagate exception


locker = AsyncResourceLocker()

async def async_change_shared_resource():
    async with locker:
        print(f'{asyncio.current_task().get_name()}: working...')
        await asyncio.sleep(1)
        print(f'{asyncio.current_task().get_name()}: done.')

async def main():
    tasks = [asyncio.create_task(async_change_shared_resource(), name=f'Task-{i}') for i in range(3)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())

"""
Feature	Description
async with	Enters an async context manager (__aenter__, __aexit__)
asyncio.Lock()	Prevents multiple coroutines from entering the critical section
asyncio.create_task()	Runs multiple async tasks concurrently
asyncio.run()	Entry point for running async programs

The difference between synchronous (sync) and asynchronous (async) methods in Python comes down to how they handle execution and waiting (blocking) — especially when dealing with I/O-bound operations like:
waiting for HTTP responses
reading/writing files
sleeping
querying a database
acquiring locks

Asynchronous code uses async def functions, and can pause and resume operations using await. 
This enables concurrent behavior within a single thread.
"""