from check_platform import get_platfrom_params
import password
# import io_file
# import make_table
# import menu

if __name__ == '__main__':
    clear, path_to_file, ssh_key_folder, platform, home = get_platfrom_params()

    # Check file and password
    with open(path_to_file) as f:
        pass_in_file = f.readline()
        if len(pass_in_file) < 8:
            password = password.create_password(path_to_file, clear)
        else:
            password = password.check_password(path_to_file, clear)
    list_decode = io_file.load_file(path_to_file, password)

    while True:
        list_decode = io_file.load_file(path_to_file, password)
        make_table.from_list(list_decode, clear)
        menu.main_menu(list_decode, clear)
