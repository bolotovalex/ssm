from platform import system as ck
from os import system, mkdir, path

def check_platform():
    if ck() == 'Windows': #If platform Windows
        print('This is Windows')
        pass
        clear_command = 'cls'
        pip_v = 'pip'
        home = path.expanduser("~")
        home_local = home + str("\\.ssm\\")
        check = system(f'cd {home_local}')
        name_config = 'base.ssm'
        path_to_config = home_local + name_config
        path_to_keys = home_local + '.ssh\\'
        if check == 1:
            mkdir(home_local)
            system(f'type nul > {home_local}\\base.ssm')
            mkdir(path_to_keys)
        else:
            check = system(f'cd {path_to_keys}')
            if check == 1:
                mkdir(path_to_keys)
            if path.exists(path_to_config) == False:
                f = open(path_to_config, 'tw', encoding='utf-8')
                f.close()

    else: #If platform not Windows
        print('Detect unix system')
        home = path.expanduser('~')
        home_local = home + '/.ssm/'
        name_config = 'base.ssm'
        path_to_config = home_local + name_config
        path_to_keys = home + '/.ssh'
        clear_command = 'clear'
        pip_v = 'pip3'

        #1 Check ~/.ssm folder
        check_folder = path.exists(home_local) #Check ~/.config folder
        if check_folder is False:
            mkdir(home_local)

        #2 check ~/.ssh folder
        check_keys = path.exists(path_to_keys)  # Check ~/.ssh folder
        if check_keys is False:
            mkdir(path_to_keys)

        #3 check ~/.ssm/base.ssm file
        check_config = path.exists(path_to_config) #Check ~/.config/server.list file
        if check_config is False:
            f = open(path_to_config, 'tw', encoding='utf-8')
            f.close()

    return clear_command, pip_v, name_config, path_to_config, path_to_keys