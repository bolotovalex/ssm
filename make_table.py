from prettytable import PrettyTable as Pt
from os import system


def from_list(lst, clear):
    system(clear)
    number = int(1)
    table = Pt()
    table.field_names = ["No", "Host", "Port", "User", "Key", "Comment"]
    if len(lst) != 0:
        for i in lst:
            if len(i['key']) != 0:
                table.add_row([number, i['host'], i['port'], i['user'], 'Yes', i['comment']])
                number += 1
            else:
                table.add_row([number, i['host'], i['port'], i['user'], 'No', i['comment']])
                number += 1
    print(table)


def from_elements(clear, host='', port='', user='', comment='', key=''):
    system(clear)
    table = Pt()
    table.field_names = ["Host", "Port", "User", "Key", "Comment"]
    table.add_row([host, port, user, key, comment])
    print(table)
