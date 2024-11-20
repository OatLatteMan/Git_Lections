import json, hashlib
DATA_PATH2 = 'Lekce_03_14.11.24/users.json'

def hash_password(password):
    hash_value = hashlib.sha256(password.encode())
    return hash_value.hexdigest()

def read_data():
    with open(DATA_PATH2, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH2, mode="w", encoding='utf-8') as file:
        json.dump(data, file)

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError("Passwords aren't the same")
    return True

def check_username(data, username):
    if username in data:
        raise ValueError("User already exists")

def logging_in(data, logged_in):
    if data[logged_in] == 'False':
        data[logged_in] = 'True'
        write_data(data)
        return True
    else:
        return 'User is already logged in'

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = hash_password(password)
    write_data(data)

# def register(username, password, password_repeat, logged_in):
#     check_password(password, password_repeat)
#     data = read_data()
#     check_username(data, username)
#     data[username] = hash_password(password)
#     data[logged_in] = "False"
#     write_data(data)

def login(username, password):
    data = read_data()

    try:
        assert data[username] == hash_password(password), 'Wrong password'
        return True
    except (KeyError, AssertionError):
        return False
    
# def login(username, password, logged_in):
#     data = read_data()

#     try:
#         assert data[username] == password, 'Wrong password'
#         logging_in(data, logged_in)
#         return True
#     except (KeyError, AssertionError):
#         return False

def logout(logged_in):
    data = read_data()
    data[logged_in] = 'False'
    write_data(data)
    if data[logged_in] == 'False':
        return 'Logged out'

def change_password(username, old_password, password, password_repeat):
    data = read_data()
    if data[username] == old_password and check_password(password, password_repeat):
        data[username] = password
        write_data(data)
    else:
        raise ValueError("New Password and repeated password aren't the same. Or your actual password is wrong")
    
# def change_password(username, old_password, password, password_repeat):
#     data = read_data()
#     if data[username] == old_password and password == password_repeat:
#         data[username] = password
#         write_data(data)
#     else:
#         raise ValueError("New Password and repeated password aren't the same. Or your actual password is wrong")

def delete_user(username, password, logged_in):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        del data[logged_in]
        write_data(data)

def text():
    register('test', 'heslo', 'heslo', 'logged_in')
    print(login('test', 'heslo', 'logged_in'))
    print(logout('logged_in'))
    delete_user('test', 'heslo133', 'logged_in')
    change_password('test', 'heslo', 'heslo133', 'heslo133')

def test2():
    register('test123', 'heslo', 'heslo')

# test2()

change_password('test', 'heslo', 'heslo133', 'heslo133')