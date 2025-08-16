import time

class BlockTimer:
    ''' Times how long it takes for the block of code to complete. '''

    def set_start_time(self):
        self.start = time.perf_counter()

    def set_close_time(self):
        close = time.perf_counter()
        print(f'block completed in {close - self.start:0.5f} seconds.')

    ''' Times how long it takes for the block of code to complete. 


        Requirements:
            Implement the context manager protocol for this class.

            Call the set_start_time method when entering the context.
            Call the set_close_time method when exiting the context.

        Example Usage:
            with BlockTimer():
                something_sorta_slow()
    '''
    def __enter__(self):
        self.set_start_time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.set_close_time()
