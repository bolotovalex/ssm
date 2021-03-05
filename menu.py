import re
import make_table
from os import system, walk, remove
import check_platform
import password
from time import strftime
import io_file
import backup
from sys import exit as exit_cmd

def main_menu(lst, clear):
    print()
    print('Type number for connect or type command:')
    print(' a - Add new host')
    print(' d - Delete host')
    # print(' m - Manage key')
    print(' r - Backup / Restore db file, keys')
    print(' 0 - Exit')
    print()
    ch = input('Enter number for connect or letter for config: ')
    check_input(ch, lst, clear)

def check_input(ch, lst, clear):
    if bool(re.match(r"[0-9aAdDmMbBrRфФвВьЬиИкК]", ch)) is True:
        if bool(re.match(r"[0-9]", ch)) is True:
            if int(ch) == 0:
                system(clear)
                exit_cmd(0)

            if int(ch) > len(lst):
                make_table.from_list(lst, clear)
                print()
                print('Wrong number. Press Enter.')
                input()
            else:
                check = check_platform.check_platform()
                platform = check[5]
                path_to_keys = check[4]

                if platform == 'linux':
                    if len(lst[int(ch)-1]['key']) != 0:
                        system(clear)
                        system(f"ssh -p {lst[int(ch)-1]['port']} -i {path_to_keys}/{lst[int(ch)-1]['key']} {lst[int(ch)-1]['user']}@{lst[int(ch)-1]['host']}")
                        print('Press Enter')
                        input()
                    else:
                        system(clear)
                        system(f"ssh -p {lst[int(ch) - 1]['port']} {lst[int(ch) - 1]['user']}@{lst[int(ch) - 1]['host']}")
                        print('Press Enter')
                        input()

        if bool(re.match(r"[aAфФ]", ch)) is True:
            add_host(lst, clear)
        elif bool(re.match(r"[dDвВ]", ch)) is True:
            del_host(lst, clear)
        elif bool(re.match(r"[rRкК]", ch)) is True:
            backup_menu(lst, clear)
    else:
        make_table.from_list(lst, clear)
        print()
        print('Wrong input. Press Enter')
        input()

def add_host(lst, clear):
    make_table.from_elements(clear)
    print()
    print("Type 0 for back to main menu")
    print('Enter hostname.')
    print()
    host = input("Hostname: ")
    if len(host) == 0:
        print("Wrong hostname. Press Enter and retype hostname. To exit enter 0.")
        input()
        add_host(lst, clear)
    elif str(host) == '0':
        pass
    else:
        add_port(lst, clear, host)

def add_port(lst, clear, host):
    make_table.from_elements(clear, host)
    print()
    print("Type 0 for back to main menu")
    print(f"Enter port for {host} (Press enter for default port = 22)")
    print()
    port = input('Port: ')
    if len(port) == 0:
        print("Default 22")
        port = "22"
        add_user(lst, clear, host, port)
    elif str(port) == '0':
        pass
    elif port.isdigit() is False:
        make_table.from_elements(clear, host)
        print()
        print("Wrong port. Must be digit. Press Enter")
        input()
        add_port(lst, clear, host)
    elif int(port) < 0 or int(port) > 65536:
        make_table.from_elements(clear, host)
        print()
        print("Wrong port. Port must be 1-65536. Press Enter")
        input()
        add_port(lst, clear, host)
    else:
        add_user(lst, clear, host, port)

def add_user(lst, clear, host, port):
    make_table.from_elements(clear, host, port)
    print()
    print("Type 0 for back to main menu")
    print(f"Enter username for {host} or live blank")
    print()
    user = input('Username: ')
    if str(user) == '0':
        pass
    else:
        add_comment(lst, clear, host, port, user)

def add_comment(lst, clear, host, port, user):
    make_table.from_elements(clear, host, port, user)
    print()
    print("Type 0 for back to main menu")
    print("Enter comment or live blank (max 40 characters)")
    print()
    comment = input("Comment: ")
    if len(comment) > 40:
        make_table.from_elements(clear, host, port, user)
        print()
        print('Max 40 characters. Press enter')
        input()
        add_comment(lst, clear, host, port, user)
    elif str(comment) == '0':
        pass
    else:
        add_key(lst, clear, host, port, user, comment)

