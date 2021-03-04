import password
from os import path
import make_table
from time import strftime
import json
import encode

def backup(lst, clear, path_to_file, path_to_key, home):
    path_for_backup = backup_path(home, lst, clear)
    if path_for_backup == '0':
        pass
    else:
        make_backup(lst, path_for_backup, path_to_key, path_to_file, clear)

def backup_path(home, lst, clear):
    make_table.from_list(lst, clear)
    print()
    print('Enter path when create backup or press Enter, 0 - back')
    print(f"Default path: {home}")
    print()
    p = input('Path: ')
    if len(p.strip()) == 0:
        p = home
    else:
        if path.exists(p) is True:
            if path.isdir(p) is True:
                return p
            else:
                make_table.from_list(lst, clear)
                print()
                print('No path. Press Enter')
                input()
                p = backup_path(home, lst, clear)
        else:
            make_table.from_list(lst, clear)
            print()
            print('No path. Press Enter')
            input()
            p = backup_path(home, lst, clear)
    return p

#def backup_password(lst, clear):
#    make_table.from_list(lst, clear)
#    print()
#    return backup_password


def restore(lst, clear, path_to_key):
    pass

def make_backup(lst, folder_for_backup, path_to_key, path_to_file, clear):
    passwd = password.check_password(path_to_file, clear)
    lst_encode = []
    for i in lst:
        j = {}
        for key, value in i.items():
            j[key] = encode.encode(passwd, value)
        with open(f"{path_to_key}/{encode.decode(passwd, j['key'])}") as f:
            key_entry = f.readlines()
            f.close()
        j['key_entry'] = key_entry
        lst_encode.append(j)
    with open(f'{folder_for_backup}/{strftime("%Y%m%d-%H%M%S")}.ssmb', 'w') as f:
        f.write(f"{encode.encode(passwd, passwd)}\n")
        for i in json.dumps(lst_encode):
            f.write(i)
        f.close()

    print('make backup in develop')
    input()


def create_password():
    return passwd
