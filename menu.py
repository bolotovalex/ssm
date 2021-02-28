import re
import make_table
from os import system


def main_menu(lst, clear):
    print()
    print('Type nubmer for connect or type command:')
    print(' a - Add new host')
    print(' d - Delete host')
    # print(' m - Manage key')
    print(' r - Backup / Restore db file, keys')
    print(' 0 - Exit')
    print()
    ch = input(' Enter number for connect or letter for config: ')
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
    make_table.from_list(lst, clear)
    print()
    host = input("Enter hostname, 0 - back: ")
    if len(host) == 0:
        print("Wrong hostname. Press Enter and retype hostname. To exit enter 0.")
        input()
        add_host(lst, clear)
    elif str(host) == '0':
        pass
    else:
        add_port(lst, clear, host)


def add_port(lst, clear, host):
    make_table.from_list(lst, clear)
    print()
    print("Type 0 for back to main menu")
    port = input(f"Enter port for {host} (Press enter for default port = 22): ")
    if len(port) == 0:
        print("Default 22")
        port = "22"
        add_user(lst, clear, host, port)
    elif str(port) == '0':
        pass
    elif port.isdigit() is False:
        make_table.from_list(lst, clear)
        print("Wrong port. Must be digit. Press Enter")
        add_port(lst, clear, host)
    elif int(port) < 0 or int(port) > 65536:
        make_table.from_list(lst, clear)
        print()
        print("Wrong port. Port must be 1-65536. Press Enter")
        input()
        add_port(lst, clear, host)
    else:
        add_user(lst, clear, host, port)


def add_user(lst, clear, host, port):
    user = 'user'
    add_key(lst, clear, host, port, user)

def add_key(lst, clear, host, port, user):
    key = 'key'
    add_comment(lst, clear, host, port, user, key)

def add_comment(lst, clear, host, port, user, key):
    comment = 'commnet'
    make_table.from_list(lst, clear)
    print()
    print(host)
    print(port)
    print(user)
    print(key)
    print(comment)
    input()


def del_host(lst, clear):
    print('Del host')
    input()


def backup_menu(lst, clear):
    print('backup menu')
    input()


def generate_key():
    pass


def assign_key():
    pass
