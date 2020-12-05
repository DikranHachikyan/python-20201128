
def main():
    app_config = {
        'title':'Text Editor',
        'version':'1.2',
        'path':'/usr/local',
        'proc':10
    }

    for key in app_config:
        print(f'param:{key} value={app_config[key]}')
        
    print('-- main --')

######################
main()