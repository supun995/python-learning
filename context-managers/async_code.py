import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Non-blocking
    print("Data fetched.")

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    await task1
    await task2

asyncio.run(main())

"""
Asynchronous code uses async def functions, and can pause and resume operations using await. 
This enables concurrent behavior within a single thread.
"""