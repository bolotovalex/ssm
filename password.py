import getpass
from os import system
from encode import encode
from sys import exit as exit_cmd


def create_password(path_to_file, clear):
    system(clear)
    print('Create new password')
    password = getpass.getpass('Enter new password: ')
    if len(password) < 8:
        system(clear)
        print('Password is to short. Press enter and retype password')
        input()
        create_password(path_to_file, clear)
    else:
        password2 = getpass.getpass('Retype new password: ')
        if password != password2:
            print('Password mismatch. Press Enter and retype passwords')
            input()
            create_password(path_to_file, clear)
        else:
            system(clear)
            print('!!!WARNING!!! All data will be lose.')
            ch = input('Continue?: ')
            if ch == 'y' or ch == 'Y':
                with open(path_to_file, 'w') as f:
                    f.write(f"{encode(password, password)}\n")
                    f.write(f"[\n")
                    f.write(f"]\n")
                    f.close()
    return password


def check_password(path_to_file, clear, i=1):
    system(clear)
    password = getpass.getpass('Enter master password: ')
    with open(path_to_file, 'r') as f:
        pass_in_file = f.readline()
        f.close()
    if pass_in_file.rstrip() == encode(password, password):
        pass
    else:
        i += 1
        if i > 3:
            system(clear)
            print('3 times type wrong password. Exit')
            exit_cmd(1)
        system(clear)
        print('Wrong. Press Enter and retype password')
        input()
        password = check_password(path_to_file, clear, i)
    return password
