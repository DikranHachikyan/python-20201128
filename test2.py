# глобална променлива

def sum_nested(lst):
    res = 0

    for _ , el in enumerate(lst):
        if type(el) is not int:
            res += sum_nested(el)
        else:
            res += el
    return res


if __name__ == '__main__':
    # 2. Извикване на функцията
    arr = [1,2,3,[5,6,[7]],4]
    print(f'sum={sum_nested(arr)}')