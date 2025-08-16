#Idiomatic Python follows the philosophy that it's better to ask for forgiveness than permission.

#ask for permission
import json
from pathlib import Path

dataset_path = Path('dataset.json')

if dataset_path.exists():
    with open(dataset_path) as dataset:
        ds = json.loads(dataset.read())
        ...

#ask for forgiveness

try:
    with open('dataset.json') as dataset:
        ds = json.loads(dataset.read())
        ...
except OSError:
    print('missing dataset file')

"""
The ask for permission model attempts to identify likely issues such as missing files throughout the code. This model merges necessary operations with defensive code used to prevent possible exceptions. This can add a non-trivial amount of code as applications grow and evolve. It also performs more operations than are strictly required.

The ask for forgiveness model defines the necessary operations to perform a specific task and handles exceptions if they occur. This model focuses on writing code based on the normal code flow and handling resulting exceptions. The Python community commonly ascribes to this model.
"""

