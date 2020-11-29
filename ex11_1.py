
def main():
    num = float(input('num = '))
    output = ''

    if num >= 0:
        output = f'{num} is positive number'
    else:
        output = f'{num} is negative number'

    print(output)
    print('---------')

######################
main()