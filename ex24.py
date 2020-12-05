
def main():
    app_config = {
        'title':'Text Editor',
        'version':'1.2',
        'path':'/usr/local',
        'proc':10
    }

    for item in app_config.items():
        key,value = item
        print(f'param:{key} value={value}')
        
    print('-- main --')

######################
main()