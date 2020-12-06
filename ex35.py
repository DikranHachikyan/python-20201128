# глобална променлива
def show2(title, a=100, *, kw1='A',kw2='B', **kwargs):
    pass
# 1. дефиниция на функцията
def show(title, a=100, *args, kw1='A',kw2='B', **kwargs):
    print(f'Title:{title}')

    print(f'a={a}')

    print('Args:')
    for v in args:
        print(f'arg:{v}',end = ' ')
    print()

    print('Kwargs:')
    if 'path' in kwargs:
        print(f"path={kwargs['path']}")
    if 'log' in kwargs:
        print(f"log={kwargs['log']}")

    print('Keyword-only arguments')
    print(f'kw1 = {kw1} kw2 = {kw2}')
    print('-' * 20)


if __name__ == '__main__':
    # 2. Извикване на функцията
    show('Text Editor')
    
    show('Text Editor',2)

    show('Text Editor',2, 10,20,30,40)

    show('Text Editor',2, 10, 20, 30, 40, log='messages.log', path='/usr/local')

    app_config = {
        'path':'/usr/local',
        'log':'/var/log/messages.log',
        'n_proc':10,
        'max_mem':4096
    }
    
    show('Text Editor',2, 10, 20, 30, 40, **app_config)

    show('Text Editor', 100, *(10,20,30,40))

    show('Text Editor',2, 10, 20, 30, 40, kw2='Z', kw1='X', **app_config)
    
    show('Text Editor', kw2='Z', kw1='X', **app_config)
