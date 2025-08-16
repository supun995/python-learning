from contextlib import contextmanager

@contextmanager
def datastore(datasource):
    try:
        if datasource not in 'S7 H1 B4'.split():
            raise Exception('invalid datasource')

        dataset = open(datasource, 'w')
        yield dataset
    finally:
        dataset.close()


if __name__ == '__main__':
    with datastore('H1') as dataset:
        dataset.write('Context managers are cool.')






