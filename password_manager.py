from cryptography.fernet import Fernet

master_password = input('Create a master password: ')


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


write_key()


def add():
    name = input('Account name: ')
    password = input('Password: ')
    with open('password_manager.txt', 'a') as f:
        f.write(f'{name} | {password}\n')


def view():
    with open('password_manager.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split('|')
            print(f'User: {user} Password: {pwd}')


print('Would you like to add a new password or view existing ones?')
print('(--- Press q to exit application ---)')

while True:
    mode = input('Enter your choice (add or view or q) : ').lower()

    if (mode == 'q'):
        print('Good Bye!')
        break
    elif (mode == 'add'):
        add()
    elif (mode == 'view'):
        view()
    else:
        print('Invalid input. Try again!')
        continue
