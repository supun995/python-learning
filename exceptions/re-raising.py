"""

Exception handling is not always easy to implement well.
Ineffective exception handling can introduce unexpected application behaviors.
This lab step focuses on ensuring that exceptions are handled or re-raised.
Exception handlers that don't resolve the exceptional condition can hide errors
"""

import json
from pathlib import Path

def deserialize(data: str) -> dict:
    return json.loads(data)

def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError:
        print('unexpected file format.')
    except FileNotFoundError:
        print('missing required file.')
    except ValueError:
        print('non-numeric payment amount.')
    except Exception as ex:
        print('unplanned exception.')

''''''
def summarize_monthly():
    path = Path(__file__).parent / 'payments.json'
    try:
        with open(path) as p:
            payments = deserialize(p.read())

            return { month: sum(payment) for month, payment in payments['months'].items() }
    except KeyError:
        print('unexpected file format.')
        raise
    except FileNotFoundError:
        print('missing required file.')
        raise
    except ValueError:
        print('non-numeric payment amount.')
        raise
    except Exception as ex:
        print('unplanned exception.')
        raise
