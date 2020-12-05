
def main():
    users = ['anna','maria','markus','florian','john']
    mails = ['anna@no.com','maria@no.com','markus@no.com','florian@no.com']

    for data in zip(users,mails):
        name, mail = data
        print(f'user:{name} => {mail}')

    print('-- main --')

######################
main()