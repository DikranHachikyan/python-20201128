# глобална променлива

def find_key(key, **kwargs):
    if key not in kwargs:
        raise KeyError(f'key {key} not found')
    
    print(f'{key} => {kwargs[key]}')

         
    
if __name__ == '__main__':
    
    connection = {
        'host':'localhost',
        'port':3306,
        'service':'mysql'
    }

    try:
        find_key('host', **connection)
        find_key('ip', **connection)
    except KeyError as e:
        print(e)