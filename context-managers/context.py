class Context:

    def __enter__(self):
        print('context opened')

    def __exit__(self, exc_type, exc_value, traceback):
        print('context closed')

class ContextA:

    def __enter__(self):
        print('context opened')

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'{exc_type=}')

if __name__ == '__main__':
    with Context():
        print('inside the context')
    print('now outside of the context')


    with ContextA():
        raise Exception('error')
    print('now outside of the context')

