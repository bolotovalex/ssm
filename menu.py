import re
import make_table
from os import system
import check_platform
from Crypto.PublicKey import RSA
import password
from time import strftime
import io_file


def main_menu(lst, clear):
    print()
    print('Type nubmer for connect or type command:')
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
                exit()

            if int(ch) > len(lst):
                make_table.from_list(lst, clear)
                print()
                print('Wrong number. Press Enter.')
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
        key = generate_key(path_to_keys)
        make_table.from_elements(clear, host, port, user, comment, key[1])
        print()
        if len(user) == 0:
            print(f'Copy and paste this key to: {host}:/home/user/.ssh/authorized_keys')
        else:
            print(f'Copy and paste this key to: {host}:/home/{user}/.ssh/authorized_keys')
        print()
        print(key[0])
        print()
        print('Press enter')
        lst.append({'host': host, 'port': port, 'user': user, 'comment': comment, 'key': key[1]})
        io_file.save_file(path_to_file, lst, paswrd)
        input()
    elif bool(re.match(r"[aA]", ch)) is True:
        print('In develop')
        input()
    elif bool(re.match(r"[nN]", ch)) is True or len(ch) == 0:
        print('In develop')
        input()
    elif str(ch) == '0':
        pass
    else:
        make_table.from_elements(clear, host, port, user, comment)
        print()
        print('Wrong choice. Press Enter.')
        input()
        add_key(lst, clear, host, port, user, comment)


def generate_key(path):
    key_name = f'key-{strftime("%Y%m%d-%H%M%S")}'
    key = RSA.generate(1024)
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


def del_host(lst, clear):
    print('Del host')
    input()


def backup_menu(lst, clear):
    print('backup menu')
    input()


def assign_key():
    pass
