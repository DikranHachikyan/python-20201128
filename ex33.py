# глобална променлива

# 1. дефиниция на функцията
def sort_priority(values, group):
    found = False # scope sort_priority
    def helper(el):
        nonlocal found
        if el in group:
            found = True
            return (0,el)
        return (1,el)

    values.sort(key=helper )
    return found


if __name__ == '__main__':
    # 2. Извикване на функцията
    numbers = [1,5,2,4,3,9,8,7,6]
    group = {5,4,3}

    res = sort_priority(numbers, group)
    print(f'res={res} {numbers}')