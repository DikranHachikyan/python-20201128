
def main():
    tpl = 1,2,3,4,5

    for key,value in enumerate(tpl, 3):
        print(f'key = {key}, value={value}')

    print('-- main --')

######################
main()