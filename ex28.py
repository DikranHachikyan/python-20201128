# глобална променлива
port = 3306
# 1. дефиниция на функцията
def sum_numbers(a,b):
    # c - локална променлива (вижда се само тук)
    c = a + b
    return c
    # print('sum_number')


if __name__ == '__main__':
    # 2. Извикване на функцията
    res = sum_numbers(5,6)
    print(f'5 + 6 = {res}')

    x,y = 7,8

    res = sum_numbers(x,y)
    print(f'{x} + {y} = {res}')