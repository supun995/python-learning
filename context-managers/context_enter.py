class Datastore:

    def __init__(self, datasource):
        if datasource in 'S7 H1 B4'.split():
            self.datasource = datasource
        else:
            raise Exception('invalid datasource')

    def __enter__(self):
        self.dataset = open(self.datasource, 'w')
        return self.dataset

    def __exit__(self, exc_type, exc_value, traceback):
        self.dataset.close()

if __name__ == '__main__':
    with Datastore('S7') as dataset:
        dataset.write('inside the context')

