# глобална променлива
port = 3306
# 1. дефиниция на функцията
def sum_numbers(a, b, *args):
    # c - локална променлива (вижда се само тук)
    print(f'{args}')
    c = a + b
    for v in args:
        c += v
    return c
    # print('sum_number')


if __name__ == '__main__':
    # 2. Извикване на функцията
    res = sum_numbers(5,6)
    print(f'5 + 6 = {res}')

    x, y, z = 1, 2, 3

    res = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {res}')
    
    res = sum_numbers(x, y, 4, 5, 6, 7, 8)
    print(f'{x} + {y} + 4 + 5 + 6 + 7 + 8 = {res}')

    ls = [ v for v in range(3,15)]

    res = sum_numbers(x, y, *ls)
    print(f'{x} + {y} + '  + ' + '.join([str(v) for v in ls]) + f'={res}')
