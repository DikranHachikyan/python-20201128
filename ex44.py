# глобална променлива

from time import time, sleep

def foo():
    sleep(0.3)

def bar():
    sleep(0.5)


def measure(func):
    t = time()
    func()
    print(f'{func.__name__}:{time() - t:.4f}')

if __name__ == '__main__':

    measure(foo)
    measure(bar)
    