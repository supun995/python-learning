import asyncio
import logging
from async_locker import AsyncResourceLocker

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Create locker instance
locker = AsyncResourceLocker("MyResourceLocker")

@locker
async def update_shared_resource():
    print(f"{asyncio.current_task().get_name()}: working with resource...")
    await asyncio.sleep(1)
    print(f"{asyncio.current_task().get_name()}: done.")

async def main():
    tasks = [asyncio.create_task(update_shared_resource(), name=f'Task-{i}') for i in range(3)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())