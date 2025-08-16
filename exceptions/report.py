from datetime import datetime

from billing import summarize_monthly

this_month = datetime.now().strftime('%b').lower()
this_month = summarize_monthly()[this_month]

print(f'The total for this month is: ${this_month}')

"""
The report module calls the summarize_monthly function and expects a dictionary to be returned. Since the None value is not a dictionary it raised an exception when attempting to access data by key.

The exception handlers in the summarize_monthly function are solely used to "log" error messages. Since these handlers are not able to take corrective action they should allow the exception to be handled by the caller.

From inside an exception handler the raise keyword instructs the runtime to re-raise the current exception. This allows a callable to perform operations before re-raising the exception. This is commonly used for logging and other clean up tasks.


"""

