# глобална променлива



if __name__ == '__main__':

    actions = {
        '+': lambda a,b: a+b
    }

    try:
        a = float(input('value of a:'))
        op = input('Action (+, -, *, /):')
        b = float(input('value of b:'))

        print(f'{a} {op} {b} = {actions[op](a,b)}')
    except ValueError as e:
        print(f'Invalid Value ({e})')
    except KeyError:
        print(f'Unsupported operation {e}')
    except Exception as e:
        print(f'Unknown error({e}) ')
    else:
        print('-- else block --')
    finally:
        print('-- finally block --')