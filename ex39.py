# глобална променлива

def get_squares(n):
    return [ v ** 2 for v in range(n+1)]

# 1. дефиниция
def generate_squares(n):
    for v in range(n+1):
        yield v ** 2

if __name__ == '__main__':
    values = get_squares(10)

    print(f'values={values}')
    
    # 2. Присвояване на функцията на променлива
    n_sqr = generate_squares(10)

    print(type(generate_squares))
    print(type(n_sqr))

    print(f'1 -> {next(n_sqr)}')
    print(f'2 -> {next(n_sqr)}')
    print(f'3 -> {next(n_sqr)}')
    print(f'4 -> {next(n_sqr)}')
    print(f'5 -> {next(n_sqr)}')

    lst = list(n_sqr)
    print(f'lst = {lst}')

    sqr_5 = generate_squares(5)

    for i in sqr_5:
        print(f'i={i}')