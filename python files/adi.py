uname = 'Admin'
pwd = 'kzkww0fv5b'

while True:
    username = input('Enter Username here : ')
    password = input('Enter password here : ')
    if uname != username:
        print('Invalid username')
    if pwd != password:
        print('Invalid password')
    if uname == username and pwd == password:
        print('Login sucessfull...')
        break