import json
DATA_PATH2 = 'Git_Lections/Lekce_03_14.11.24/users.json'

def read_data():
    with open(DATA_PATH2, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH2, mode="w", encoding='utf-8') as file:
        json.dump(data, file)

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError("Passwords aren't the same")

def check_username(data, username):
    if username in data:
        raise ValueError("User already exists")

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = password
    write_data(data)

def login(username, password):
    data = read_data()
    try:
        assert data[username] == password, 'Wrong password'
        return True
    except (KeyError, AssertionError):
        return False

def logout(username):
    pass

def change_password(username, old_password, new_password, password_repeat):
    data = read_data()
    if data[username] == old_password and new_password == password_repeat:
        data[username] = new_password
    else:
        raise ValueError("New Password and repeated password aren't the same. Or your actual password is wrong")
    write_data(data)

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)

# register('test', 'heslo', 'heslo')
# print(login('test', 'heslo'))
# delete_user('test', 'heslo')
change_password('test', 'heslo', 'heslo133', 'heslo133')