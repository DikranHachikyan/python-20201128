
def main():
    # 1 + 2 + 3 + ... + 100 = 5050
    i = 1
    suma = 0

    while i <= 100:
        suma += i
        i += 1

    print(f'1+2+...+99+100={suma}')

    print('-- main --')

######################
main()