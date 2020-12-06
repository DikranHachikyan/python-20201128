# глобална променлива

def sum_numbers(n):
    if n > 0:
        return n + sum_numbers(n-1)
    return 0

if __name__ == '__main__':
    # 2. Извикване на функцията
    res = sum_numbers(5)

    print(f'res = {res}')