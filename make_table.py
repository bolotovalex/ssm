from prettytable import PrettyTable as pt
from os import system

def make_table_from_list(lst, clear): 
    system(clear)
    number = int(1)
    table = pt()
    table.field_names = ["No", "Host", "Port", "User", "Key", "Comment"]
    for i in lst:
        table.add_row([number, i['host'], i['port'], i['user'], i['key'], i['comment']])
        number+=1
    print(table)

def make_table_from_line(dict, clear):
    #system(clear)
    table = pt()
    table.field_names = ["Host", "Port", "User", "Key", "Comment"]
    table.add_row([dict['host'], dict['port'], dict['user'], dict['key'], dict['comment']])
    print(table)