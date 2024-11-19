from users import login, register

while True:
    username = input('Zadej username: ')
    password = input('Zadej heslo: ')
    success = login(username, password)
    if success:
        print('Ok')
    else:
        print('Invalid data')