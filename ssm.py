# This is a sample Python script.
import getpass
import check_platform as ck
import password
import prettytable
import make_table
import io_file
import menu
import encode

list_decode = [{'host': 'csys.su', 'port': '22', 'user': 'ilexx', 'key': 'key.ppk', 'comment': 'comment'},{'host': '1.su', 'port': '2022', 'user': '234', 'key': 'key2.ppk', 'comment': 'comment2'}]

if __name__ == '__main__':
    check_platform = ck.check_platform()
    clear = check_platform[0]
    pip = check_platform[1]
    file_base = check_platform[2]
    path_to_file = check_platform[3]
    ssh_key_folder = check_platform[4]

    #Check file and password
    with open(path_to_file) as f:
        pass_in_file = f.readline()
        if len(pass_in_file) < 8:
            password = password.create_password(path_to_file, clear)
        else:
            password = password.check_password(path_to_file, clear)

    while True:
        #lst = io_file.load_file(path_to_file, password)
        #io_file.load_file(path_to_file, password)
        #io_file.save_file(path_to_file, list_decode, password)
        #menu.main_menu()
        print(io_file.load_file(path_to_file, password))
        input('p')
        pass



