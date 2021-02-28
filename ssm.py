# This is a sample Python script.
import check_platform as ck
import password
import io_file
import make_table
import menu

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
    list_decode = io_file.load_file(path_to_file, password)

    while True:
        make_table.from_list(list_decode, clear)
        menu.main_menu(list_decode, clear)


