import getpass
from os import system
import encode

def create_password(path_to_file, clear):
    system(clear)
    print('Create new password')
    password = getpass.getpass('Enter new password: ')
    if len(password) < 8:
        system(clear)
        print('Password is to short. Press enter and retype password')
        input()
        create_password()
    else:
        password2 = getpass.getpass('Retype new password: ')
        if password != password2:
            print('Password mismatch. Press Enter and retype passwords')
            input()
            create_password()
        else:
            system(clear)
            print('!!!WARNING!!! All data will be lose.')
            ch = input('Continue?: ')
            if ch == 'y' or ch == 'Y':
                with open(path_to_file, 'w') as f:
                    f.write(encode.encode(password, password))
                    f.close()
    return password

def check_password(path_to_file, clear):
    system(clear)
    password = getpass.getpass('Enter master password: ')
    with open(path_to_file, 'r') as f:
        pass_in_file = f.readline()
        if pass_in_file == encode.encode(password, password):
            return password
        else:
            system(clear)
            print('Wrong')
            exit()



