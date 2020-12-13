# глобална променлива

def find_key(key, **kwargs):
    try:
        print(f'{key} => {kwargs[key]}')
    except KeyError:
        raise 
    
if __name__ == '__main__':
    
    connection = {
        'host':'localhost',
        'port':3306,
        'service':'mysql'
    }

    find_key('host', **connection)
    find_key('ip', **connection)
    