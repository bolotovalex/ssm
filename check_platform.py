from platform import system
from os import system, mkdir, path, name

def get_platfrom_params():
    if name == 'nt': #If Windows
        platform = 'windows'
        clear = system('cls')
    else:
        platform = 'unix'
        clear = system('clear')
    
    home = path.expanduser("~")
    home_local = path.join(home, ".ssm")
    path_to_config = path.join(home_local, 'base.ssm')
    path_to_keys = path.join(home_local, 'keys')
    #1 Check ~/.ssm folder
    
    if path.exists(home_local) is False:
        mkdir(home_local)
    
    #2 check ~/.ssh folder
    if path.exists(path_to_keys) is False:
        mkdir(path_to_keys)

    #3 check ~/.ssm/base.ssm file
    if path.exists(path_to_config) is False:
        f = open(path_to_config, 'tw', encoding='utf-8')
        f.close()
    
    return clear, path_to_config, path_to_keys, platform, home

   
   