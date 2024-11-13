data = {
    'Dimo' : '26290815796',
    'Julia' : '15796262908',
    'Spolu' : '2629081579615796262908'
}

username = input('Zadej username: ')
password = input('Zadej heslo: ')
error_text = 'Wrong username or password'

"""
print(username, password)
if username in data :
    if password == data[username] :
        print('ok')
    else:
        print(error_text)
else: 
    print(error_text)
"""

try:
    assert password == data[username]
    print('Ok')
except:
    print(error_text)