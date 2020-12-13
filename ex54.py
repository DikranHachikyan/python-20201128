# глобална променлива



if __name__ == '__main__':

    actions = {
        '+': lambda a,b: a+b,
        'q': quit
    }

    while True:
        try:
            a = float(input('value of a:'))
            op = input('Action (+, -, *, /, q):')
            if op == 'q':
                actions['q']()
            b = float(input('value of b:'))

            print(f'{a} {op} {b} = {actions[op](a,b)}')
        except (ValueError, KeyError) as e:
            print(f'Invalid Value or Unsupported operation ({e})')
        except Exception as e:
            print(f'Unknown error({e}) ')
        else:
            continue
        finally:
            print('-- finally block --')