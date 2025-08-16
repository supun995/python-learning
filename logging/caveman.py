import json
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))


# For the sake of this lab, pretend that you don't already have access to the data in the json file.
def fetch_dataset(source: str = os.path.join(current_dir, 'caveman.json')):
    with open(source, 'r') as dataset:
        return json.loads(dataset.read().encode('utf8'))


def normalize_name(dataset, key: str) -> list:
    ''' Removes white space around the text and converts to title case.

        Args:
            dataset | a dictionary-like structure.
            key     | a str representing the key used to look
                    |> up names in the dataset.
    '''
    print(dataset)
    try:
        return [name.strip().title() for name in dataset[key]]
    except KeyError:
        return []
    except:
        raise


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        clean_dataset = normalize_name(fetch_dataset(), sys.argv[1])

        if clean_dataset:
            print('The cleaned dataset: ', end='')
            print(*clean_dataset, sep=', ')
        else:
            print('data not found')

    else:
        print('missing required dataset key')
        print('example: python3 caveman.py "keyname"')