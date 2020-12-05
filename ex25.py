
def main():
    lst = [ x ** 2 for x in range(10)]
    txt = 'hello python'

    print(f'values = {lst}')

    letters = [ f'--{t}--' for t in txt]

    print(f'letters = {letters}')
    print('-- main --')

######################
main()