#Exceptions raised inside of a context can be suppressed by having the __exit__ method return a True value. 

class Context:

    def __enter__(self):
        print('context opened')

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f'{exc_type=}\n{exc_value}\n{traceback=}')
        return True

if __name__ == '__main__':
    with Context():
        raise Exception('error')
    print('now outside of the context')
