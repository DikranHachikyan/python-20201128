# глобална променлива

# def first_element(el):
#     return el[1]

if __name__ == '__main__':
    sq = lambda a: a ** 2

    pw = lambda a: a ** 2 if a % 2 else a ** 3


    # 1.
    # print(f'4 ^ 2 = {sq(4)}')
    # print(f'pw(3) = {pw(3)}')
    # print(f'pw(4) = {pw(4)}')

    items = [('A', 5, 7), ('D', 2, 6), ('B', 4, 8), ('D', 2, 5)]
    # 2.
    # items.sort()
    # print(f'in-place,default sorted:{items}')

    # 3.
    # items.sort(key = first_element )
    # items.sort(key = lambda el: el[1] )
    
    # 4.
    items.sort(key = lambda el: (el[1],el[0],el[2]) )
    print(f'sorted:{items}')


    values = [2,5,7,9,4]
    for v in map( lambda e: e ** 2, values):
        print(v)

