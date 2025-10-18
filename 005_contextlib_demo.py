# contextlib_demo.py - contextmanager 演示
from contextlib import contextmanager

@contextmanager
def simple_context(name):
    print(f'enter {name}')
    try:
        yield
    finally:
        print(f'exit {name}')

def main():
    with simple_context('demo'):
        print('在上下文中工作')

if __name__ == '__main__':
    main()
