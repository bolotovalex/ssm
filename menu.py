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

        # elif bool(re.match(r"[mMьЬ]", ch)) is True:
        #    manage_key_menu(lst, clear)

        elif bool(re.match(r"[rRкК]", ch)) is True:
            backup_menu(lst, clear)

    else:
        make_table.from_list(lst, clear)
        print()
        print('Wrong input. Press Enter')
        input()


def add_host(lst, clear):
    print('Add host')
    input()


def del_host(lst, clear):
    print('Del host')
    input()


# def manage_key_menu(lst, clear):
#    print('manage key menu')
# input()

def backup_menu(lst, clear):
    print('backup menu')
    input()
