import asyncio
import logging
from contextlib import asynccontextmanager
from functools import wraps


class AsyncResourceLocker:
    def __init__(self, name: str = "AsyncLocker"):
        self.lock = asyncio.Lock()
        self.name = name
        self.logger = logging.getLogger(name)

    @asynccontextmanager
    async def context(self):
        task_name = asyncio.current_task().get_name()
        self.logger.info(f'{task_name}: acquiring lock...')
        await self.lock.acquire()
        self.logger.info(f'{task_name}: lock acquired.')

        try:
            yield
        except Exception as e:
            self.logger.error(f'{task_name}: Exception - {type(e).__name__}: {e}')
            raise
        finally:
            self.logger.info(f'{task_name}: releasing lock...')
            self.lock.release()
            self.logger.info(f'{task_name}: lock released.')

    def __call__(self, func):
        """Allow the locker to be used as a decorator for async functions."""
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with self.context():
                return await func(*args, **kwargs)
        return wrapper
