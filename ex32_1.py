# глобална променлива
c = 3306
# 1. дефиниция на функцията
def show():
    global c
    c = 10
    print(f'c={c}')


if __name__ == '__main__':
    # 2. Извикване на функцията
    print(f'before c = {c}')
    show()
    print(f'after c = {c}')