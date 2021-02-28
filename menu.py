import re
import make_table
from os import system
def main_menu(lst, clear):
    print()
    print('Type nubmer for connect or type command:')
    print(' a - Add new host')
    print(' d - Delete host')
    print(' m - Manage key')
    print(' b / r - Backup / Restore db file, keys')
    print(' 0 - Exit')
    print()
    ch = input(' Enter number for connect or letter for config: ')
    check_input(ch, lst, clear)

def check_input(ch, lst, clear):
    if bool(re.match(r"[0-9]|[aAdDmMbBrRфФвВьЬиИкК]", ch)) is True:
        if bool(re.match(r"[0-9]", ch)) is True:
            if int(ch) == 0:
                system(clear)
                exit()

            if int(ch) > len(lst):
                make_table.from_list(lst, clear)
                print()
                print('Wrong number. Press Enter.')
                input()

    else:
        make_table.from_list(lst, clear)
        print()
        print('Wrong input. Press Enter')
        input()