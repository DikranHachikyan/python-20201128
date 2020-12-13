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
    except ValueError:
        print('Invalid Value')
    except KeyError:
        print('Unsupported operation')
    except :
        print('Unknown error')
    else:
        print('-- else block --')
    finally:
        print('-- finally block --')