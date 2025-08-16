"""
From inside an exception handler the raise keyword can pair with the from keyword to produce an exception chain.
This allows custom exceptions to provide specific details without losing the original exception.

"""

import json
from pathlib import Path
import sys

"""
-> dict:
This is another type hint for the return value. It says the function will return a dict (dictionary).
"""

def deserialize(data: str) -> dict:
    return json.loads(data)

class BillingSummaryError(Exception): ...

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from ex
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from ex
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from ex
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from ex

"""
Passing a None value to the from keyword causes the original exception to be suppressed.
def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError as ex:
        raise BillingSummaryError('unexpected file format.') from None
    except FileNotFoundError:
        raise BillingSummaryError('missing required file.') from None
    except ValueError:
        raise BillingSummaryError('non-numeric payment amount.') from None
    except Exception as ex:
        raise BillingSummaryError('unplanned exception.') from None
"""

