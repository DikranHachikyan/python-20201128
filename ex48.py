# глобална променлива

from time import time, sleep
from functools import wraps

def upper_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # args = [ str(v).upper() for v in args]
        # или
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper

def add_brackets(left = '[', right = ']'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = [ f'{left}{v}{right}' for v in args]
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_brackets(left='<', right='>')
@upper_case    
def concat(*args, **kwargs):
    '''Concatenate list elements with sep'''
    sep = kwargs.get('sep',';')
    return sep.join(args)

x = 1

if __name__ == '__main__':
    users = ['anna', 'maria','markus','jane','florian']
    print(concat(*users, sep=' # '))
    print(concat(1,2,3,4,5, sep=','))