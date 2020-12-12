# глобална променлива

def foo(a = [], b = {}):
    print(f'a={a}')
    print(f'b={b}')
    print('-' * 20)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == '__main__':
    # 2. Извикване на функцията
    foo()
    foo([1,2,3], {'B':100})
    foo()
    foo()
    foo([11,22,33,44], {'B':100, 'C':150})
    foo()
    