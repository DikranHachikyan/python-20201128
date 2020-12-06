# глобална променлива
port = 3306
# 1. дефиниция на функцията
def sum_numbers(a, b, d = 0):
    # c - локална променлива (вижда се само тук)
    c = a + b + d
    return c
    # print('sum_number')


if __name__ == '__main__':
    # 2. Извикване на функцията
    res = sum_numbers(5,6)
    print(f'5 + 6 = {res}')

    x, y, z = 7, 8, 10

    res = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {res}')