def add_key(lst, clear, host, port, user, comment):
    make_table.from_elements(clear, host, port, user, comment)
    print()
    print('G - Generate and assign new key')
    print('A - Assign exist key')
    print('N or live blank - No key')
    print('0 - Back to main menu')
    print()
    ch = input('You choice: ')
    platform = check_platform.check_platform()
    path_to_keys = platform[4]
    path_to_file = platform[3]
    if bool(re.match(r"[gG]", ch)) is True:
        paswrd = password.check_password(path_to_file, clear)
        pub_key, key = generate_key(path_to_keys, paswrd)
        make_table.from_elements(clear, host, port, user, comment, key)
        remove(f"{path_to_keys}/{key}.pub")
        print()
        if len(user) == 0:
            print(f'Copy and paste this key to: {host}:/home/user/.ssh/authorized_keys')
        else:
            print(f'Copy and paste this key to: {host}:/home/{user}/.ssh/authorized_keys')
        print()
        print(pub_key)
        print()
        print('Press enter')
        lst.append({'host': host, 'port': port, 'user': user, 'comment': comment, 'key': key})
        io_file.save_file(path_to_file, lst, paswrd)
        input()
    elif bool(re.match(r"[aA]", ch)) is True:
        make_table.from_elements(clear, host, port, user, comment)
        list_files = []
        for root, dirs, files in walk(path_to_keys):
            for filename in files:
                list_files.append(filename)
        print()
        no = 1
        print('List files, 0 - back:')
        for i in list_files:
            print(f"{no}. {i}")
            no += 1
        print()
        ch_number = input('Enter the number to bind the key: ')
        if ch_number.isdigit() is True:
            ch_number = int(ch_number)
        else:
            add_key(lst, clear, host, port, user, comment)
        if ch_number == 0:
            print('0')
            input()
            add_key(lst, clear, host, port, user, comment)
        elif len(list_files) >= ch_number >= 1:
            key = list_files[ch_number - 1]
            paswrd = password.check_password(path_to_file, clear)
            lst.append({'host': host, 'port': port, 'user': user, 'comment': comment, 'key': key})
            io_file.save_file(path_to_file, lst, paswrd)
        else:
            print('any')
            input()
            add_key(lst, clear, host, port, user, comment)
    elif bool(re.match(r"[nN]|[Nn][Oo]", ch)) is True or len(ch) == 0:
        lst.append({'host': host, 'port': port, 'user': user, 'comment': comment, 'key': ''})
        paswrd = password.check_password(path_to_file, clear)
        io_file.save_file(path_to_file, lst, paswrd)
    elif str(ch) == '0':
        pass
    else:
        make_table.from_elements(clear, host, port, user, comment)
        print()
        print('Wrong choice. Press Enter.')
        input()
        add_key(lst, clear, host, port, user, comment)

def generate_key(path, passwd):
    key_name = f'key-{strftime("%Y%m%d-%H%M%S")}'
    line_call = f'ssh-keygen -t rsa -f {path}/{key_name} -C {key_name}' #-N {passwd}  '
    system(line_call)
    with open(f"{path}/{key_name}.pub") as f:
        lines = f.readlines()
    print(lines[0])
    return lines[0], key_name
    '''key = RSA.generate(1024)
    f = open(f"{path}/{key_name}", "wb")
    f.write(key.exportKey('PEM'))
    f.close()
    platform = check_platform.check_platform()
    if platform[5] == 'linux':
        system(f'chmod 600 {path}/{key_name}')
    elif platform[5] == 'win':
        pass
    elif platform[5] == 'mac':
        pass

    pubkey = key.publickey()
    pubkey_print = re.findall(r"b\'{1}(.*)\'", str(pubkey.exportKey('OpenSSH')))
    return pubkey_print[0], key_name
    input()
'''

def del_host(lst, clear):
    if len(lst) == 0:
        make_table.from_list(lst, clear)
        print()
        print('No hosts. Press Enter')
        input()
    else:
        make_table.from_list(lst, clear)
        print()
        print('Enter the host number to delete. 0 - back')
        number = input('Host: ')
        if number.isdigit() is False:
            make_table.from_list(lst, clear)
            print()
            print('Wrong number. Press Enter')
            input()
            del_host(lst, clear)
        else:
            if str(number) == '0':
                pass
            elif len(lst) < int(number):
                make_table.from_list(lst, clear)
                print()
                print('Wrong number. Press Enter')
                input()
                del_host(lst, clear)
            else:
                number = int(number)
                if len(lst[number - 1]['key']) > 0:
                    key = '+'
                else:
                    key = ''
                make_table.from_elements(clear, lst[number - 1]['host'], lst[number - 1]['port'],
                                         lst[number - 1]['user'], key, lst[number - 1]['comment'])
                print()
                ch = input('Are you sure delete this record?(Yes/No): ')
                if check_yes_no(ch) is True:
                    platform = check_platform.check_platform()
                    path_to_keys = platform[4]
                    path_to_file = platform[3]
                    paswrd = password.check_password(path_to_file, clear)
                    remove(f"{path_to_keys}/{lst[number - 1]['key']}")
                    lst.pop(int(number) - 1)
                    io_file.save_file(path_to_file, lst, paswrd)
                else:
                    make_table.from_elements(clear, lst[number - 1]['host'], lst[number - 1]['port'],
                                             lst[number - 1]['user'], key, lst[number - 1]['comment'])
                    print()
                    print('Abort. Press Enter')
                    input()

def backup_menu(lst, clear):
    make_table.from_list(lst, clear)
    print()
    print("Command:")
    print("1 - Create backup")
    print("2 - Restore backup")
    print("0 - Back")
    print()
    chb = input('Enter command: ')
    if chb == '0':
        pass
    elif chb == '1':
        platform = check_platform.check_platform()
        path_to_file = platform[3]
        path_to_key = platform[4]
        home = platform[6]
        backup.backup(lst, clear, path_to_file, path_to_key, home)
    elif chb == '2':
        platform = check_platform.check_platform()
        path_to_file = platform[3]
        path_to_key = platform[4]
        backup.restore(lst, clear, path_to_key, path_to_file)
    else:
        make_table.from_list(lst, clear)
        print()
        print('Wrong command. Press Enter.')
        input()
        backup_menu(lst, clear)


def check_yes_no(ch):
    if bool(re.match(r"[Yy][eE][sS]|[Yy]", ch)) is True:
        return True
    elif bool(re.match(r"[Nn][oO]|[Nn]", ch)) is True:
        return False